# KF-09 — DESIGN SYSTEM LANDING KANGNAM v3.0 (chuẩn giao HTML)
Version: 1.0 · Nguồn: `Agent-AdsOptimize-Kangnam/knowledge/kn-khung-landing.md` v3.0 — token lấy **nguyên** từ trang production
Cập nhật: 2026-10-16

**Trang mẫu chuẩn:** `https://benhvienthammykangnam.com.vn/quyen-loi-thanh-vien/dep-ven-tron/` (bản lưu: `Agent-AdsOptimize-Kangnam/template/dep-ven-tron.html`)

> ⚠️ **Lấy GÌ và KHÔNG lấy gì từ trang mẫu.** Đây là trang quyền lợi thành viên (`noindex`, 3 section).
> ✅ Lấy: token màu · khung trang · header/footer · form + bottom sheet · sticky/shimmer CTA · nhịp trình bày mobile.
> ❌ **Không lấy cấu trúc nội dung** — 3 section của nó không phải khung landing chạy ads. Thứ tự màn lấy từ §6 của bộ não (9 màn).

---

## 1. ⚠️ BA BẢNG MÀU ĐANG TỒN TẠI — DÙNG BẢNG NÀO

| Bảng | Giá trị | Dùng cho |
|---|---|---|
| **Production v3.0** ✅ | navy `#074E84` · CTA `#EF6103` | **Dựng landing — dùng bảng này**, để trang mới khớp trang đang chạy |
| Nhận diện cấp thương hiệu | navy `#003c77` · CTA `#f6871f` | Ấn phẩm cấp brand: profile, brochure, biển hiệu |
| Spec KLA đề xuất 🔶 | `#294573` · accent `#3A6CAE` · teal `#2F8E7E` · gold `#9F7131` · nude `#F6F1ED` · peach `#F9E6D7` | **Chưa dùng.** Bảng này đến từ spec KLA, chưa đối chiếu tương phản và chưa khớp production |

**Luật:** landing dùng **token production** ở mục 2. Muốn chuyển sang bảng KLA thì phải chạy lại kiểm tương phản WCAG cho từng cặp màu và **brand + pháp chế chốt một lần** — xem *Việc còn treo* ở [`doc/CHANGELOG.md`](../doc/CHANGELOG.md). ⛔ Không trộn hai bảng trong một trang.

---

## 2. TOKEN MÀU (production)

```css
:root{
  --navy:#074E84; --navy-900:#04365E; --navy-950:#022544;
  --ynavy:#1F5FC4; --cyan:#00A5E0;
  --gold:#A66E29;  --amber:#FBBF65;  --terra:#D77927;
  --cta:#EF6103;   --cta-press:#CF5300;
  --bg:#F3F6FA;    --surface:#FFFFFF;
  --ink:#0E2338;   --ink-2:#4A5C70;  --ink-3:#6E7E90;
  --line:#DCE3EC;  --ok:#1E8E5A;     --err:#C62828; --err-t:#FDECEC;
  /* màu nhóm dịch vụ — chip, viền card, dot trong bottom sheet */
  --g-spa:#00A5E0;  --g-spa-t:#E2F5FC;    /* Beauty & Spa  */
  --g-pttm:#1F5FC4; --g-pttm-t:#E8EFFB;   /* Phẫu thuật TM */
  --g-nk:#A66E29;   --g-nk-t:#FCF1DF;     /* Nha khoa      */
  --g-oth:#6E7E90;  --g-oth-t:#EEF1F5;    /* Khác          */
  --r-sm:8px; --r:14px; --r-lg:20px;
  --sh:0 2px 10px rgba(7,78,132,.08);
  --sh-lg:0 10px 30px rgba(2,37,68,.16);
  --hdr-h:56px;
}
```

| Luật | |
|---|---|
| **Tỷ lệ** | 80% trắng/`--bg` · 15% navy · 5% cam CTA. ⛔ Không nền toàn navy |
| **Nền trang** | `#D9E0E8` — để khối `--bg` ở giữa nổi lên như một thẻ |
| **`--cta` là màu NỀN NÚT, không phải màu chữ** | Chữ trắng trên `--cta` chỉ đạt **3,29:1** → chữ trên nút cam phải **≥ 19px/800** (ngưỡng large-text AA). Nút nhỏ hơn → đổi sang `--navy` (trắng trên navy = 8,63 AAA) |
| ⛔ **Cấm** | `--amber` làm chữ trên trắng (**1,65:1**) — amber **chỉ** dùng trên navy (9,43 AAA) và làm vạch trang trí · `--cyan` làm chữ trên trắng (**2,82:1**) — cyan chỉ là màu nhóm/viền · `--ink-3` cho chữ nhỏ (3,84) — chữ phụ dùng `--ink-2` (6,87 AA) |
| **An toàn** | `--navy` trên trắng 8,63 AAA · `--ink` trên `--bg` 14,72 AAA · `--gold` trên trắng 4,30 → **chỉ heading ≥ 18px** · `--err` trên trắng 5,62 AA |

