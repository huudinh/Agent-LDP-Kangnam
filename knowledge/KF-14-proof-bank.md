# KF-14 — PROOF BANK (ngân hàng bằng chứng)
Version: 1.1 · Cập nhật: **2026-10-16** — đã nối với nguồn dữ liệu live

> **LUẬT MỘT DÒNG: bằng chứng không truy được về một nguồn trong file này thì không được viết lên landing.**
> Thiếu → ghi `[PLACEHOLDER: cần … từ KF-14]` ở đúng vị trí trên trang **và** liệt kê lại ở mục I của output. ⛔ Tuyệt đối không tự tạo số liệu, case, review, chứng chỉ, báo chí, giải thưởng.

---

## 1. NĂM NGUỒN CHÍNH THỐNG — tra tại thời điểm chạy

| Loại bằng chứng | Nguồn duy nhất | Trạng thái 2026-10-16 |
|---|---|---|
| **Bác sĩ** | `/doi-ngu-bac-si/` → JSON `kn-doctors-data` | ✅ **có dữ liệu đầy đủ**: 16 bác sĩ + Richard Huy, kèm **CCHN · chuyên khoa · cơ sở · cờ `verified` · số năm · số ca** |
| **Dịch vụ** | menu *Dịch vụ* của site | ✅ 10 nhóm — xem `KF-01` mục 5 |
| **Cơ sở** | `/chi-nhanh/` | ✅ **7 cơ sở** (2 bệnh viện + 5 viện thẩm mỹ) — xem `KF-01` mục 2 |
| **Khách hàng thực tế (case)** | `/case-thuc-te/` | ⚠️ **đang trống** — trang báo *"Chưa có ca nào trong nhóm này."* |
| **Ảnh trước – sau** | `/hinh-anh-khach-hang/` | ✅ có ảnh, **9 nhóm dịch vụ**, đã khai có đồng ý khách hàng |
| Giá · ưu đãi | `/bang-gia/` · `/uu-dai/` | dữ liệu **động**, lấy lúc chạy |

**Ký hiệu trạng thái dùng trong file:** ✅ **DUYỆT** (dùng được) · 🔶 **CHỜ DUYỆT** (có tư liệu, chưa duyệt → placeholder) · ⛔ **KHÔNG DÙNG** (vướng rào → ẩn khối) · ❓ **CHƯA CÓ**.

---

## 2. BẰNG CHỨNG CẤP THƯƠNG HIỆU

| # | Bằng chứng | Nội dung | Trạng thái | Rào | Dùng ở màn |
|---|---|---|---|---|---|
| B1 | Giấy phép KCB — Sài Gòn | **287/BYT-GPHĐ**, Bộ Y tế, 03/12/2020 | ✅ DUYỆT | — | **Footer (bắt buộc)** + badge màn 1 |
| B2 | Giấy phép KCB — Hà Nội | **194/BYT-GPHĐ** | ✅ DUYỆT | R3 | Footer landing khu vực Bắc |
| B3 | CCHN của bác sĩ | Số CCHN từng người — có trong dữ liệu live | ✅ DUYỆT *(trừ 4 người thiếu số, xem mục 3)* | R4 | Màn 4 |
| B4 | Cơ sở vật chất | **Phòng mổ vô khuẩn + khu hậu phẫu riêng** tại tuyến bệnh viện *(nguyên văn `/chi-nhanh/`)* | ✅ DUYỆT | — | Màn 6 |
| B5 | Quy trình | **5 bước chuẩn y khoa** · hội đồng chuyên môn giám sát | ✅ DUYỆT | — | Màn 6 |
| B6 | Quyền lợi | **6 quyền lợi** · bảo hành áp dụng **tại mọi chi nhánh** | ✅ DUYỆT | — | Màn 7 |
| B7 | Truyền hình | **Hành Trình Lột Xác** — ekip do Dr. Richard Huy phụ trách | ✅ DUYỆT *(từng case vẫn cần consent)* | R5 | Màn 5 |
| B8 | Số cơ sở hệ thống | **7 cơ sở tại 7 tỉnh thành** | ✅ **ĐÃ CHỐT** 2026-10-16 | — | Footer · màn 1 |
| B9 | Hiệp hội của bác sĩ | VSAPS · ASPS · ASAPS · AAFPRS · AAOMS · ISAPS · IAOMS *(Richard Huy)* | ✅ DUYỆT *(theo từng bác sĩ)* | R4 | Màn 4 |
| B10 | Chính sách bảo hành — bản chi tiết | điều kiện · thời hạn · phạm vi theo nhóm dịch vụ | ❓ CHƯA CÓ | R1 | Màn 7 → `[CHỜ CẬP NHẬT]` |
| B11 | Báo chí | danh sách bài + link | ❓ CHƯA CÓ | — | Màn 1 hoặc 5 |
| B12 | Giải thưởng | danh sách + năm + đơn vị trao | ❓ CHƯA CÓ | R1 | ⛔ Không nêu khi chưa có hồ sơ |

