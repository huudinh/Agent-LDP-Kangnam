# KF-01 — HỒ SƠ THƯƠNG HIỆU KANGNAM *(module swappable)*
Version: 1.1 · Cập nhật: **2026-10-16** — đối chiếu trực tiếp với site production
Nguồn gốc: `Agent-AdsOptimize-Kangnam/knowledge/kn-ho-so-thuong-hieu.md` v2.1, **đã sửa theo dữ liệu live**

> Đây là **module thương hiệu**. Đổi sang brand khác = thay file này + `KF-11-cong-phap-ly.md` + `KF-09-design-system.md`, giữ nguyên bộ não.

---

## §0. NGUỒN DỮ LIỆU CHÍNH THỐNG — tra tại thời điểm chạy

**Luật:** năm loại dữ liệu dưới đây **chỉ có một nguồn đúng**. Không lấy từ trí nhớ, không lấy từ landing cũ, không lấy từ file knowledge của agent khác.

| Dữ liệu | Nguồn duy nhất | Dùng cho màn | Rào |
|---|---|---|---|
| **Bác sĩ** | `/doi-ngu-bac-si/` → dữ liệu trong `<script id="kn-doctors-data">` của trang | màn 4 | **R4** |
| **Dịch vụ** | menu chính của `benhvienthammykangnam.com.vn` (mục *Dịch vụ*) | màn 1 · 3 · bottom sheet | **R2** |
| **Cơ sở** | `/chi-nhanh/` | hero local · footer | **R3** |
| **Khách hàng thực tế (case)** | `/case-thuc-te/` | màn 5 | **R5** |
| **Ảnh trước – sau** | `/hinh-anh-khach-hang/` | màn 5 | **R5** · **R12** |
| **Giá** | `/bang-gia/` | màn 7 | — |
| **Ưu đãi** | `/uu-dai/` | màn 7 · hero | — |

**Quy tắc dùng nguồn:**
1. **Tra lại mỗi lần dựng landing.** Dữ liệu dưới đây là bản chụp ngày **2026-10-16**, không phải sự thật vĩnh viễn.
2. Không truy cập được nguồn → ghi `[CHỜ CẬP NHẬT: tra <URL>]`, ⛔ không dùng số cũ.
3. Dữ liệu trên site **mới hơn** file này → tin site, rồi cập nhật file này và ghi một dòng vào `doc/CHANGELOG.md`.
4. Chạy lại bản chụp bằng `tools/fetch-du-lieu.py` (xem `doc/01-cai-dat.md` mục F).

---

## 1. ĐỊNH VỊ & GIỌNG
Hệ thống **Bệnh viện Thẩm mỹ chuẩn Hàn tại Việt Nam**, nền tảng **Y khoa Quốc tế** — 2 bệnh viện + 5 viện thẩm mỹ trải Bắc · Trung · Nam.

**Giọng trên landing:** chuyên nghiệp – y khoa nhưng **ấm**, "chuẩn Hàn", tận tâm. ⛔ Không dùng từ cấm / so sánh tuyệt đối (`KF-11` mục 3).

**Hệ sinh thái:** KPS (Kangnam Plastic Surgery) · KBS (Beauty & Spa) · KDT (Dental) · KWL (Weight Loss) · KWN (Wellness).

**Liên hệ:**
- Hotline chung toàn hệ thống: **0968.999.777** (áp dụng cho mọi cơ sở)
- Email: **benhvienthammy@kangnam.com.vn** *(site /chi-nhanh/ 2026-10-16 — khác với `info@benhvienthammykangnam.com.vn` trong hồ sơ cũ; dùng email trên site)*
- App: **Kangnam Care** · Zalo OA
- Pháp nhân chịu trách nhiệm nội dung: **Công ty TNHH Bệnh viện Thẩm mỹ Kangnam Sài Gòn**

> Hotline campaign có thể khác số tổng đài. ⛔ Không hard-code — dùng biến `{{HOTLINE}}` `{{ZALO_OA}}` `{{BOOKING_URL}}` `{{UTM}}`.

---