**Chỉ MỘT màu dành cho CTA trên toàn trang** — nhất quán từ màn 1 đến màn 9.

---

## 3. KHUNG TRANG — nền · container · header · footer · sticky

Mọi landing dùng **đúng bộ khung này**, chỉ thay các `<section>` ở giữa.

```css
*{box-sizing:border-box} html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;font:400 15px/1.55 var(--f);color:var(--ink);background:#D9E0E8}
img{max-width:100%}
:focus-visible{outline:3px solid var(--amber);outline-offset:2px;border-radius:6px}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto} *{transition:none!important;animation:none!important}}

/* container: thẻ khổ điện thoại, căn giữa trên nền xám xanh */
.app{max-width:480px;margin:0 auto;background:var(--bg);min-height:100vh;
  box-shadow:0 0 0 1px rgba(0,0,0,.04),0 20px 60px rgba(0,0,0,.12);
  padding-bottom:env(safe-area-inset-bottom,0px);position:relative;overflow-x:clip}
.wrap{padding-inline:16px}
section{position:relative;padding:44px 0 36px}

/* header: sticky, kính mờ, logo + 1 CTA cam */
.hdr{position:sticky;top:0;z-index:60;display:flex;align-items:center;
  justify-content:space-between;gap:10px;min-height:var(--hdr-h);padding:9px 14px;
  padding-top:calc(9px + env(safe-area-inset-top,0px));
  background:rgba(243,246,250,.86);backdrop-filter:blur(10px);
  -webkit-backdrop-filter:blur(10px);border-bottom:1px solid rgba(220,227,236,.75)}
.hdr__logo img{max-height:34px;width:auto;display:block}
.hdr__cta{flex-shrink:0;display:inline-flex;align-items:center;gap:6px;
  background:var(--cta);color:#fff;font-weight:800;font-size:12.5px;
  padding:10px 15px;border-radius:999px;border:0;white-space:nowrap;
  box-shadow:0 4px 12px rgba(239,97,3,.3)}

/* tiêu đề section: pre serif vàng + main navy + vạch amber */
.sec-head{text-align:center;margin-bottom:20px}
.sec-head .pre{display:block;font:italic 600 18px/1.3 var(--f2);color:var(--gold)}
.sec-head .main{display:block;font-size:26px;font-weight:800;color:var(--navy);
  letter-spacing:-.2px;margin-top:2px}
.sec-head .bar{display:block;width:48px;height:3px;border-radius:3px;
  background:var(--amber);margin:12px auto 0}

/* nút */
.btn{display:flex;align-items:center;justify-content:center;gap:8px;min-height:52px;
  width:100%;border:0;border-radius:999px;padding:12px 22px;font-weight:800;
  letter-spacing:.3px;text-decoration:none;transition:transform .12s,background-color .15s}
.btn-cta{background:var(--cta);color:#fff;font-size:19px;text-transform:uppercase;
  box-shadow:0 6px 18px rgba(239,97,3,.38)}          /* 19px/800 — ngưỡng tương phản */
.btn-cta:hover{background:var(--cta-press)}
.btn-cta:active{transform:scale(.98);background:var(--cta-press)}
.btn-outline{background:#fff;color:var(--navy);box-shadow:inset 0 0 0 1.5px var(--navy);
  font-size:15px;min-height:46px;font-weight:700}

/* card nhóm dịch vụ: viền trên theo màu nhóm */
.gcard{background:var(--surface);border-radius:var(--r-lg);box-shadow:var(--sh);
  overflow:hidden;border-top:4px solid var(--gc)}
.gcard[data-g="spa"]{--gc:var(--g-spa);--gct:var(--g-spa-t)}
.gcard[data-g="pttm"]{--gc:var(--g-pttm);--gct:var(--g-pttm-t)}
.gcard[data-g="nk"]{--gc:var(--g-nk);--gct:var(--g-nk-t)}

/* footer */
.foot{position:relative;background:#f1f1ef;color:#254770;padding:26px 14px 30px;
  text-align:center}
.ft__license{font-size:12.5px;font-style:italic;line-height:1.55;margin-top:8px}
.ft__hot{display:flex;align-items:center;justify-content:center;gap:12px;max-width:270px;
  margin:18px auto 0;padding:10px 22px;border-radius:55px;
  background:linear-gradient(90deg,#fec465 0%,#c28710 100%);color:#fff;
  font-weight:700;text-decoration:none}
.ft__hot-num{display:block;font-size:24px;font-weight:800}
```

