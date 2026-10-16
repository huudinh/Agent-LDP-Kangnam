#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng trang hướng dẫn KLA — nhúng nội dung thật từ repo Agent-LDP-Kangnam.

Chay:  python tools/build-huong-dan.py
Ket qua: tools/huong-dan-kla.html  -> publish de lai cung URL artifact
(https://claude.ai/artifact/JvyWoqxudQFfN5szP2x5ZQ), xem README muc "Huong dan cai dat".
Sua noi dung trang thi sua tools/huong-dan-kla.tpl.html, khong sua file .html sinh ra."""
import io, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "huong-dan-kla.html")

KF_ORDER = [
    ("KF-11-cong-phap-ly", "Cổng pháp lý + bảng rào R0–R12", "Rà mọi output. Fail = không xuất trang", True),
    ("KF-12-hanh-vi-khach-hang", "Hành vi khách hàng", "6 nhóm · 3 rào cản · 5 mức nhận thức · 6 giai đoạn", True),
    ("KF-13-noi-so-phan-doi", "Nỗi sợ &amp; phản đối theo BL", "Kèm câu trả lời đã rà từ cấm + bằng chứng được dùng", True),
    ("KF-01-ho-so-thuong-hieu", "Hồ sơ thương hiệu", "Bác sĩ · cơ sở + tuyến · taxonomy · nguồn dữ liệu live", False),
    ("KF-14-proof-bank", "Proof Bank", "Bằng chứng được phép dùng + trạng thái pháp lý từng loại", False),
    ("KF-15-block-library", "Thư viện khối landing", "24 mã khối B-* map vào 9 màn", False),
    ("KF-09-design-system", "Design System v3.0", "Token · khung trang · form · ô ảnh tạm · chuẩn giao HTML", False),
    ("KF-16-performance-log", "Performance Log", "Vòng học — hiện đang trống, chờ dữ liệu thật", False),
]


def copyblock(path):
    s = io.open(os.path.join(REPO, path), encoding="utf-8").read()
    m = re.search(r"```\n(.*?)\n```", s, re.S)
    if not m:
        sys.exit("Khong tim thay khoi copy trong " + path)
    return m.group(1)


def kf(name):
    return io.open(os.path.join(REPO, "knowledge", name + ".md"), encoding="utf-8").read()


def fmt(n):
    return "{:,}".format(n).replace(",", ".")


brain = copyblock("SYSTEM-PROMPT.md")
short = copyblock("SYSTEM-PROMPT-NGAN.md")

parts = []
for name, _t, _d, _s in KF_ORDER:
    parts.append("<!-- ===== %s.md ===== -->\n\n%s" % (name, kf(name)))
merged = ("# TRI THỨC GỘP — KANGNAM LANDING AGENT (KLA)\n"
          "# 8 file knowledge nối liền, thứ tự đọc: pháp lý → hành vi → thương hiệu → thiết kế\n"
          "# Dùng khi nền tảng không cho upload nhiều file. Bản gốc: Agent-LDP-Kangnam/knowledge/\n\n"
          + "\n\n".join(parts))

payload = {"a": brain, "b": short, "c": merged}
blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")

rows = []
for name, title, desc, star in KF_ORDER:
    n = len(kf(name))
    rows.append(
        '<tr%s><td><code>%s.md</code>%s</td><td><b>%s</b><br><span class="dim">%s</span></td>'
        '<td class="num">%s</td></tr>'
        % (' class="hl"' if star else "", name, ' <span class="star">★</span>' if star else "", title, desc, fmt(n))
    )
kf_rows = "\n".join(rows)

html = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "huong-dan-kla.tpl.html"),
               encoding="utf-8").read()
html = (html
        .replace("@@KF_ROWS@@", kf_rows)
        .replace("@@LEN_A@@", fmt(len(brain)))
        .replace("@@LEN_B@@", fmt(len(short)))
        .replace("@@LEN_C@@", fmt(len(merged)))
        .replace("@@KB_C@@", str(round(len(merged.encode("utf-8")) / 1024)))
        .replace("@@PAYLOAD@@", blob))

io.open(OUT, "w", encoding="utf-8").write(html)
print("Da ghi:", OUT, "-", round(os.path.getsize(OUT) / 1024), "KB")
print("The A:", fmt(len(brain)), "| The B:", fmt(len(short)), "| The C:", fmt(len(merged)))