## 2. CƠ SỞ & TUYẾN — ràng buộc cứng của landing
> Nguồn: `/chi-nhanh/` · chụp 2026-10-16

**Tổng: 7 cơ sở tại 7 tỉnh thành — 2 bệnh viện thẩm mỹ + 5 viện thẩm mỹ.**

| Cơ sở | **TUYẾN** | Địa chỉ | Khu vực | Mời đại phẫu? |
|---|---|---|---|---|
| **Kangnam Hà Nội** | **Bệnh viện** — GP **194/BYT-GPHĐ** | 190 Trường Chinh, Hà Nội | Bắc | ✅ **CÓ** |
| **Kangnam Sài Gòn** | **Bệnh viện** — GP **287/BYT-GPHĐ** | 666 Cách Mạng Tháng 8, P. Tân Sơn Nhất, TP.HCM | Nam | ✅ **CÓ** |
| Kangnam Hải Phòng | Viện thẩm mỹ | 378 Tô Hiệu, P. Trần Nguyên Hãn, TP. Hải Phòng | Bắc | ❌ không |
| Kangnam Nghệ An | Viện thẩm mỹ | 148 Nguyễn Văn Cừ, TP. Vinh | Trung | ❌ không |
| Kangnam Đà Nẵng | Viện thẩm mỹ | 293 Hùng Vương, P. Thanh Khê, Đà Nẵng | Trung | ❌ không |
| Kangnam Cần Thơ | Viện thẩm mỹ | 28 Lý Tự Trọng, P. Ninh Kiều, TP. Cần Thơ | Nam | ❌ không |
| Kangnam Thanh Hóa | Viện thẩm mỹ | 103 Nguyễn Trãi, P. Hạc Thành, Thanh Hóa | Trung | ❌ không |

> ✅ **Đã chốt (2026-10-16):** trang `/chi-nhanh/` công bố **7 cơ sở**. Các con số từng lưu hành trong repo đều khác: spec KLA ghi *"2 bệnh viện + 7 chi nhánh"* (= 9) · hồ sơ Ads có thêm dòng *"Kangnam Hà Nội (Viện TM) — 194 Trường Chinh"* (= 8) · file brand của CPW/PBP ghi *"3 bệnh viện + 7 viện"* (= 10).
> ⚠️ **Ba địa chỉ sau không có trên `/chi-nhanh/`:** `218 Nguyễn Trãi (SG CS2)` · `194 Trường Chinh` *(các file khác gọi là "Viện Trẻ hoá & Điều trị da công nghệ cao" — có thể là **pháp nhân khác**)* · `chi nhánh Bình Dương`. **Chưa đủ căn cứ nói ba cơ sở này đã đóng.**
> → **Luật: landing chỉ dùng 7 cơ sở ở bảng trên.** Ba địa chỉ kia chỉ dùng sau khi Pháp chế xác nhận còn hoạt động và còn giấy phép — nêu sai pháp nhân là rào **R3**.
> Lưu ý `194` cũng là **số giấy phép của bệnh viện Hà Nội** (bệnh viện ở số **190**), nên dòng cũ dễ gây nhầm.

### ⚠️ LUẬT TUYẾN — kiểm trước khi gắn địa chỉ vào footer

Site tự phát biểu luật này, dùng được nguyên văn làm copy:
> *"Kangnam Hà Nội và Kangnam Sài Gòn [thực hiện được phẫu thuật lớn]. Các viện thẩm mỹ tập trung dịch vụ da, spa, tiểu phẫu trong phạm vi giấy phép, cùng vai trò tư vấn và tái khám."*
> *"Tái khám và chăm sóc hậu phẫu tại chi nhánh Kangnam gần nhà nhất, không bắt buộc quay lại đúng nơi đã phẫu thuật."*

Landing nhắm **đại phẫu + tên tỉnh chỉ có viện thẩm mỹ** là **bẫy**: có người tìm thật, chạy được, nhưng trang **không được mời mổ tại đó**. Hai cách hợp lệ, chọn một và ghi rõ ngay ở hero:
① *"Tư vấn / đặt khám tại [viện thẩm mỹ tỉnh], phẫu thuật tại [tuyến bệnh viện] — tái khám tại chi nhánh gần nhà"*; hoặc
② đưa cụm từ khoá đó vào **phủ định** của chiến dịch local.
Chi tiết: `KF-11` mục 3.1.

