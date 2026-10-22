# Agent-LDP-Kangnam

**Agent chuyên làm landing page (LDP) cho hệ sinh thái Kangnam, xuất phát từ hành vi khách hàng.**

Kiêm ba vai: **60% CRO · 25% conversion copywriter · 15% UX/UI designer mobile-first**.
Mỗi landing chỉ có một nhiệm vụ: biến traffic của **một** chiến dịch cụ thể thành **lead chất lượng → booking → show-up**, trong khuôn khổ pháp lý quảng cáo y tế.

**Đo bằng 4 chỉ số, không có chỉ số thứ 5:** CVR (lead/visit) · tỉ lệ lead kết nối được · booking rate · show-up rate.
Không tối ưu cho lượt xem, time-on-page, hay độ "đẹp". Một trang đẹp mà không ai điền form là một trang thất bại.

> **Bắt đầu nhanh:** chưa từng dùng agent nào → [`doc/04-prompt-nguoi-moi.md`](doc/04-prompt-nguoi-moi.md). Muốn cài ngay → [`doc/01-cai-dat.md`](doc/01-cai-dat.md).

## 📘 Hướng dẫn cài đặt

**<https://claude.ai/artifact/JvyWoqxudQFfN5szP2x5ZQ>**

Trang gồm đúng ba mục: **① Cài đặt** — nút tải ZIP, ba bước, 3 tab nền tảng, ba thẻ Copy bộ não và **9 thẻ copy từng file tri thức** · **② 42 prompt mẫu** copy được, 4 nhóm lọc (có nhóm *Hỏi dẫn* cho người chưa có brief) · **③ Kiến thức** — link bản đặc tả gốc, Album Kangnam và các file `knowledge/`.

> Nội dung trong trang lấy thẳng từ repo này nên luôn khớp bản mới nhất. Dựng lại sau khi sửa knowledge: `python tools/build-huong-dan.py` rồi republish cùng URL.

---

## 1. Vì sao agent này tồn tại

Phần lớn landing thẩm mỹ thất bại không vì copy dở, mà vì **viết trước khi hiểu khách**. Triệu chứng quen thuộc:

| Triệu chứng | Nguyên nhân thật |
|---|---|
| CTR quảng cáo tốt, không ai điền form | Màn 1 không nhắc lại lời hứa của ad — khách tưởng bấm sai chỗ |
| Lead nhiều, không ai bắt máy | CTA không nói **ai gọi, khi nào, từ số nào** |
| Bắt máy nhưng không booking | Trang gỡ sai rào cản: khách lo riêng tư mà trang nói về công nghệ |
| Booking nhiều, show-up thấp | Trang hứa khác thứ khách nhận được |

Cả bốn đều là **lỗi hành vi**, không phải lỗi thẩm mỹ. Vì vậy agent bị buộc đi theo một thứ tự cố định: **hành vi trước, chữ sau**.

---

## 2. Luật nền — 7 điều

1. Khách mua **kết quả cảm xúc**, không mua ca phẫu thuật.
2. Ba rào cản quyết định việc điền form: **SỢ** · **NGỜ** · **NGẠI**. Gỡ **đúng** rào cản của **đúng** chân dung, không gỡ chung chung cả ba.
3. **Trục riêng tư** là đặc thù của ngành: mọi landing phải có kênh liên hệ riêng tư song song với form.
4. Trả lời **câu hỏi thật**: *"có đau không"* = *tôi chịu nổi không*; *"bao nhiêu tiền"* = *có đáng không*.
5. Niềm tin xây bằng **bằng chứng**, không bằng tính từ.
6. ⛔ **Không khoét sâu nỗi sợ** trên landing chạy ads — tăng bounce, và quảng cáo dịch vụ KCB không được gây hoang mang.
7. Một màn = một câu hỏi của khách = một ý chính.

Chi tiết: [`knowledge/KF-12-hanh-vi-khach-hang.md`](knowledge/KF-12-hanh-vi-khach-hang.md).

---

## 3. Quy trình 3 tầng — không đảo, không bỏ

```
TẦNG 1 · NGUỒN & ĐỐI TƯỢNG
kênh · ad copy/keyword nguyên văn · tệp · nhiệt độ · mức nhận thức
        ↓ khoá MESSAGE-MATCH
TẦNG 2 · TRẢI NGHIỆM LANDING
9 màn, mỗi màn trả lời đúng 1 câu hỏi trong đầu khách
        ↓
TẦNG 3 · CTA
tin cậy + lý do hành động bây giờ + điều xảy ra sau khi bấm
─────────────────────────────────────────────
XUYÊN SUỐT: mobile-first · cổng pháp lý · tracking → CRM
```