**Luật khung trang**
- `.app` là **480px** — khớp production. `.sticky-bar` phải cùng `max-width:480px`, nếu không sẽ lệch trên desktop.
- Header **sticky, kính mờ**, chỉ chứa **logo + 1 CTA cam**. Không nhồi menu, không nhồi 3 nút.
- `--hdr-h:56px` dùng cho `scroll-margin-top` của mọi section có anchor — bỏ đi là CTA cuộn tới chỗ bị header che.
- Footer là **khối sáng `#f1f1ef`**, không phải navy. Chữ `#254770` (8,39 AAA).
- **Dòng giấy phép KCB `287/BYT-GPHĐ` trong footer là bắt buộc**, chép đúng nguyên văn, không rút gọn.
- Logo Bộ Công Thương + 4 kênh social: giữ đủ — đây là tín hiệu tin cậy.
- Form đặt trong `.reg` nền navy đậm (`#1B4182`), card form trắng nổi lên bằng `--sh-lg`.
- Giữ `:focus-visible` viền amber và khối `prefers-reduced-motion` — đây là phần accessibility của production.

---

## 4. STICKY BAR MOBILE — bắt buộc trên mọi landing
Ba nút: **Gọi | Zalo | Đặt lịch**. Lý do có cả ba, không chỉ một: khách không muốn gọi ở nơi công cộng (→ Zalo), khách nóng muốn gọi ngay (→ Gọi), khách muốn hẹn giờ (→ Đặt lịch). Xem `KF-12` mục 7.
- `max-width:480px`, canh giữa, `z-index` dưới popup và trên nội dung.
- Nút ≥ 44px cao · chừa `env(safe-area-inset-bottom)`.
- Zalo dùng **deep-link thật**, kiểm trên máy thật trước khi giao.

---

## 5. FORM & BOTTOM SHEET — chép mẫu, đừng dựng lại
Trang production đã giải xong bài form mobile:
- `.input` / `.select-btn`: `min-height:50px` · `border:1.5px solid var(--line)` · `border-radius:12px` · **`font:500 16px`** (nhỏ hơn 16px là iOS tự zoom khi chạm) · focus `border-color:var(--ynavy)` + `box-shadow:0 0 0 3px rgba(31,95,196,.18)`.
- Lỗi: `.field.bad` → viền `--err` + nền `--err-t`, kèm `.err` 13px/600 có icon; `aria-describedby` trỏ tới ô lỗi.
- **Chọn dịch vụ = bottom sheet**, không phải `<select>` — mỗi dòng có **dot màu nhóm**. Đây chính là micro-conversion.
- **Honeypot** `input[name=email]` ẩn ngoài màn hình + `aria-hidden` — chống bot, giữ nguyên.
- `aria-live="polite"` cho vùng trạng thái submit, `.spin` trong nút khi đang gửi.
- `.privacy` 12px **ngay dưới nút submit**: *"Thông tin của bạn chỉ dùng để BVTM Kangnam liên hệ xác nhận…"* — đây là trục **riêng tư**, ⛔ không được bỏ, không được đẩy xuống footer.
- **Checkbox đồng ý xử lý dữ liệu cá nhân + popup chính sách: bắt buộc.**
- Màn **cảm ơn** là một `.view` riêng che toàn trang, **không phải `alert()`** — và là một màn CX đủ 5 thành phần (xem §7.5 bộ não).
- **Tối đa 3 trường**: họ tên · SĐT (`inputmode="tel"`) · dịch vụ quan tâm. Tuỳ chọn: khung giờ gọi lại.

---

## 6. TYPOGRAPHY — hai font, không font thứ ba

