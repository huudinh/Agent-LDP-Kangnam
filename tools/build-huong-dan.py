#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng trang hướng dẫn Agent-LDP-Kangnam — nhúng nội dung thật từ repo Agent-LDP-Kangnam.

Chay:  python tools/build-huong-dan.py
Ket qua: tools/huong-dan.html  -> publish de lai cung URL artifact
(https://claude.ai/artifact/JvyWoqxudQFfN5szP2x5ZQ), xem README muc "Huong dan cai dat".
Sua noi dung trang thi sua tools/huong-dan-kla.tpl.html, khong sua file .html sinh ra."""
import io, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "huong-dan.html")

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


# ---------------------------------------------------------------- prompts
PROMPT_FILES = [
    ("wizard", "Hỏi dẫn từ đầu", "prompts/prompt-wizard.md"),
    ("landing", "Dựng landing", "prompts/prompt-landing.md"),
    ("audit", "Audit trang đang chạy", "prompts/prompt-audit.md"),
    ("variant", "Chuyển kênh & biến thể", "prompts/prompt-variant.md"),
]


def parse_prompts(path):
    """Rút prompt từ file .md: khối ``` , dòng bảng có prompt trong backtick,
    và các câu trích dạng 1. *"..."*. Giữ nguyên văn, không viết lại."""
    lines = io.open(os.path.join(REPO, path), encoding="utf-8").read().split("\n")
    out, head, i = [], None, 0
    while i < len(lines):
        l = lines[i]
        if re.match(r"^#{2,3} ", l):
            head = re.sub(r"^#{2,3} ", "", l).strip()
            i += 1
            continue
        if l.strip() == "```":
            j, buf = i + 1, []
            while j < len(lines) and lines[j].strip() != "```":
                buf.append(lines[j])
                j += 1
            out.append(("full", head, "\n".join(buf).strip()))
            i = j + 1
            continue
        if l.startswith("|") and l.count("`") >= 2:
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cells) >= 2 and re.fullmatch(r"`[^`]+`", cells[-1]):
                out.append(("short", re.sub(r"[*`]", "", cells[0]).strip(), cells[-1].strip("`")))
            i += 1
            continue
        m = re.match(r'^\d+\.\s+\*"(.+)"\*\s*$', l)
        if m:
            out.append(("short", head, m.group(1)))
            i += 1
            continue
        i += 1
    return out


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def clean_title(t):
    t = re.sub(r"^[A-E]\d?\. ", "", t or "")
    t = re.sub(r"\s*—\s*nhớ khai cách xử lý tuyến$", "", t)
    return t.strip()


def build_prompts(payload):
    cards, n = [], 0
    counts = {}
    for key, label, path in PROMPT_FILES:
        items = parse_prompts(path)
        counts[key] = len(items)
        seen = {}
        for kind, title, body in items:
            n += 1
            pid = "p%d" % n
            payload[pid] = body
            t = clean_title(title)
            seen[t] = seen.get(t, 0) + 1
            if seen[t] > 1 or (kind == "short" and title and title.startswith("E.")):
                t = "%s · %d" % (t, seen[t])
            cards.append(
                '<article class="prompt" data-g="%s">'
                '<div class="prompt-h"><span class="n">%02d</span>'
                '<span class="t">%s</span><span class="k">%s</span></div>'
                '<pre class="prompt-b">%s</pre>'
                '<div class="prompt-f"><span class="get">%s · %s ký tự</span>'
                '<button class="copy" data-copy="%s">Copy prompt</button></div>'
                "</article>"
                % (key, n, esc(t), "Đầy đủ" if kind == "full" else "Một dòng",
                   esc(body), label, fmt(len(body)), pid)
            )
    return "\n".join(cards), n, counts


def build_files(payload):
    """Mỗi file tri thức một thẻ: copy riêng + xem nội dung. Dùng khi không tải được ZIP."""
    cards = []
    items = [(n + ".md", t, d, st, "knowledge/" + n + ".md") for n, t, d, st in KF_ORDER]
    items.append(("lp-skeleton.html", "Khung HTML landing",
                  "Khung 9 màn, form + bottom sheet, sticky bar — để /prototype dựng đúng ngay lần đầu",
                  False, "template/lp-skeleton.html"))
    for i, (fname, title, desc, star, rel) in enumerate(items, 1):
        body = io.open(os.path.join(REPO, rel), encoding="utf-8").read()
        fid = "f%d" % i
        payload[fid] = body
        cards.append(
            '<article class="fcard%s">'
            '<div class="fcard-h"><span class="fname">%s</span>%s'
            '<span class="fsize">%s ký tự</span>'
            '<button class="copy" data-copy="%s">Copy</button></div>'
            '<p class="fhow"><b>%s</b> — %s</p>'
            '<details class="fview"><summary>Xem nội dung</summary>'
            '<pre class="filebody">%s</pre></details>'
            "</article>"
            % (" hi" if star else "", esc(fname),
               '<span class="fbadge up">★ lõi</span>' if star else "",
               fmt(len(body)), fid, esc(title), desc, esc(body[:3000]) +
               ("\n\n… (còn %s ký tự — bấm Copy để lấy đủ)" % fmt(len(body) - 3000) if len(body) > 3000 else ""))
        )
    return "\n".join(cards)


brain = copyblock("SYSTEM-PROMPT.md")
short = copyblock("SYSTEM-PROMPT-NGAN.md")

parts = []
for name, _t, _d, _s in KF_ORDER:
    parts.append("<!-- ===== %s.md ===== -->\n\n%s" % (name, kf(name)))
merged = ("# TRI THỨC GỘP — AGENT-LDP-KANGNAM\n"
          "# 8 file knowledge nối liền, thứ tự đọc: pháp lý → hành vi → thương hiệu → thiết kế\n"
          "# Dùng khi nền tảng không cho upload nhiều file. Bản gốc: Agent-LDP-Kangnam/knowledge/\n\n"
          + "\n\n".join(parts))

payload = {"a": brain, "b": short, "c": merged}
prompt_cards, prompt_n, prompt_counts = build_prompts(payload)
file_cards = build_files(payload)
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

html = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "huong-dan.tpl.html"),
               encoding="utf-8").read()
html = (html
        .replace("@@KF_ROWS@@", kf_rows)
        .replace("@@LEN_A@@", fmt(len(brain)))
        .replace("@@LEN_B@@", fmt(len(short)))
        .replace("@@LEN_C@@", fmt(len(merged)))
        .replace("@@KB_C@@", str(round(len(merged.encode("utf-8")) / 1024)))
        .replace("@@FILE_CARDS@@", file_cards)
        .replace("@@PROMPT_CARDS@@", prompt_cards)
        .replace("@@PROMPT_N@@", str(prompt_n))
        .replace("@@N_WIZARD@@", str(prompt_counts["wizard"]))
        .replace("@@N_LANDING@@", str(prompt_counts["landing"]))
        .replace("@@N_AUDIT@@", str(prompt_counts["audit"]))
        .replace("@@N_VARIANT@@", str(prompt_counts["variant"]))
        .replace("@@PAYLOAD@@", blob))

io.open(OUT, "w", encoding="utf-8").write(html)
print("Da ghi:", OUT, "-", round(os.path.getsize(OUT) / 1024), "KB")
print("The A:", fmt(len(brain)), "| The B:", fmt(len(short)), "| The C:", fmt(len(merged)))
print("Prompt:", prompt_n, prompt_counts)