**Thứ tự ưu tiên dùng:** B1/B2 → B3+B9 → B4+B5 → B6 (bảo hành) → B7.

---

## 3. BÁC SĨ — nguồn trust mạnh nhất của BL phẫu thuật
> Danh sách đầy đủ kèm CCHN: **`KF-01` mục 4**. Dưới đây chỉ là luật dùng.

**Năm ô cần đủ trước khi bác sĩ lên landing (R4):**

| Ô | Lấy ở đâu | Trạng thái chung |
|---|---|---|
| Tên + chức danh | JSON live (`name`, `role`) | ✅ đủ 17 người |
| **Chuyên khoa** | JSON live (`specTag`, `group`) | ✅ đủ |
| **Cơ sở hành nghề** | JSON live (`area`) | ✅ đủ — HÀ NỘI / SÀI GÒN |
| **CCHN** | JSON live (`cchn`) | ⚠️ **thiếu 4 người**: Alex Han · Nicolas Hung · Felix Tran · Frankie Vu |
| Ảnh chân dung `3/4` | JSON live (`photoSrc`) | ✅ có URL ảnh thật cho từng người |

**Bốn cổng trước khi gắn tên:**
1. Có trong **danh sách live** không? *(trang hồ sơ còn sống ≠ được dùng — `jolie-huynh`, `bac-si-dr-hong-vu`, `le-thi-thuy` nay đều 404)*
2. **Đúng chuyên khoa + đúng cơ sở** của landing không?
3. `status` có phải **`verified`** không? *(6 người đang để trống)* — và **có CCHN** không? *(4 người đang thiếu)*
4. ★ Có trong **danh sách nội bộ "được duyệt quảng bá" (KF-02)** không? **Đây mới là cổng quyết định.**

> ⚠️ **Cờ `verified` trên web ≠ Pháp chế đã duyệt.** `K4-dich-vu.md` (2026-10-08) ghi **Louis Truong đã bị gỡ khỏi danh sách duyệt quảng bá** và **Frankie Vu không có trong danh sách 10**, trong khi web 2026-10-16 đánh Louis Truong là `verified`. Hai nguồn lệch → **dừng, hỏi Pháp chế**.
> 🔶 **KF-02 chưa có trong repo.** Chừng nào chưa có, màn 4 chỉ an toàn khi bác sĩ thoả **cả ba**: `verified` · có CCHN · **không bị K4 gắn cờ**.

**Số ca & số năm:** dùng đúng con số trên site, gắn `*` + *"Hiệu quả phụ thuộc cơ địa mỗi người"*. ⛔ Không làm tròn lên.

---

## 4. CASE / KHÁCH HÀNG THỰC TẾ
> Nguồn: **`/case-thuc-te/`**

