#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch-du-lieu.py — lấy dữ liệu live của Kangnam về làm bản chụp cho Agent-LDP-Kangnam.

Năm nguồn chính thống (xem knowledge/KF-01 mục §0):
  bác sĩ   /doi-ngu-bac-si/        -> JSON nhúng id="kn-doctors-data"
  dịch vụ  menu chính (trang chủ)  -> nhóm + dịch vụ trong mega menu
  cơ sở    /chi-nhanh/             -> tên + địa chỉ + giấy phép
  case     /case-thuc-te/          -> số case đang có theo nhóm lọc
  ảnh      /hinh-anh-khach-hang/   -> nhóm dịch vụ có ảnh

Dùng:
    python tools/fetch-du-lieu.py                 # in tóm tắt ra màn hình
    python tools/fetch-du-lieu.py --out out/      # ghi snapshot JSON + MD

Script KHÔNG tự sửa file knowledge. Nó đưa dữ liệu để người thật đối chiếu
rồi cập nhật KF-01 / KF-14 — vì mỗi thay đổi về bác sĩ, cơ sở, case đều
chạm rào pháp lý (R3, R4, R5) và cần người duyệt.
"""

import argparse
import datetime as _dt
import html
import json
import os
import re
import sys
import urllib.request

BASE = "https://benhvienthammykangnam.com.vn"
UA = "Mozilla/5.0 (compatible; Agent-LDP-Kangnam-snapshot/1.0)"
TIMEOUT = 60

PAGES = {
    "bac_si": "/doi-ngu-bac-si/",
    "co_so": "/chi-nhanh/",
    "case": "/case-thuc-te/",
    "anh": "/hinh-anh-khach-hang/",
    "menu": "/",
}


def get(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read().decode("utf-8", "replace")


def to_text(s):
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?is)</(p|div|li|h[1-6]|tr|td|section|span|a)>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return [l.strip() for l in s.split("\n") if l.strip()]


# ---------------------------------------------------------------- bác sĩ
def parse_bac_si(raw):
    """Danh sách bác sĩ nằm trong JSON nhúng, không phải trong DOM."""
    m = re.search(r'id="kn-doctors-data"[^>]*>(.*?)</script>', raw, re.S)
    if not m:
        return {"loi": "khong tim thay kn-doctors-data — markup trang da doi"}
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        return {"loi": "JSON hong: %s" % e}

    thieu_cchn = [d["name"] for d in data if not d.get("cchn")]
    chua_verified = [d["name"] for d in data if d.get("status") != "verified"]
    theo_nhom = {}
    for d in data:
        theo_nhom.setdefault(d.get("group", "?"), []).append(d["name"])

    return {
        "tong": len(data),
        "thieu_cchn": thieu_cchn,
        "chua_verified": chua_verified,
        "theo_nhom": theo_nhom,
        "theo_khu_vuc": sorted({d.get("area", "?") for d in data}),
        "danh_sach": data,
    }


# ---------------------------------------------------------------- cơ sở
def parse_co_so(raw):
    lines = to_text(raw)
    tong = None
    for l in lines:
        m = re.search(r"có\s+(\d+)\s+cơ sở", l, re.I)
        if m:
            tong = int(m.group(1))
            break
    dia_chi = [l for l in lines if re.match(r"^\d+\s+[A-ZĐÀ-Ỹ]", l) and len(l) < 120]
    gp = sorted(set(re.findall(r"\d{2,4}/BYT-GPHĐ", raw)))
    return {"tong_tren_trang": tong, "giay_phep": gp, "dia_chi_bat_duoc": dia_chi[:12]}


# ---------------------------------------------------------------- case
def parse_case(raw):
    lines = to_text(raw)
    trong = any("Chưa có ca nào" in l for l in lines)
    nhom = []
    for l in lines:
        m = re.search(r"(\d+)\s+nhóm dịch vụ", l)
        if m:
            nhom.append(int(m.group(1)))
    return {
        "dang_trong": trong,
        "so_nhom_khai_tren_trang": nhom[0] if nhom else None,
        "canh_bao": "Trang trong -> man 5 phai dung PLACEHOLDER" if trong else "",
    }


# ---------------------------------------------------------------- ảnh
def parse_anh(raw):
    lines = to_text(raw)
    nhom = None
    for i, l in enumerate(lines):
        if l.strip() == "Nhóm dịch vụ" and i and lines[i - 1].strip().isdigit():
            nhom = int(lines[i - 1].strip())
            break
    co_consent = any("đồng ý của khách hàng" in l for l in lines)
    co_mien_tru = any("phụ thuộc cơ địa" in l for l in lines)
    return {
        "so_nhom": nhom,
        "co_khai_consent": co_consent,
        "co_cau_mien_tru": co_mien_tru,
    }


# ---------------------------------------------------------------- menu
def parse_menu(raw):
    """Mega menu Dịch vụ: lấy nhóm + dịch vụ con để đối chiếu KF-01 mục 5."""
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{2,60})</a>', raw)
    bo = {"Trang chủ", "Hotline", "Đặt lịch"}
    ten = []
    for href, text in links:
        t = html.unescape(text).strip()
        if t and t not in bo and "/" in href and BASE in href:
            ten.append(t)
    return {"so_link_menu_bat_duoc": len(ten), "mau": ten[:40]}


PARSERS = {
    "bac_si": parse_bac_si,
    "co_so": parse_co_so,
    "case": parse_case,
    "anh": parse_anh,
    "menu": parse_menu,
}


def main():
    # Console Windows mac dinh cp1252 -> in tieng Viet se vo. Ep UTF-8.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description="Chup du lieu live Kangnam cho Agent-LDP-Kangnam")
    ap.add_argument("--out", help="thu muc ghi snapshot (vd out/)")
    ap.add_argument("--chi", nargs="*", choices=sorted(PAGES), help="chi lay vai nguon")
    args = ap.parse_args()

    can_lay = args.chi or list(PAGES)
    ngay = _dt.date.today().isoformat()
    kq = {"ngay_chup": ngay, "base": BASE, "nguon": {}}

    for ten in can_lay:
        path = PAGES[ten]
        try:
            raw = get(path)
        except Exception as e:  # noqa: BLE001 — muốn báo lỗi chứ không dừng
            kq["nguon"][ten] = {"url": BASE + path, "loi": str(e)}
            print("[LOI] %-7s %s -> %s" % (ten, path, e), file=sys.stderr)
            continue
        kq["nguon"][ten] = dict(PARSERS[ten](raw), url=BASE + path)
        print("[OK ] %-7s %s (%d KB)" % (ten, path, len(raw) // 1024))

    bs = kq["nguon"].get("bac_si", {})
    if "tong" in bs:
        print("\n--- BAC SI ---")
        print("  tong:", bs["tong"], "| khu vuc:", ", ".join(bs["theo_khu_vuc"]))
        print("  thieu CCHN (%d):" % len(bs["thieu_cchn"]), ", ".join(bs["thieu_cchn"]) or "-")
        print("  chua verified (%d):" % len(bs["chua_verified"]), ", ".join(bs["chua_verified"]) or "-")
        for g, names in sorted(bs["theo_nhom"].items()):
            print("    %-9s %d" % (g, len(names)))

    cs = kq["nguon"].get("co_so", {})
    if cs and "loi" not in cs:
        print("\n--- CO SO ---")
        print("  tong tren trang:", cs["tong_tren_trang"], "| giay phep:", ", ".join(cs["giay_phep"]))

    ca = kq["nguon"].get("case", {})
    if ca and "loi" not in ca:
        print("\n--- CASE ---")
        print("  dang trong:", ca["dang_trong"], ca["canh_bao"])

    an = kq["nguon"].get("anh", {})
    if an and "loi" not in an:
        print("\n--- ANH TRUOC SAU ---")
        print("  so nhom:", an["so_nhom"], "| khai consent:", an["co_khai_consent"],
              "| cau mien tru:", an["co_cau_mien_tru"])

    if args.out:
        os.makedirs(args.out, exist_ok=True)
        p = os.path.join(args.out, "kangnam-snapshot-%s.json" % ngay)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(kq, f, ensure_ascii=False, indent=1)
        print("\nDa ghi:", p)
        print("Doi chieu voi knowledge/KF-01 muc 2,4,5 va KF-14 muc 1 roi cap nhat tay.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