> 🔶 Vẫn cần xác minh: **phạm vi giấy phép chi tiết từng viện thẩm mỹ** (làm được đúng những kỹ thuật nào) — `/chi-nhanh/` chỉ nói chung "da, spa, tiểu phẫu".

---

## 3. TRUST / PHÁP LÝ — bằng chứng được phép dùng
- Giấy phép KCB **287/BYT-GPHĐ** (Bộ Y tế, 03/12/2020 — Sài Gòn) và **194/BYT-GPHĐ** (Hà Nội). **Dòng giấy phép ở footer là bắt buộc**, chép đúng nguyên văn, chọn đúng số theo cơ sở của trang.
- Bác sĩ có **chứng chỉ hành nghề (CCHN)** — số CCHN có trong dữ liệu live, xem mục 4.
- **Phòng mổ vô khuẩn và khu hậu phẫu riêng** tại tuyến bệnh viện *(nguyên văn `/chi-nhanh/`)*.
- **Quy trình 5 bước chuẩn y khoa**, **Hội đồng chuyên môn giám sát**.
- **6 quyền lợi:** bác sĩ chuyên khoa trực tiếp khám · gói xét nghiệm tổng quát · trải nghiệm phẫu thuật đẳng cấp · gói chăm sóc hậu phẫu · tái khám định kỳ · **bảo hành minh bạch** *(bảo hành áp dụng tại mọi chi nhánh — `/hinh-anh-khach-hang/`)*.
- Chương trình **Hành Trình Lột Xác (HTLX)** — nguồn case thật, ekip do Dr. Richard Huy phụ trách.

**Thứ tự ưu tiên dùng bằng chứng:** giấy phép Bộ Y tế → CCHN + hiệp hội của bác sĩ → phòng mổ vô khuẩn + quy trình → bảo hành minh bạch → case HTLX.

---

## 4. BÁC SĨ ĐƯỢC PHÉP NÊU TÊN (R4)
> Nguồn: `/doi-ngu-bac-si/`, khối `<script type="application/json" id="kn-doctors-data">` · chụp 2026-10-16 · **16 bác sĩ trong danh sách + 1 bác sĩ giới thiệu riêng**

### 4.1 Danh sách live