**Cấu trúc trang:** lọc theo **4 nhóm** — Tất cả · Nâng mũi · Nâng ngực · Cấy mỡ *(phần mô tả có nhắc cả chỉnh hình hàm mặt)*. Mỗi case gồm: ảnh trước & sau · **mốc thời gian chụp** (vd sau 7 ngày, sau 1 tháng) · bác sĩ chuyên khoa trực tiếp thực hiện · mô tả tình trạng ban đầu và phương pháp.

> ⚠️ **Trạng thái 2026-10-16: trang đang trống** — hiển thị *"Chưa có ca nào trong nhóm này."*
> → Màn 5 của mọi landing hiện phải dùng `[PLACEHOLDER: case từ /case-thuc-te/]` hoặc chuyển sang ảnh trước–sau ở mục 5. **Đây là mục chặn số 1 của agent lúc này.**

**Điều kiện dùng một case (đủ 4, thiếu một là không dùng):**
1. **Văn bản đồng ý minh thị** (R5): loại dữ liệu · mục đích marketing · kênh · thời hạn · quyền rút lại.
2. Pháp chế đã duyệt hình ảnh.
3. **Khớp phân khúc của khách trên trang** — case đúng người, không phải case đẹp nhất (`KF-12` mục 6).
4. Đã kiểm **policy nền tảng** sẽ chạy (Google / Meta / TikTok hạn chế nhiều định dạng before-after của ngành thẩm mỹ).

**Câu miễn trừ site đang dùng — chép đúng, đừng viết lại:**
> *"Hình ảnh được khách hàng đồng ý chia sẻ và ghi rõ thời điểm chụp. Kết quả thẩm mỹ phụ thuộc cơ địa từng người."*

---

## 5. ẢNH TRƯỚC – SAU
> Nguồn: **`/hinh-anh-khach-hang/`** — menu chính gọi là *Ảnh Trước – Sau*

**Phân loại: 9 nhóm dịch vụ** — Mắt (cắt mí) · Mũi (nâng mũi) · Khuôn mặt (hàm mặt) · Thẩm mỹ vòng 1 · Lipo 360 – Mỡ & Mông · Trẻ hóa da · Da liễu · Spa (Kangnam Clinic) · Nha khoa.

**Trang đã khai sẵn ba điều kiện pháp lý** — dùng lại nguyên văn trên landing:
> *"Tất cả hình ảnh tại đây là ảnh thật của khách hàng đã thực hiện dịch vụ tại Bệnh viện thẩm mỹ Kangnam, đều được sự đồng ý của khách hàng. Kết quả thẩm mỹ phụ thuộc cơ địa từng người."*
> *"Mỗi hình ảnh đều ghi rõ thời điểm chụp (ví dụ sau 1 tháng, sau 2 tháng)."*
> *"Hình ảnh trước - sau mang tính tham khảo … Bác sĩ sẽ tư vấn phương án phù hợp sau khi thăm khám trực tiếp tại cơ sở được Bộ Y tế cấp phép."*

**Luật khi lấy ảnh từ trang này:**
1. Lấy **đúng nhóm dịch vụ** của landing, và trong nhóm đó chọn ảnh **gần chân dung khách nhất** — không chọn ảnh đẹp nhất.
2. **Giữ nguyên mốc thời gian chụp** đi kèm ảnh. Bỏ mốc thời gian là làm sai lệch bằng chứng.
3. Luôn kèm dòng miễn trừ ở trên, đặt ngay dưới cụm ảnh.
4. ⛔ **BL giảm cân / Lipo 360:** không dùng ảnh so sánh **cơ thể** trên landing chạy ads (R12 + policy Meta/Google/TikTok) — dù trang gốc có ảnh. Thay bằng câu chuyện khách hàng (`KF-13` mục 3).
5. Kiểm lại **consent còn hiệu lực** trước mỗi chiến dịch — khách có quyền rút lại.

> 🔶 **Chưa có:** bảng kê ảnh ↔ mã case ↔ ngày consent ↔ hạn consent. Trang public không hiển thị dữ liệu này; cần CSKH/Pháp chế cung cấp bản nội bộ.

---

## 6. REVIEW & FEEDBACK