Nhảy thẳng vào copy hay thiết kế mà bỏ Tầng 1 là **lỗi loại thẳng**.

### Chín màn và chín câu hỏi

| Màn | Câu hỏi của khách | Trust tối thiểu |
|---|---|---|
| 1 Hero | "Có đúng thứ mình tìm không?" | 2–3 badge: bác sĩ · cơ sở cấp phép · con số thật |
| 2 Vấn đề | "Họ có hiểu mình không?" | – |
| 3 Giải pháp | "Cách nào? Khác gì nơi khác?" | công nghệ chính danh |
| 4 Người làm | "Ai làm cho mình?" | Dr Trust (R4) |
| 5 Bằng chứng | "Người giống mình ra sao?" | Case Trust (R5) |
| 6 Quy trình & an toàn | "Mình sẽ trải qua những gì?" | Process Trust |
| 7 Giá / Offer | "Bao nhiêu? Có đáng không?" | bảo hành / cam kết quy trình |
| 8 FAQ | "Mình còn lo gì?" | – |
| 9 Chốt | "Giờ làm gì?" | Brand: giấy phép · cơ sở · NAP |

Trang **Nóng/CDP** chỉ dùng 1→4 hoặc 5→7→9. Trang **Lạnh** dùng đủ 9 màn. Bắt khách đã sẵn sàng cuộn 9 màn là cách mất lead dễ nhất.

---

## 4. Cấu trúc thư mục

```
Agent-LDP-Kangnam/
├── SYSTEM-PROMPT.md            bộ não đầy đủ (Claude Project / Gemini)
├── SYSTEM-PROMPT-NGAN.md       bản 7.953 ký tự (ChatGPT Custom GPT, giới hạn 8.000)
├── knowledge/                  ← nạp TOÀN BỘ vào Knowledge của project
│   ├── KF-11-cong-phap-ly.md        cổng pháp lý + rào R0–R12   ★ đọc trước
│   ├── KF-12-hanh-vi-khach-hang.md  hành vi khách               ★ lõi của agent
│   ├── KF-13-noi-so-phan-doi.md     nỗi sợ & phản đối theo BL   ★
│   ├── KF-01-ho-so-thuong-hieu.md   brand · bác sĩ · cơ sở + tuyến
│   ├── KF-14-proof-bank.md          bằng chứng được phép dùng
│   ├── KF-15-block-library.md       24 mã khối landing
│   ├── KF-09-design-system.md       token · khung trang · form
│   └── KF-16-performance-log.md     vòng học (đang trống)
├── goi/GOP-tri-thuc.md         bản gộp 8 file knowledge (101 KB) — đường dự phòng
│                               khi nền tảng chặn số file. Sinh bằng tools/gop-tham-khao.py
├── template/lp-skeleton.html   khung HTML một file, 9 màn, mobile-first
├── tools/                      fetch-du-lieu.py (chụp 5 nguồn live) · build-huong-dan.py (dựng trang
│                               hướng dẫn) · gop-tham-khao.py (sinh lại bản gộp)
├── prompts/                    42 prompt mẫu: wizard · landing · audit · variant
├── doc/                        cài đặt · câu lệnh · output mẫu · người mới · changelog
└── out/                        nơi lưu output, file HTML đã dựng và snapshot dữ liệu
```

**Thứ tự đọc của agent: pháp lý → hành vi → dữ liệu thương hiệu → thiết kế.** Đọc ngược là nguyên nhân của những trang phải làm lại.

> **Chạm trần số file khi upload?** Gemini Gems chỉ cho 10 file. Dùng [`goi/GOP-tri-thuc.md`](goi/GOP-tri-thuc.md) thay cho cả 8 file `knowledge/` — nội dung giống hệt, mỗi phần mở đầu bằng dòng `===== tên file =====` nên mã `KF-xx` vẫn tra được. Đánh đổi: mất khả năng thay riêng một file, phải sinh lại cả bản gộp. Chi tiết ở [`doc/01-cai-dat.md`](doc/01-cai-dat.md).

---

## 5. Tám lệnh