| Vai trò | Font | Weight |
|---|---|---|
| Toàn bộ body, nút, form, heading chính | **Be Vietnam Pro** (`--f`) | 400 · 500 · 700 · 800 |
| Dòng "pre" của tiêu đề section, câu nhấn cảm xúc (`--f2`) | **Lora** *italic* | 600 |

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;700;800&family=Lora:ital,wght@1,600&display=swap" rel="stylesheet">
```

```css
--f:'Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
--f2:'Lora',Georgia,'Times New Roman',serif;
```

- Body **15px/1.55**; **input bắt buộc 16px**.
- `h1,h2,h3{line-height:1.2}` · `.sec-head .main` 26px/800 · `.sec-head .pre` Lora italic 18px.
- Lora **chỉ** cho dòng pre và câu nhấn — không dùng cho đoạn văn.
- ⛔ **Không nạp font thứ ba.** Cần nhấn thì đổi weight.

---

## 7. LAYOUT & PHONG CÁCH
- Card radius **20px** (`--r-lg`) · input/ô nhỏ **14px** (`--r`) · chip **8px** (`--r-sm`) · button **999px**.
- Shadow chỉ hai cấp: `--sh` cho card, `--sh-lg` cho khối nổi. ⛔ Không chồng shadow.
- `section` padding **44px 0 36px**, nội dung trong `.wrap`.
- Mobile-first, **single-file HTML**, khung thiết kế **360–430px**, container 480px.

**Phong cách:** y khoa cao cấp chuẩn Hàn — sạch, nhiều khoảng trắng, navy làm nền tin cậy, cam chỉ dành cho hành động.
⛔ **Không:** nền tối toàn trang · quá 3 màu chính · gradient/neon mạnh · nhiều style icon lẫn lộn · card nhiều shadow · animation rối. (`shimmer` trên CTA header là ngoại lệ duy nhất đã có trên production.)

> 🔶 Bài audit landing Mũi v3 ghi nhận lỗi **quá tải thông tin**: 4 thẻ công nghệ dàn dọc, danh sách bác sĩ và tình trạng quá dài. Cách xử lý đã được yêu cầu: chuyển sang **tabs / carousel / bộ lọc theo cơ sở**, và tăng khoảng trắng giữa các section. Áp dụng ngay khi một màn có hơn 4 thẻ cùng loại.

---

## 8. Ô ẢNH TẠM — bắt buộc khi chưa có ảnh thật

⛔ **Không bao giờ** chèn ảnh stock, ảnh AI, hay `<img>` trỏ tới URL không tồn tại.

```css
.ph{display:grid;place-content:center;gap:6px;text-align:center;margin:0;padding:16px;
    aspect-ratio:var(--ar,16/9);background:#E8EFFB;border:2px dashed var(--line,#DCE3EC);
    border-radius:var(--r,14px);color:var(--ink-2,#4A5C70);font-size:14px;line-height:1.45}
.ph b{display:block;font-weight:700;color:var(--navy,#074E84)}
```

```html
<figure class="ph" style="--ar:16/9">
  <b>Ảnh 16:9</b>
  Case nâng mũi cấu trúc trước–sau · phục vụ chân dung nhóm 1 · cần văn bản đồng ý KH + pháp chế duyệt
</figure>
```

**Dòng mô tả phải nói rõ ảnh đó LÀ GÌ** — tối thiểu: nội dung · màn/chân dung nó phục vụ · điều kiện pháp lý nếu là case thật. ⛔ Không viết "ảnh minh hoạ".

| Vị trí | `--ar` | Ghi chú |
|---|---|---|
| Hero | `4/5` mobile · `16/9` desktop | Ảnh duy nhất **không lazy-load**, `fetchpriority="high"` |
| Before–after | `1/1` | Cặp 2 ô cạnh nhau hoặc tab/swipe |
| Chân dung bác sĩ | `3/4` | Chỉ bác sĩ trong `KF-01` |
| Công nghệ · thiết bị · phòng mổ · cơ sở | `16/9` | Ảnh thật của hệ thống |
| Case HTLX | `16/9` | Ảnh/clip đã phát sóng, ghi rõ số phát sóng |
| Icon | `1/1` | 48px, **một bộ icon duy nhất** |

**Cuối mỗi landing phải kèm BẢNG KÊ ẢNH CẦN CẤP** — từng ô tạm: màn · tỉ lệ · nội dung cần · ai duyệt. Không có bảng này thì trang **chưa giao xong**.

> ⚠️ Ô ảnh tạm là để **người trong team** đọc. Khi trang lên production, mọi ô tạm và mọi `[CHỜ CẬP NHẬT]` phải **biến mất hoặc khối bị ẩn** — placeholder nội bộ lọt ra trang thật làm mất niềm tin nặng hơn cả thiếu thông tin (`KF-12` mục 7).

---

## 9. PERFORMANCE — ngưỡng giao hàng
- **LCP < 2,5s.** Ảnh WebP nén; hero không lazy; mọi ảnh khác `loading="lazy"`.
- Video `lazy`, ⛔ không autoplay có tiếng.
- Single-file HTML; CSS inline trong `<style>`; JS tối thiểu, không framework.
- Khai `width`/`height` cho mọi `<img>` để không giật layout (CLS).