| Bác sĩ | CCHN | Chuyên khoa (`specTag`) | Nhóm | Cơ sở | `status` | KN | Số ca |
|---|---|---|---|---|---|---|---|
| **Dr. Richard Huy** (Võ Tiến Huy) | 000303/HNO-CCHN | Chỉnh hình hàm mặt · nâng mũi sụn sườn · nâng ngực · ca khó | — | HN + SG | *(trang riêng)* | 20 năm | — |
| **Dr. Victor Vu** | 000220/QNI-CCHN | HÀM MẶT | ham-mat | HÀ NỘI | ✅ verified | 18 | ~14.250 |
| **Dr. Harvey Nguyen** | 028305/HNO-CCHN | NÂNG MŨI · CẮT MÍ | mui-mat | SÀI GÒN | ✅ verified | 20 | 15.000 |
| **Dr. Jason Nguyen** | 030179/HNO-CCHN | NÂNG MŨI · TIỂU PHẪU | mui-mat | SÀI GÒN | ✅ verified | 10 | >4.000 |
| **Dr. Louis Truong** | 035619/BYT-CCHN | NÂNG MŨI · CẮT MÍ | mui-mat | HÀ NỘI | ✅ verified | 10 | 10.000 |
| **Dr. Nicolas Hung** | — | NÂNG MŨI · CẮT MÍ | khac | HÀ NỘI | ✅ verified | 10 | 3.000 |
| **Dr. Alex Han** | — | HÀM MẶT | khac | HÀ NỘI | ✅ verified | 10 | 9.250 |
| **Dr. Felix Tran** | — | NGỰC · VÓC DÁNG | nguc | SÀI GÒN | ✅ verified | 20 | 10.000 |
| **Dr. Daniel Nguyen** | 032533/HNO-CCHN | CẤY MỠ · KHUÔN MẶT | cay-mo | HÀ NỘI | ✅ verified | 10 | ~8.000 |
| **Dr. Alice Tran** | 039379/HNO-CCHN | DA LIỄU | da | SÀI GÒN | ✅ verified | 5 | >4.000 |
| **Đỗ Minh Vương** | 037801/HNO-CCHN | DA LIỄU | da | HÀ NỘI | ✅ verified | 8 | ~6.000 |
| Dr. Edward Nguyen | 005169/TNG-CCHN | HÀM MẶT | ham-mat | SÀI GÒN | ⚠️ **trống** | 10 | >7.000 |
| Dr. Henry Nguyen | 028062/HNO-CCHN | NÂNG MŨI · CẮT MÍ | mui-mat | HÀ NỘI | ⚠️ **trống** | 12 | >13.000 |
| Dr. Galvin Nguyen | 038579/HNO-CCHN | NGỰC · VÓC DÁNG | nguc | HÀ NỘI | ⚠️ **trống** | 10 | ~14.000 |
| Dr. Lucas Hoang | 009496/HNO-CCHN | NGỰC · VÓC DÁNG | nguc | SÀI GÒN | ⚠️ **trống** | 15 | >20.000 |
| Dr. Mark Nguyen | 036718/HNO-CCHN | CẤY MỠ · KHUÔN MẶT | cay-mo | SÀI GÒN | ⚠️ **trống** | 10 | 15.000 |
| Dr. Frankie Vu | — | NÂNG MŨI · CẮT MÍ | mui-mat | SÀI GÒN | ⚠️ **trống** | 10 | 10.000 |

**Nhóm chuyên khoa trong dữ liệu:** `mui-mat` · `ham-mat` · `nguc` · `cay-mo` · `da` · `khac`.

### 4.2 Ba luật khi gắn bác sĩ vào landing

**① Chỉ dùng bác sĩ có trong danh sách live.** Trang hồ sơ còn tồn tại **không** đồng nghĩa được dùng.
> ⚠️ Hồ sơ cũ từng liệt kê **Dr. Jolie Huynh** — trang `/doi-ngu-bac-si/jolie-huynh/` nay trả **404** và tên này **không còn trong danh sách live**. Đã loại. Hai slug khác cũng 404: `bac-si-dr-hong-vu`, `le-thi-thuy`. ⛔ Không dùng ba tên này.

**② Gắn đúng chuyên khoa VÀ đúng cơ sở.** Landing nâng mũi tại Hà Nội → chọn bác sĩ nhóm `mui-mat` **area HÀ NỘI** (Louis Truong, Henry Nguyen) hoặc `khac` HN (Nicolas Hung). Gắn bác sĩ Sài Gòn vào landing Hà Nội là sai R4 dù tên đúng.

**③ `status: verified` trên site là TÍN HIỆU, KHÔNG phải xác nhận của Pháp chế.**
- **Bác sĩ `status` trống (6 người):** không dùng cho tới khi Chuyên môn/Pháp chế xác nhận.
- **Bác sĩ không có CCHN trong dữ liệu (4 người: Alex Han, Nicolas Hung, Felix Tran, Frankie Vu):** xác minh CCHN trước khi dùng, kể cả khi đang `verified`.

**④ Cổng quyết định là danh sách nội bộ "được duyệt quảng bá" (KF-02 / *"10 bác sĩ"*), KHÔNG phải cờ trên web.**
> ⚠️ **Hai nguồn đang lệch nhau — đây là lý do phải có cổng ④.**
> `Kangnam-Agent-Factory/knowledge/K4-dich-vu.md` (chụp **2026-10-08**) ghi **Dr. Louis Truong *"đã gỡ khỏi danh sách duyệt quảng bá"*** và **Dr. Frankie Vu *"KHÔNG trong danh sách 10 duyệt quảng bá"***. Nhưng dữ liệu live **2026-10-16** lại đánh **Louis Truong là `verified`**.
> → Gặp lệch thì **dừng, hỏi Pháp chế**, không tự chọn bên. Web có thể cập nhật chậm hoặc nhanh hơn danh sách nội bộ, và danh sách nội bộ mới là thứ Pháp chế bảo vệ được.
> 🔶 **KF-02 chưa có trong repo** — mới chỉ được nhắc tới. Lấy được file này là việc mở khoá màn 4 cho toàn hệ thống agent (xem `doc/CHANGELOG.md`).