| Loại | Điều kiện dùng | Trạng thái |
|---|---|---|
| Rating/review trên trang bác sĩ | JSON live có `rating` và `reviews` (vd 4.9 / 1.586) | 🔶 **hỏi Pháp chế trước** — chưa rõ nguồn và cách thu thập; ⛔ chưa dùng trên landing |
| Review có tên + ảnh khách | Consent như case (R5) | ❓ CHƯA CÓ bảng kê |
| Review nền tảng (Google Maps, Fanpage) | Trích + dẫn nguồn, không chọn lọc gây hiểu sai | ❓ CHƯA CÓ |
| Video khách hàng | Consent + duyệt | 🔶 |

⛔ Không viết review mẫu, kể cả có ghi chú "ví dụ".

---

## 7. CÔNG NGHỆ · THIẾT BỊ · VẬT TƯ (R7)
- Chỉ nêu thiết bị / vật tư **cơ sở đang có, đúng tính năng, có số lưu hành**.
- ⛔ Không nêu tên thương mại thuốc · filler · botox. ⛔ Không mượn hình máy của nơi khác.
- ❓ **CHƯA CÓ danh mục thiết bị/vật tư được phép nêu tên** → mọi tên công nghệ phải đối chiếu DMKT (R2) trước khi viết.

> Bài học từ audit landing Mũi v3: con số *"chính xác tới 95%"* gắn cho một công nghệ mà **không có tài liệu lâm sàng** phải bỏ, thay bằng mô tả tính năng trực quan.

---

## 8. SỐ LIỆU — luật dùng
- Mọi con số truy được về B1–B12 hoặc JSON bác sĩ live.
- Gắn `*` + chú thích *"Hiệu quả phụ thuộc cơ địa mỗi người"*.
- ⛔ Không ước lượng, không làm tròn lên, không lấy số năm trước.
- ⚠️ Con số **"hơn 3.000.000 ca thẩm mỹ"** xuất hiện ở trang đội ngũ: **chưa rõ phạm vi tính** (toàn hệ thống? mọi dịch vụ? từ năm nào?) → 🔶 hỏi Pháp chế trước khi đưa lên landing.
- Giá và ưu đãi **không nằm trong file này** — dữ liệu động, lấy `/bang-gia/` và `/uu-dai/`.

---

## 9. 🔶 CÒN THIẾU — ưu tiên từ trên xuống

| # | Việc | Chặn gì |
|---|---|---|
| 1 | ★ **Lấy KF-02 — danh sách bác sĩ "được duyệt quảng bá"** (hiện chỉ được nhắc tới, chưa có file) | **Màn 4 của mọi landing** — và của mọi agent Kangnam khác |
| 2 | **Nạp case lên `/case-thuc-te/`** (trang đang trống) | Màn 5 của **mọi** landing |
| 3 | **Bảng kê ảnh ↔ consent ↔ hạn consent** (bản nội bộ) | Màn 5 — rào R5 |
| 4 | **CCHN cho 4 bác sĩ còn thiếu** + xác nhận 6 bác sĩ `status` trống + **giải quyết lệch Louis Truong / Frankie Vu** | Màn 4 với các bác sĩ đó |
| 5 | **Chính sách bảo hành bản chi tiết** | Màn 7 |
| 6 | **Mốc hồi phục dạng khoảng** theo từng dịch vụ, bác sĩ xác nhận | Màn 6 + FAQ |
| 7 | **Danh mục thiết bị/vật tư** được phép nêu tên + số lưu hành | Màn 3 — rào R7 |
| 8 | Làm rõ phạm vi con số **"3.000.000 ca"** và dữ liệu rating/review | Badge màn 1 |
| 9 | **Bác sĩ nhóm nha khoa** — hiện không có trong dữ liệu live | Màn 4 của landing KDT |

Mỗi lần lấy xong một mục: cập nhật file này, ghi ngày + người duyệt, và ghi một dòng vào `doc/CHANGELOG.md`.