| Lệnh | Việc agent làm |
|---|---|
| `/wizard` | **Hỏi dẫn từ đầu** khi chỉ có tên dịch vụ — 3 vòng × 3 câu, có phương án chọn sẵn |
| `/brief` | Chuẩn hoá brief đã có, hỏi trường thiếu (tối đa 3 câu) |
| `/landing` | Trọn bộ, output 11 mục A→K |
| `/audit [URL]` | Chấm theo scorecard, liệt kê lỗi theo mức, **viết lại phần yếu nhất** |
| `/variant [kênh]` | Chuyển landing master sang kênh khác |
| `/cta` | Siết riêng CTA · form · thank-you page |
| `/ab` | 3 giả thuyết + chỉ số kết luận + thời hạn |
| `/prototype` | Xuất HTML một file + bảng kê ảnh cần cấp |

Chưa có brief, chỉ biết tên dịch vụ → dùng `/wizard`. Chi tiết [`doc/02-cau-lenh.md`](doc/02-cau-lenh.md) · output mẫu đầy đủ [`doc/03-output-mau.md`](doc/03-output-mau.md).

---

## 6. Hai cổng chặn — tính năng, không phải lỗi

### Cổng pháp lý: **fail = không xuất trang**
Agent rà mọi output theo bảng rào **R0–R12** ([`KF-11`](knowledge/KF-11-cong-phap-ly.md)). Bốn điểm chặn hay gặp nhất:

| Rào | Luật |
|---|---|
| **R4** bác sĩ | Chỉ nêu tên có trong `KF-01` **và đúng chuyên môn với dịch vụ của trang** |
| **R3** tuyến cơ sở | **Đại phẫu chỉ tại tuyến bệnh viện** (190 Trường Chinh HN · 666 CMT8 TP.HCM). Viện tỉnh: da · spa · tiểu phẫu + tư vấn + tái khám. Landing local phải ghi rõ *"tư vấn tại [viện tỉnh], phẫu thuật tại [tuyến bệnh viện]"* |
| **R1** cam kết | ⛔ "số 1 / tốt nhất / cam kết 100% / không biến chứng / vĩnh viễn / không đau". Mốc hồi phục luôn dạng **khoảng** + *"tùy cơ địa mỗi người"* |
| **R5 · R12** hình ảnh | Case phải có văn bản đồng ý. ⛔ Before/after cơ thể và ngôn từ miệt thị cân nặng (BL giảm cân) |

**Agent không bịa.** Thiếu giá, tên bác sĩ, case, số liệu → `[CHỜ CẬP NHẬT]` + địa chỉ đi lấy. Nhiều `[CHỜ CẬP NHẬT]` trong output nghĩa là nó đang làm đúng.

### Scorecard: chấm trước khi giao

| Tiêu chí | Điểm |
|---|---|
| Message-match với ad / keyword / tệp | 20 |
| Luồng CX đúng chuỗi câu hỏi và đúng nhiệt độ | 15 |
| Trust đủ mật độ và **đúng thứ tự theo BL** | 20 |
| CTA: đủ 4 câu hỏi · đúng nấc · form ngắn · thank-you | 20 |
| Mobile-first | 15 |
| UI nhất quán `KF-09` | 10 |
| **Cổng pháp lý** | **fail = 0 điểm toàn bài** |

**≥ 80** giao · **65–79** sửa theo danh sách lỗi · **< 65** làm lại từ Tầng 1.

---

## 7. Nguồn dữ liệu — chỉ một nguồn đúng cho mỗi loại

Agent **tra site tại thời điểm chạy**, không lấy từ trí nhớ hay landing cũ:

| Dữ liệu | Nguồn | Có gì (chụp 2026-10-16) |
|---|---|---|
| **Bác sĩ** | [`/doi-ngu-bac-si/`](https://benhvienthammykangnam.com.vn/doi-ngu-bac-si/) | **17 bác sĩ** kèm **CCHN · chuyên khoa · cơ sở · cờ `verified` · số năm · số ca** |
| **Dịch vụ** | menu chính của site | **10 nhóm** dịch vụ |
| **Cơ sở** | [`/chi-nhanh/`](https://benhvienthammykangnam.com.vn/chi-nhanh/) | **7 cơ sở**: 2 bệnh viện + 5 viện thẩm mỹ |
| **Khách hàng thực tế** | [`/case-thuc-te/`](https://benhvienthammykangnam.com.vn/case-thuc-te/) | ⚠️ **đang trống** |
| **Ảnh trước – sau** | [`/hinh-anh-khach-hang/`](https://benhvienthammykangnam.com.vn/hinh-anh-khach-hang/) | **9 nhóm**, đã khai consent + câu miễn trừ |
| Giá · ưu đãi | `/bang-gia/` · `/uu-dai/` | dữ liệu động |

Chụp lại bất cứ lúc nào: `python tools/fetch-du-lieu.py --out out/` — script in ra tổng bác sĩ, **ai thiếu CCHN**, **ai chưa `verified`**, số cơ sở, case còn trống hay không.

**Luật R4 của agent — bác sĩ phải qua cả ba cổng:**
① có trong **danh sách live** *(trang hồ sơ còn sống không đồng nghĩa được dùng — `jolie-huynh`, `bac-si-dr-hong-vu`, `le-thi-thuy` nay đều 404)*
② **đúng chuyên khoa VÀ đúng cơ sở** của landing
③ `status: verified` và **có số CCHN** *(6 người đang trống status, 4 người thiếu CCHN)*

### Còn 13 việc cần người thật chốt
Bốn việc chặn nhiều nhất: ① **nạp case lên `/case-thuc-te/`** (chặn màn 5 của mọi landing) → ② **bảng kê consent nội bộ cho ảnh** → ③ **CCHN cho 4 bác sĩ thiếu + xác nhận 6 người chưa verified** → ④ **chính sách bảo hành bản chi tiết**.
Danh sách đủ, kèm ai chốt: [`doc/CHANGELOG.md`](doc/CHANGELOG.md) mục *Việc còn treo*.

**Hai điểm agent cố ý chưa chọn bên:** bảng màu (production `#074E84/#EF6103` đang dùng vs palette trong spec gốc chưa kiểm tương phản) · mã rào **R12** (có thật theo policy nền tảng, chưa được pháp chế đánh số).

---

## 8. Quan hệ với các agent khác trong repo

| Agent | Khác gì agent này |
|---|---|
| [`Agent-AdsOptimize-Kangnam`](../Agent-AdsOptimize-Kangnam/) | Làm **bộ từ khoá + mẫu quảng cáo**. Agent-LDP-Kangnam nhận đầu ra của nó làm **đầu vào Tầng 1** |
| [`Agent-CRM-Automation`](../Agent-CRM-Automation/) | Làm **luồng tái khai thác + LP cho khách cũ**. Agent-LDP-Kangnam làm LP cho **traffic mới từ chiến dịch** |
| [`Kangnam-Agent-Factory`](../Kangnam-Agent-Factory/) | Làm **kịch bản hội thoại và vận hành**. Agent-LDP-Kangnam dừng ở lúc lead vào CRM |
| [`Agent-KN-CPW`](../Agent-KN-CPW/) | Làm **content SEO/GEO** (khung PAS). Agent-LDP-Kangnam làm trang chạy ads (khung trả lời trước) |

**Ranh giới:** cơ xương khớp / PRP khớp → agent CXK-CPW. Nghiệp vụ nha khoa chuyên sâu → agent nha khoa riêng (Agent-LDP-Kangnam vẫn dựng được LP nha khoa, nhưng phải đổi thứ tự trust theo `KF-13` mục 4).

**Tri thức dùng lại từ repo:** `KF-01` kế thừa `kn-ho-so-thuong-hieu.md` v2.1 · `KF-09` kế thừa `kn-khung-landing.md` v3.0 · `KF-11` kế thừa bảng rào R0–R11 của `geo-rao-phap-ly.md` · `KF-12` kế thừa `K2-khach-hang.md`, `K3-hanh-vi-trang-thai.md`, `kn-chan-dung-hanh-trinh.md`. Sửa dữ liệu ở đầu nguồn thì nhớ đồng bộ sang đây.

---

## 9. Vòng học — bước duy nhất làm agent khá hơn

1. Publish → đo 4 chỉ số.
2. Sau 14 ngày (hoặc đủ 100 lead/nhánh), ghi một dòng vào [`KF-16`](knowledge/KF-16-performance-log.md).
3. Landing sau đọc được dòng đó và ưu tiên pattern đã thắng cho **cùng kênh × cùng BL**.

`KF-16` hiện **đang trống**. Mọi phát biểu kiểu "pattern này thắng" trước khi bảng đó có dữ liệu đều là **giả định**, và agent phải nói rõ là giả định.
"# Agent-LDP-Kangnam" 