**Cách chọn an toàn khi chưa có KF-02:** chọn bác sĩ thoả **cả ba**: `verified` trên web · có CCHN · **không bị K4 gắn cờ gỡ/chưa duyệt**. Với landing mũi Hà Nội hiện nay, không ai thoả cả ba → để `[CHỜ CẬP NHẬT]` và hỏi Pháp chế, **không chọn đại một tên trông ổn**.

**④ Số ca và số năm kinh nghiệm** trong bảng là số **trên site**, dùng được, nhưng phải gắn dấu `*` + chú thích *"Hiệu quả phụ thuộc cơ địa mỗi người"*. ⛔ Không làm tròn lên, không đổi "~14.250" thành "hơn 15.000".

**⑤ Trang hồ sơ từng bác sĩ** (`/doi-ngu-bac-si/<slug>/`) có thêm: học hàm/học vị · chức danh · danh sách dịch vụ thực hiện · hiệp hội. Lấy ở đó khi cần viết thẻ bác sĩ đầy đủ.
*Ví dụ Dr. Richard Huy:* Tiến sĩ Y học – ĐH Y Hà Nội · Giám đốc chuyên môn Hệ thống Thẩm mỹ Kangnam · Trưởng ekip *Hành Trình Lột Xác* · thành viên VSAPS, ASPS, ASAPS, AAFPRS, AAOMS, ISAPS, IAOMS.

> ⚠️ Bài audit landing Mũi v3 ghi nhận **ba bác sĩ bị gắn cờ nội bộ** (chưa rõ CCHN / chưa duyệt / mâu thuẫn hồ sơ) từng lọt lên production kèm ghi chú cảnh báo. **Bác sĩ chưa sạch hồ sơ thì ẩn khối, không hiển thị kèm cảnh báo.**

---

## 5. TAXONOMY DỊCH VỤ — đúng menu chính
> Nguồn: menu *Dịch vụ* của `benhvienthammykangnam.com.vn` · chụp 2026-10-16 · **10 nhóm**

| # | Nhóm | Dịch vụ | BL |
|---|---|---|---|
| 1 | **Dịch vụ Mắt** | Tạo mắt 2 mí · Mở khóe mắt · Trẻ hóa mắt · Khắc phục sụp mí | KPS |
| 2 | **Dịch vụ Mũi** | Nâng mũi thẩm mỹ · Thu nhỏ cánh mũi · Mài gồ chỉnh xương mũi · Khắc phục mũi hỏng | KPS |
| 3 | **Hàm Mặt** | Chỉnh hàm hô · Chỉnh hàm móm · Thu gọn góc hàm Vline · Hạ gò má · Tạo má lúm · Tạo hình môi | KPS |
| 4 | **Thẩm mỹ Vòng 1** | Nâng ngực · Treo sa trễ | KPS |
| 5 | **Lipo 360 – Mỡ – Mông** | Giảm mỡ · Tạo hình thành bụng · Cấy mỡ | KPS / KWL |
| 6 | **Trẻ Hóa Da** | Tiêm trẻ hóa · Căng da · Trẻ hóa công nghệ cao · Căng chỉ | KBS |
| 7 | **Da Liễu** | Trị mụn · Trị sẹo | KBS |
| 8 | **Trị Sắc Tố** | Trị nám tàn nhang · Trị bớt sắc tố · Xóa xăm | KBS |
| 9 | **Kangnam Clinic** | Triệt lông · Tắm trắng · Phun xăm · Điêu khắc | KBS |
| 10 | **Nha Khoa** | Niềng răng · Bọc răng sứ · Cấy Implant · Dán mặt sứ | KDT |

> ⚠️ **Khác hồ sơ cũ:** bản cũ gộp "Da liễu & sắc tố" thành một nhóm. Menu thật **tách đôi**: *Da Liễu* (2 dịch vụ) và *Trị Sắc Tố* (3 dịch vụ). Bottom sheet chọn dịch vụ trên form phải theo bảng này.

**Bảng giá gom theo 8 nhóm** (khác taxonomy dịch vụ): Mắt · Mũi · Khuôn mặt · Thẩm mỹ vòng 1 · Lipo 360 – Mỡ & Mông · Trẻ hóa da · Da liễu · Spa.

**Dịch vụ giá trị lớn** (ưu tiên ngân sách landing): nâng ngực · hút mỡ Lipo 360 · chỉnh hàm · nâng mũi cấu trúc.

**Tên dịch vụ dùng đúng như menu.** Tên khách hay gọi (*"gọt hàm V-line"*) chỉ dùng khi **trích lời khách** ở màn 2 hoặc FAQ, không dùng ở phần nêu dịch vụ (R2).

**Menu chính của site** (để map điều hướng và nguồn nội dung): Dịch vụ · Bảng Giá · Ảnh Trước – Sau · Tin tức – Sự kiện · Giới thiệu Kangnam · Hệ sinh thái · Hành trình Lột xác.

---

## 6. ⚠️ GIÁ & KHUYẾN MÃI = DỮ LIỆU ĐỘNG
Lấy **tại thời điểm chạy**: giá `/bang-gia/` · ưu đãi `/uu-dai/`.

**KHÔNG bịa. KHÔNG dùng số cũ.** Không truy cập được → `[CHỜ CẬP NHẬT]` và báo người dùng. Áp cho cả: % ưu đãi · số suất · hạn chương trình · giá trả góp.
Giá không cố định → **bắt buộc ghi "tham khảo"**.

> Site đang chạy cơ chế **"ưu đãi theo từng tháng + mã ưu đãi cá nhân hoá qua Zalo"** (`/hinh-anh-khach-hang/`). Đây là **lý do "tại sao bây giờ" có thật** — dùng được cho CTA, nhưng phải kiểm chương trình của đúng tháng đang chạy. ⛔ Không tự dựng đồng hồ đếm ngược nếu chương trình không có hạn thật.

---

## 7. NHẬN DIỆN & LOGO
**Logo** (giữ safe-area, ⛔ không đổi màu / bóp méo / thêm bóng):
- Header: `https://benhvienthammykangnam.com.vn/wp-content/themes/SCI_Theme_v3/Module/Home/header_kn_3_0_0/images/logo-kbh.png`
- Footer (SVG, nền tối): `https://benhvienthammykangnam.com.vn/wp-content/themes/SCI_Theme_v3/Module/Home/footer_kn_3_1_0/images/logo.svg`
- Hệ sinh thái (cùng thư mục `header_kn_3_0_0/images/`): KPS `logo-kps.png` · KBS `logo-kbs.png` · KDT `logo-kdt.png` · KWN `logo-kwn.png` · KWL `logo-kwl.png`

**Màu & font:** xem `KF-09-design-system.md` — **dựng landing thì dùng token production**, không dùng bảng màu cấp ấn phẩm.

---

## 8. RANH GIỚI VỚI THƯƠNG HIỆU ANH EM
- **Cơ xương khớp / bảo tồn khớp / PRP khớp** thuộc **Cơ Xương Khớp – Wellness**, có agent riêng (CXK-CPW). Báo người dùng chuyển agent, **không viết bằng giọng thẩm mỹ**.
- **Nha khoa (KDT)** thuộc sub-brand **Kangnam Dental**: vẫn trong hệ sinh thái nên **được cross-sell**, nhưng rào cản chốt khác hẳn (NGỜ về vật liệu nặng nhất). Dựng landing nha khoa bằng agent này thì **phải** đổi thứ tự trust theo `KF-13` mục 4. ⚠️ Dữ liệu live hiện **không có bác sĩ nhóm nha khoa** trong `kn-doctors-data` → màn 4 của landing nha khoa phải để `[CHỜ CẬP NHẬT]` hoặc ẩn khối.
