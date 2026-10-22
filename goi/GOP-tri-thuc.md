# TRI THỨC KF — Agent LDP Kangnam
> File này gộp **8 module tri thức** từ `knowledge/`. Sinh tự động ngày 2026-10-22 bằng `python tools/gop-tham-khao.py`.
> ⛔ **Không sửa file này** — sửa ở bản rời trong thư mục nguồn rồi chạy lại lệnh trên.

**Cách đọc:** mỗi phần bắt đầu bằng dòng `===== tên file =====` và là **một đơn vị tri thức riêng**. Tham chiếu dạng `[[tên-file]]` trong văn bản trỏ tới **phần cùng tên ngay trong file này**, không phải file bên ngoài.

## MỤC LỤC

| # | File | Cỡ |
|---|---|---|
| 1 | `KF-01-ho-so-thuong-hieu.md` | 18.0 KB |
| 2 | `KF-09-design-system.md` | 15.7 KB |
| 3 | `KF-11-cong-phap-ly.md` | 13.0 KB |
| 4 | `KF-12-hanh-vi-khach-hang.md` | 13.2 KB |
| 5 | `KF-13-noi-so-phan-doi.md` | 12.0 KB |
| 6 | `KF-14-proof-bank.md` | 14.3 KB |
| 7 | `KF-15-block-library.md` | 7.7 KB |
| 8 | `KF-16-performance-log.md` | 4.5 KB |


===== KF-01-ho-so-thuong-hieu.md =====

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
| **Ảnh trước – sau** (công khai) | `/hinh-anh-khach-hang/` | màn 5 | **R5** · **R12** |
| **Kho ảnh nội bộ** | **Album Kangnam** — https://hcigroup.vn/app/albumkn/ *(cần đăng nhập)* | màn 5 | **R5** |
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

> ✅ **Đã chốt (2026-10-16):** trang `/chi-nhanh/` công bố **7 cơ sở**. Các con số từng lưu hành trong repo đều khác: spec gốc ghi *"2 bệnh viện + 7 chi nhánh"* (= 9) · hồ sơ Ads có thêm dòng *"Kangnam Hà Nội (Viện TM) — 194 Trường Chinh"* (= 8) · file brand của CPW/PBP ghi *"3 bệnh viện + 7 viện"* (= 10).
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


===== KF-09-design-system.md =====

# KF-09 — DESIGN SYSTEM LANDING KANGNAM v3.0 (chuẩn giao HTML)
Version: 1.0 · Nguồn: `Agent-AdsOptimize-Kangnam/knowledge/kn-khung-landing.md` v3.0 — token lấy **nguyên** từ trang production
Cập nhật: 2026-10-16

**Trang mẫu chuẩn:** `https://benhvienthammykangnam.com.vn/quyen-loi-thanh-vien/dep-ven-tron/` (bản lưu: `Agent-AdsOptimize-Kangnam/template/dep-ven-tron.html`)

> ⚠️ **Font KHÔNG lấy từ trang mẫu nữa** — xem mục 6: landing của agent này dùng **Roboto**, trong khi `dep-ven-tron` chạy Be Vietnam Pro + Lora.
> ⚠️ **Lấy GÌ và KHÔNG lấy gì từ trang mẫu.** Đây là trang quyền lợi thành viên (`noindex`, 3 section).
> ✅ Lấy: token màu · khung trang · header/footer · form + bottom sheet · sticky/shimmer CTA · nhịp trình bày mobile.
> ❌ **Không lấy cấu trúc nội dung** — 3 section của nó không phải khung landing chạy ads. Thứ tự màn lấy từ §6 của bộ não (9 màn).

---

## 1. ⚠️ BA BẢNG MÀU ĐANG TỒN TẠI — DÙNG BẢNG NÀO

| Bảng | Giá trị | Dùng cho |
|---|---|---|
| **Production v3.0** ✅ | navy `#074E84` · CTA `#EF6103` | **Dựng landing — dùng bảng này**, để trang mới khớp trang đang chạy |
| Nhận diện cấp thương hiệu | navy `#003c77` · CTA `#f6871f` | Ấn phẩm cấp brand: profile, brochure, biển hiệu |
| Spec gốc đề xuất 🔶 | `#294573` · accent `#3A6CAE` · teal `#2F8E7E` · gold `#9F7131` · nude `#F6F1ED` · peach `#F9E6D7` | **Chưa dùng.** Bảng này đến từ bản đặc tả gốc, chưa đối chiếu tương phản và chưa khớp production |

**Luật:** landing dùng **token production** ở mục 2. Muốn chuyển sang bảng của spec gốc thì phải chạy lại kiểm tương phản WCAG cho từng cặp màu và **brand + pháp chế chốt một lần** — xem *Việc còn treo* ở [`doc/CHANGELOG.md`](../doc/CHANGELOG.md). ⛔ Không trộn hai bảng trong một trang.

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

> ⚠️ **Hai nhánh landing Kangnam đang dùng hai font khác nhau — đây là lựa chọn, không phải lỗi.**
>
> | | Font | Nguồn production |
> |---|---|---|
> | **Agent này** (`Agent-LDP-Kangnam`) | **Roboto** | `/quyen-loi-thanh-vien/phau-thuat-tham-my-20-10/` |
> | `Agent-CRM-Automation` | **Roboto** | cùng trang 20-10 |
> | `Agent-AdsOptimize-Kangnam` | Be Vietnam Pro + Lora italic | `/quyen-loi-thanh-vien/dep-ven-tron/` |
>
> Trước 2026-10-16 agent này theo `dep-ven-tron` (Be Vietnam Pro + Lora). Nay **đổi sang Roboto** cho khớp nhánh LP ưu đãi và gói CRM. Token màu và khung trang **vẫn giữ theo `dep-ven-tron`** — chỉ font đổi.
> ⛔ **Không trộn:** một trang dùng Roboto thì dùng Roboto cho tất cả, kể cả dòng pre.

## 6. TYPOGRAPHY — một họ Roboto

| Vai trò | Font | Weight |
|---|---|---|
| Toàn bộ body, nút, form, heading chính | **Roboto** (`--f`) | 400 · 500 · 700 · 800 |
| Dòng "pre" của tiêu đề section, câu nhấn cảm xúc (`--f2`) | **Roboto *italic*** | 500 · 600 |

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
```

```css
--f:'Roboto',system-ui,-apple-system,'Segoe UI',Arial,sans-serif;
--f2:'Roboto',system-ui,-apple-system,'Segoe UI',Arial,sans-serif;  /* dùng italic của cùng họ */
```

- Body **15px/1.55**; **input bắt buộc 16px**.
- `h1,h2,h3{line-height:1.2}` · `.sec-head .main` 26px/800 · `.sec-head .pre` **Roboto italic 600** 18px.
- *Italic* **chỉ** dùng cho dòng pre và câu nhấn cảm xúc — không dùng cho đoạn văn.
- ⛔ **Không nạp font thứ hai.** Một họ Roboto, phân cấp bằng **weight và italic** — không thêm serif, không thêm display face.

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


===== KF-11-cong-phap-ly.md =====

# KF-11 — CỔNG PHÁP LÝ LANDING PAGE · BẢNG RÀO R0–R12
Version: 1.0 · Nguồn: `Agent-KN-CPW/knowledge/geo-rao-phap-ly.md` (R0–R11, pháp luật cập nhật đến 7/2026) + `Agent-AdsOptimize-Kangnam/knowledge/kn-rao-phap-ly.md`
Cập nhật: 2026-10-16 · **Tài liệu nội bộ, không thay thế ý kiến Pháp chế.**

> **NGUYÊN TẮC NỀN: KHÔNG CHẮC → DỪNG → HỎI PHÁP CHẾ → RỒI MỚI ĐĂNG.**
> Cổng này **FAIL = KHÔNG XUẤT**. Không có ngoại lệ vì chiến dịch gấp. Một trang vi phạm không chỉ bị từ chối quảng cáo — nó là nội dung quảng cáo dịch vụ khám chữa bệnh sai quy định.

---

## 1. NGUYÊN TẮC NỀN
- Thẩm mỹ là **dịch vụ khám chữa bệnh** → nội dung chịu quản lý của pháp luật quảng cáo y tế VN, **cộng thêm** chính sách hạn chế của Google Ads, Meta và TikTok với ngành làm đẹp/phẫu thuật.
- Mọi phát ngôn y khoa (cơ chế · hiệu quả · chỉ định · an toàn) phải là **lời bác sĩ hoặc chữ đã được bác sĩ duyệt**.
- Mọi con số (số ca · % · tỷ lệ hài lòng · giải thưởng · năm kinh nghiệm) phải có nguồn thật trong `KF-01` / `KF-14`. **Không nguồn → không đăng.**
- Nội dung quảng cáo dịch vụ KCB cần **giấy xác nhận nội dung quảng cáo (GXNNDQC)** trước khi phát hành. Chưa có → gắn ⚠️, **không bật chiến dịch**.

---

## 2. BẢNG RÀO R0–R12

| Mã | Rào | KHÔNG được làm | THAY BẰNG | Người duyệt |
|---|---|---|---|---|
| **R0** | Nội dung kiến thức | Nhồi CTA bán hàng vào bài kiến thức | Giọng giáo dục, CTA mềm, ghi ngày cập nhật + bác sĩ thẩm định | Content lead |
| **R1** | **Cam kết kết quả** | "cam kết đẹp 100%", "vĩnh viễn", "không biến chứng", "bảo hành trọn đời", "đẹp như ý hoặc hoàn tiền" | "chế độ theo dõi và chỉnh sửa theo chính sách", "kết quả tuỳ cơ địa và được bác sĩ đánh giá riêng" | Pháp chế |
| **R2** | Danh mục kỹ thuật (DMKT) | Đăng dịch vụ/kỹ thuật không có trong DMKT của đúng pháp nhân; thổi phồng "công nghệ độc quyền" | Chỉ nêu kỹ thuật có trong DMKT; tên thương mại phải soi chiếu về tên DMKT | Pháp chế + Chuyên môn |
| **R3** | **Đúng pháp nhân / tuyến cơ sở** ★ | Một trang chạy chung nhiều pháp nhân mà không ghi rõ; **mời đại phẫu tại cơ sở không có giấy phép đại phẫu** | Mỗi trang gắn **đúng pháp nhân có giấy phép**; dùng chung thì ghi rõ cơ sở nào thực hiện dịch vụ nào | Pháp chế |
| **R4** | **Bác sĩ** ★ | Gắn bác sĩ vào dịch vụ khi chưa xác minh chuyên khoa; quảng cáo bác sĩ tại cơ sở chưa đăng ký hành nghề | Chỉ dùng bác sĩ **đã xác minh chuyên khoa + đăng ký hành nghề đúng cơ sở** (danh sách ở `KF-01`) | Chuyên môn + HR |
| **R5** | Hình ảnh khách hàng | Dùng ảnh/video khách khi mới có thoả thuận miệng; suy đoán "khách không phản đối"; dùng ngoài phạm vi đã đồng ý | **Văn bản đồng ý minh thị**: loại dữ liệu · mục đích marketing · kênh · thời hạn · quyền rút lại — lưu để xuất trình | CSKH + Pháp chế |
| **R6** | So sánh đối thủ | Nêu tên, so sánh trực tiếp, hạ thấp cơ sở khác; ám chỉ "nơi khác làm hỏng" | Đưa **bộ tiêu chí khách quan** để khách tự đánh giá; với khách sửa hỏng thì **tuyệt đối không phán xét nơi cũ** | Pháp chế |
| **R7** | Trang thiết bị & vật tư | Mượn hình máy nơi khác; thổi phồng công dụng; nêu vật tư cơ sở không thực sự có; **nêu tên thương mại thuốc/filler/botox** | Chỉ nêu thiết bị/vật tư cơ sở đang có, đúng tính năng và số lưu hành | Kho vật tư + Pháp chế |
| **R8** | Khách nước ngoài / Việt kiều | Đăng nội dung tiếp nhận khách nước ngoài khi thiếu bất kỳ điều kiện nào trong 4 | Đủ 4: dịch vụ trong DMKT · cơ sở đủ phạm vi chuyên môn · năng lực ngôn ngữ/phiên dịch được công nhận · văn bản đồng ý song ngữ | Pháp chế |
| **R9** | **GXNNDQC** ★ | Phát hành nội dung quảng cáo dịch vụ KCB chưa xin GXNNDQC | Đến 7/2026 vẫn còn hiệu lực, thẩm quyền đã phân cấp về **SỞ Y TẾ**. Xác minh trực tiếp với Sở trước chiến dịch lớn | Pháp chế (Sở Y tế) |
| **R10** | KOL / người chuyển tải | KOL nói về dịch vụ mà không công khai là quảng cáo | Từ **01/01/2026**: KOL phải xác minh tính trung thực, công khai `#quảng_cáo`, chịu trách nhiệm liên đới — ràng buộc trong hợp đồng | Brand + Pháp chế |
| **R11** | Người nổi tiếng | Nêu tên hoặc dùng hình người nổi tiếng; suy đoán họ đã phẫu thuật | Phân tích xu hướng chung, không cá nhân hoá | Brand + Pháp chế |
| **R12** 🆕 | **Hình ảnh cơ thể & giảm cân** | Before/after cơ thể; ảnh cơ thể phản cảm; ngôn từ miệt thị cân nặng; hứa số kg giảm | Câu chuyện khách hàng thật (có consent) · khoa học của phương pháp · quy trình "dám từ chối" | Brand + Pháp chế |

> 🆕 **R12 là rào BỔ SUNG của gói Landing, chưa có trong bảng R0–R11 gốc.** Nó gom các giới hạn về hình ảnh cơ thể của **policy Meta / Google Ads / TikTok** cho ngành làm đẹp — giới hạn này có thật và đang chặn quảng cáo, nhưng mã R12 **chưa được Pháp chế đánh số chính thức**. Khi Pháp chế cập nhật bảng rào, đồng bộ lại mã này. Xem *Việc còn treo* ở [`doc/CHANGELOG.md`](../doc/CHANGELOG.md).

---

## 3. BẢNG TỪ CẤM → TỪ ĐÚNG (rà toàn bộ copy trước khi xuất)

| Cấm | Thay bằng |
|---|---|
| đẹp tuyệt đối / hoàn hảo 100% | kết quả hài hoà với gương mặt, bác sĩ tư vấn theo từng cơ địa* |
| khỏi 100% / chắc chắn thành công | tỷ lệ cải thiện cao khi thực hiện đúng chỉ định* |
| không biến chứng / an toàn tuyệt đối | quy trình chuẩn y khoa, môi trường vô khuẩn, hội đồng chuyên môn giám sát |
| không đau | giảm đau theo phác đồ, gây tê/gây mê do bác sĩ chỉ định |
| số 1 / tốt nhất / duy nhất / hàng đầu | (bỏ) hoặc nêu USP đo được: giấy phép, chứng chỉ, bảo hành |
| vĩnh viễn / trọn đời | duy trì lâu dài, có chế độ bảo hành minh bạch |
| cam kết kết quả như hình | kết quả tuỳ cơ địa, bác sĩ đánh giá riêng từng trường hợp* |
| rẻ nhất thị trường | chi phí minh bạch, công khai tại bảng giá |
| không để lại sẹo | vị trí đường mổ được chọn để hạn chế sẹo, chăm sóc theo hướng dẫn* |
| **"3 ngày là đi làm được"** và mọi mốc hồi phục **cứng** | mốc hồi phục dạng **khoảng** (vd 7–14 ngày) + **"tùy cơ địa mỗi người"** |
| "chính hãng" gắn cho vật liệu không có hồ sơ | nêu đúng tên vật liệu/thiết bị có trong hồ sơ, hoặc bỏ |

Mọi con số và cam kết mức độ phải gắn dấu `*` dẫn chú thích **"Hiệu quả phụ thuộc cơ địa mỗi người"**.

### 3.1 Hai luật riêng của gói Kangnam
**① KHÔNG hứa thời gian hồi phục cứng.** Hồi phục là trục **NGẠI** thật của ngành ("nghỉ bao lâu mới đi làm được") nên rất dễ hứa quá. Luôn dạng **khoảng** + *"tùy cơ địa mỗi người"*.

**② KHÔNG quảng cáo đại phẫu cho viện tỉnh.** Đại phẫu chỉ tại **tuyến bệnh viện** (xem `KF-01`). Viện tỉnh / viện TM: da · spa · tiểu phẫu + tư vấn + tái khám.
Landing nhắm từ khoá **đại phẫu + tên tỉnh chỉ có viện tỉnh** (vd *"nâng ngực Đà Nẵng"*) phải chọn **một** trong hai và ghi rõ:
① hero nói thẳng *"tư vấn / đặt khám tại [viện tỉnh], phẫu thuật tại [tuyến bệnh viện]"*; hoặc
② đưa cụm từ khoá đó vào **phủ định** của chiến dịch local.
Để mặc không xử lý là **vượt phạm vi giấy phép** — rủi ro pháp lý, không phải chỉ là lead kém.

---

## 4. HÌNH ẢNH / VIDEO TRÊN LANDING
- **Before–after:** chỉ case **thật, đã duyệt, có văn bản đồng ý**, và **xác minh policy nền tảng trước khi chạy** (nhiều định dạng before-after bị Google/Meta hạn chế với ngành thẩm mỹ).
- ⛔ **Không tạo ảnh kết quả giả**; không dùng ảnh stock/AI mô phỏng kết quả rồi trình bày như case thật.
- ⛔ Tránh cận cảnh thao tác phẫu thuật · máu · vết mổ gây sợ (vi phạm policy nền tảng **và** phản tác dụng chuyển đổi).
- Ảnh bác sĩ, cơ sở, thiết bị: **chỉ ảnh thật của hệ thống**.
- Chưa có ảnh thật → **ô ảnh tạm** theo mẫu `KF-09`, mô tả rõ cần ảnh gì và ai duyệt. ⛔ Không `<img>` trỏ tới URL không tồn tại.

---

## 5. KHÔNG ĐƯỢC LÀM (trên landing và trong mọi copy)
- **Không chẩn đoán** tình trạng khách qua ảnh/mô tả, **không kê đơn**, **không báo giá ca cụ thể** — chỉ tư vấn định hướng rồi mời thăm khám.
- **Không nêu tên hạ thấp đối thủ** (R6).
- **Không gắn sai pháp nhân / sai phạm vi giấy phép** (R3).
- **Không nạp** CCCD · hồ sơ bệnh án · ảnh khách chưa có consent lên công cụ công cộng.
- **Không hiển thị lịch sử dịch vụ / tình trạng sức khoẻ của khách trên landing CDP** — link có thể bị người khác xem.
- **Không khoét sâu nỗi sợ** — quảng cáo dịch vụ KCB không được gây hoang mang.

---

## 6. CHECKLIST CỔNG — chạy trước khi xuất bất kỳ output nào

```
☐ R4  Mọi tên bác sĩ có trong KF-01 và đúng chuyên môn với dịch vụ của trang
☐ R3  Dịch vụ của trang khớp tuyến cơ sở ghi ở footer; đại phẫu → tuyến bệnh viện
☐ R3  Landing local có khách tỉnh → đã khai rõ cách xử lý ① hoặc ②
☐ R1  Rà toàn bộ copy qua bảng từ cấm (mục 3); mọi con số có dấu * + chú thích
☐ —   Mốc hồi phục dạng khoảng + "tùy cơ địa mỗi người"
☐ R7  Không tên thương mại thuốc/filler/botox; thiết bị nêu đúng hồ sơ
☐ R5  Mọi ảnh case có consent; chưa có → ô ảnh tạm, không ảnh stock/AI
☐ R12 BL giảm cân: không before/after cơ thể, không ngôn từ miệt thị cân nặng
☐ —   Mọi số liệu, case, review, chứng chỉ, báo chí truy được về KF-14
☐ —   Giá ghi "tham khảo" nếu không phải giá cố định; giá/ưu đãi lấy tại thời điểm chạy
☐ —   Form có checkbox đồng ý xử lý dữ liệu cá nhân + link chính sách
☐ R9  Đã gắn cờ ⚠️ "cần GXNNDQC trước khi phát hành"
☐ —   Danh sách [CHỜ CẬP NHẬT] / [PLACEHOLDER] đã liệt kê đầy đủ ở mục I của output
```

**Một ô không tick = không xuất trang.** Ghi rõ ô nào đang vướng và cần ai xử lý.

---

## 7. QUY TRÌNH DUYỆT — cộng vào deadline, đừng bỏ qua

```
MKT/Chi nhánh soạn
   → tự kiểm checklist rào R0–R12 (mục 6)
   → BS thẩm định chuyên môn
   → Pháp chế duyệt nội dung & hình ảnh
   → (quảng cáo dịch vụ KCB) xin GXNNDQC tại Sở Y tế
   → publish
   → lưu hồ sơ
```

**Hệ quả lập kế hoạch:** mọi landing phải cộng **thời gian duyệt 2 lớp (BS + Pháp chế)** vào hạn chót. Không đặt hạn sản xuất trùng ngày publish.

---

## 8. BA CÂU CẤM TUYỆT ĐỐI — agent tự soát mọi đầu ra
1. Không cam kết **tuyệt đối / 100% / vĩnh viễn / không đau / không rủi ro / không biến chứng / bảo hành trọn đời**.
2. Không **tự tạo** số liệu · review · giá · voucher · chính sách · mức giảm · thông tin bác sĩ (bằng cấp, kinh nghiệm, giải thưởng, số ca).
3. Không **hạ thấp đối thủ**, không xem bệnh viện thẩm mỹ là spa, không lấy giảm giá làm trọng tâm.

---

## 9. 🔶 CẦN XÁC NHẬN TRƯỚC KHI BẬT CHIẾN DỊCH
- Số **GXNNDQC** của từng landing / chiến dịch: `[CHỜ CẬP NHẬT]`
- Danh sách case + ảnh **đã có văn bản đồng ý**: `[CHỜ CẬP NHẬT]` → xem `KF-14`
- **Phạm vi giấy phép chi tiết từng cơ sở** (làm được gì / không làm gì): `[CHỜ CẬP NHẬT]`
- Bản chính thức của **chính sách bảo hành** theo từng nhóm dịch vụ: `[CHỜ CẬP NHẬT]`
- Mã chính thức cho rào **R12**: `[CHỜ PHÁP CHẾ ĐÁNH SỐ]`


===== KF-12-hanh-vi-khach-hang.md =====

# KF-12 — HÀNH VI KHÁCH HÀNG KANGNAM ★ (file lõi của agent)
Version: 1.0 · Nguồn: `Kangnam-Agent-Factory/knowledge/K2-khach-hang.md` + `K3-hanh-vi-trang-thai.md` + `Agent-AdsOptimize-Kangnam/knowledge/kn-chan-dung-hanh-trinh.md`
Cập nhật: 2026-10-16

> **Đây là file được đọc trước khi viết chữ nào.** Mọi màn, mọi câu, mọi nút trên landing phải truy được về một dòng trong file này. Không truy được = đang viết theo cảm tính.

---

## 1. INSIGHT CỐT LÕI — một câu

> *"Tôi muốn thay đổi ngoại hình để tự tin hơn, nhưng chỉ sẵn sàng thực hiện khi thật sự tin tưởng vào bác sĩ, quy trình và kết quả."*

Hai nửa của câu này sinh ra hai nửa của mọi landing:
- **Nửa trước** (muốn tự tin hơn) → màn 1–3: kết quả cảm xúc, nói bằng ngôn ngữ khách.
- **Nửa sau** (chỉ khi tin) → màn 4–7: bằng chứng, đúng thứ tự rào cản.

Đảo thứ tự hai nửa này là lỗi hành vi nghiêm trọng nhất: nói quy trình phẫu thuật cho một người còn chưa thấy mình muốn gì.

**Khách mua kết quả cảm xúc, không mua ca phẫu thuật.** Họ mua: tự tin · trẻ ra · được công nhận · thôi phải né ống kính. Họ **không** mua "nâng mũi cấu trúc sụn sườn".

---

## 2. BA RÀO CẢN CHỐT — SỢ · NGỜ · NGẠI

Cảm xúc đưa khách tới trang. Ba rào cản này quyết định khách có điền form.

| Rào cản | Khách đang nghĩ gì | Bằng chứng gỡ được | Hỏi ngược lại khách |
|---|---|---|---|
| **① SỢ** | Đau không? Biến chứng không? Hỏng thì sao? Gây mê có sao không? | Quy trình chuẩn y khoa · môi trường vô khuẩn · hội đồng chuyên môn giám sát · gói chăm sóc hậu phẫu · xét nghiệm trước mổ | *"Tôi có chịu nổi không?"* |
| **② NGỜ** | Bác sĩ có thật giỏi? Cơ sở có phép? Ảnh này có phải case thật? Có giá ẩn? | Giấy phép KCB của Bộ Y tế · chứng chỉ chuyên môn bác sĩ · bảng giá công khai · bảo hành minh bạch · case có consent | *"Có bị lừa không?"* |
| **③ NGẠI** | Nghỉ bao lâu? **Người nhà có biết không?** Đồng nghiệp nhìn ra không? | Mốc hồi phục dạng **khoảng** · kênh tư vấn kín đáo · tái khám định kỳ · hẹn giờ gọi lại | *"Ai sẽ biết chuyện này?"* |

**Luật gỡ rào cản:**
1. **Gỡ đúng rào cản của chân dung đang nhắm.** Gỡ cả ba cùng lúc = loãng, và vô tình nhắc khách những nỗi lo họ chưa có.
2. **Thứ tự gỡ theo BL** — xem `KF-13` mục 1. Không có thứ tự chung cho mọi dịch vụ.
3. ⛔ **Không khoét sâu.** Gọi tên nỗi lo rồi trả lời ngay. Quảng cáo dịch vụ KCB không được gây hoang mang (`KF-11` R1, R9).

### 2.1 Trục riêng tư — đặc thù của ngành này
Rào cản NGẠI của thẩm mỹ có một trục không tồn tại ở ngành khác: **"không muốn người thân / đồng nghiệp biết"**.

Hệ quả bắt buộc trên mọi landing:
- **Kênh liên hệ riêng tư song song với form**: nút Zalo / Messenger riêng, đặt cạnh form, không nhỏ hơn form.
- Dòng cam kết bảo mật **ngay dưới nút submit**, không nhét xuống footer.
- Tuỳ chọn **khung giờ muốn được gọi lại** — đây không phải UX trang trí, đây là gỡ rào cản NGẠI.
- Trang CDP: ⛔ không hiển thị lịch sử dịch vụ hay tình trạng sức khoẻ — link có thể bị người khác xem.

Thiếu trục này là tự bỏ một phần lead, và phần bỏ mất thường là nhóm chịu chi nhất (nhóm 2 ở mục 3).

---

## 3. SÁU NHÓM KHÁCH — chọn đúng giọng và đúng bằng chứng

| # | Nhóm | Tuổi | Nỗi đau chính | Rào cản nặng nhất | Giọng landing | Bằng chứng ưu tiên |
|---|---|---|---|---|---|---|
| **1** | **Công sở & người tích góp** | 25–45 | Tích góp mới làm được; sợ rủi ro; sợ ảnh hưởng công việc / con | **SỢ** rồi **NGỜ** | Điềm tĩnh, giải thích rõ, không hối | An toàn + bảo hành + mốc hồi phục dạng khoảng |
| **2** | **Doanh nhân / thu nhập cao** | 35–55 | Sợ lộ dấu phẫu thuật; cần riêng tư; ngại bị chèo kéo | **NGẠI** (riêng tư) | Tinh tế, kín đáo, ít chữ, không khuyến mãi ồn | Bác sĩ đầu ngành + kênh riêng tư + đặc quyền |
| **3** | **KOC/KOL trẻ, Gen Z** | 20–30 | Sợ lỗi trend, xấu khi lên hình; sợ hồi phục lâu | **NGẠI** (thời gian) | Cảm hứng, nhanh, trực diện | Case đúng gu + mốc hồi phục + bác sĩ "tay đẹp" |
| **4** | **Sinh viên / mới đi làm** | 18–25 | Thu nhập thấp; sợ mua hớ; sợ đau, sợ sẹo | **NGỜ** (giá) rồi **SỢ** | Nhẹ nhàng, dễ hiểu, không thuật ngữ | Giá minh bạch + trả góp + feedback thật |
| **5** | **Khách sửa lại (đã hỏng nơi khác)** | 28–50, cả nam | Ám ảnh thất bại; cảnh giác cao; kiệt niềm tin | **NGỜ** ở mức cực đoan | Lắng nghe trước, không phán xét nơi cũ (R6) | Bác sĩ chuyên ca khó + case sửa lại + quy trình hội chẩn |
| **6** | **Trung niên trẻ hoá** | 40–55+ | Lão hoá lộ rõ; sợ mặt đơ, mất tự nhiên; sợ rủi ro sức khoẻ | **SỢ** (sức khoẻ) | Trang trọng, y khoa, kín đáo | Năng lực y khoa + xét nghiệm + kết quả tự nhiên |

**Luật dùng:**
- **Một landing = một nhóm.** Trang cố nói với cả 6 nhóm là trang không nói với ai. Nhóm còn lại dùng `/variant`.
- Nhóm 5 **không bao giờ** nhận copy chung — họ đọc kỹ hơn mọi nhóm khác và phát hiện chữ rỗng nhanh nhất.
- ⚠️ Nhóm 4 có thể là **vị thành niên** → không nội dung tự-sexualize, giữ nội dung đúng lứa tuổi, hướng có người giám hộ. Không nạp tuổi / DOB của khách vào công cụ.

---

## 4. NĂM MỨC NHẬN THỨC — quyết định màn 1 nói gì

| Mức | Khách đang ở đâu | Màn 1 phải làm gì | ⛔ Đừng làm |
|---|---|---|---|
| **1** Chưa biết vấn đề | đang lướt, không tìm gì | Gợi vấn đề bằng câu chuyện hoặc quiz | Đừng mời đặt lịch |
| **2** Biết vấn đề | "mũi mình thấp thật" | Cho thấy vấn đề này giải được | Đừng liệt kê kỹ thuật |
| **3** Biết giải pháp | "nâng mũi là cách" | So sánh phương pháp, nói điểm khác biệt | Đừng dạy lại khái niệm |
| **4** So sánh nơi làm ★ | "làm ở đâu thì an toàn" | **Bằng chứng + bác sĩ + giấy phép, ngay lập tức** | Đừng khơi gợi cảm xúc lại từ đầu |
| **5** Sẵn sàng đặt | "giá bao nhiêu, đặt sao" | Giá tham khảo + lịch + nút đặt, hết | Đừng cho đọc 9 màn |

**Mức 4 là nơi tiền được quyết định.** Phần lớn traffic Google Search nằm ở mức 4–5; phần lớn traffic TikTok/FB TOF nằm ở mức 1–2. Dùng một trang cho cả hai là lý do thường gặp nhất của "CTR tốt mà không ai điền form".

---

## 5. SÁU GIAI ĐOẠN PHỄU → LANDING NÀO

| Giai đoạn | Nhiệt | Dấu hiệu intent trong từ khoá | Landing nên dùng |
|---|---|---|---|
| **1 NHẬN BIẾT** | Lạnh | "là gì" · "có nên" · "xu hướng" | Content / quiz — **không chạy landing chốt** |
| **2 TÌM HIỂU** | Ấm | "phương pháp" · "công nghệ" · "ở đâu tốt" · "bao nhiêu tiền" | Landing đủ màn, thiên giáo dục |
| **3 CÂN NHẮC & NỖI SỢ ★** | Ấm→Nóng | "có đau không" · "bao lâu hồi phục" · "có nguy hiểm" · "bác sĩ nào" · "review" · "hỏng" | **Landing trả lời trước**: hero gọi tên nỗi lo → trả lời ngay → bằng chứng |
| **4 THỰC HIỆN** | Nóng | "giá [dịch vụ]" · "ưu đãi" · "đặt lịch" · "trả góp" | Landing ngắn, form booking nổi |
| **5 TRẢI NGHIỆM & HẬU PHẪU** | Khách hiện hữu | "chăm sóc sau" · "kiêng gì" · "sưng bao lâu" | Trang hướng dẫn / CRM — **không chạy landing chốt** |
| **6 GẮN BÓ & MỞ RỘNG** | LTV | "dịch vụ [khác]" · "khách cũ ưu đãi" | Landing CDP cá nhân hoá mềm |

**Giai đoạn 3 là điểm quyết định** — ngân sách và chất lượng nội dung nên dồn vào đây.
**Giai đoạn 1 và 5 không chạy landing chốt** — ép bán ở đây là đốt ngân sách và làm hỏng niềm tin.

### 5.1 Nhận diện giai đoạn từ một từ khoá lạ
1. Có **giá / "ở đâu" / "đặt lịch" / "ưu đãi"** → giai đoạn 4.
2. Có **"có đau không" / "nguy hiểm" / "review" / "hỏng" / "bác sĩ nào"** → giai đoạn 3.
3. Có **"so sánh" / "loại nào tốt" / "công nghệ"** → giai đoạn 2.
4. Có **"là gì" / "có nên"** → giai đoạn 1.
5. Có **"sau khi" / "kiêng" / "chăm sóc"** → giai đoạn 5.
6. Không khớp nhóm nào → **hỏi lại người dùng, không đoán bừa**.

---

## 6. QUY TẮC CÂU HỎI NGẦM — trả lời cái lo thật

| Khách hỏi | Khách thật sự đang hỏi | Câu trả lời đúng trên landing |
|---|---|---|
| "Có đau không?" | *Tôi có chịu nổi không?* | Phác đồ giảm đau do bác sĩ chỉ định + điều gì xảy ra từng ngày |
| "Bao lâu thì đẹp?" | *Khi nào tôi đi làm lại được?* | Mốc hồi phục dạng **khoảng** + "tùy cơ địa" + gợi ý sắp lịch |
| "Bao nhiêu tiền?" | *Có đáng với số tiền đó không?* | Giá tham khảo + **cái gì nằm trong giá** + bảo hành + trả góp |
| "Bác sĩ nào làm?" | *Người này đã làm ca giống tôi chưa?* | Bác sĩ + case **đúng phân khúc của khách**, không phải case đẹp nhất |
| "Có ảnh thật không?" | *Mấy ảnh kia là giả đúng không?* | Case có consent + ghi rõ nguồn + không retouch quá tay |
| "Để em hỏi lại gia đình" | *Tôi cần một thứ để thuyết phục người khác* | Nội dung mang về được: tài liệu, link bác sĩ, lịch hội chẩn có người thân |

Trả lời nghĩa đen là lý do khách đọc xong vẫn thoát: họ được trả lời nhưng không được **gỡ lo**.

---

## 7. HÀNH VI TRÊN TRANG — cái quyết định bố cục

| Hành vi quan sát được | Hệ quả lên landing |
|---|---|
| Khách quyết trong **~3 giây** là trang có đúng thứ mình tìm hay không | Màn 1 phải nhắc lại **nguyên văn** lời hứa của ad; không có hero "đẹp nhưng mơ hồ" |
| Gần như toàn bộ traffic là **mobile**, một tay, đang di chuyển | Thiết kế 375–414px trước; nút ≥ 44px; sticky bar Gọi \| Zalo \| Đặt lịch |
| Khách **cuộn nhanh và dừng ở ảnh mặt người** | Đặt bằng chứng cạnh ảnh thật; không đặt trust quan trọng trong khối chỉ có chữ |
| Khách **so sánh 3–5 cơ sở cùng lúc, nhiều tab** | Trang phải trả lời được "khác gì nơi khác" bằng tiêu chí kiểm chứng được, không bằng tính từ |
| Khách **không muốn gọi điện ở nơi công cộng** | Zalo / chat luôn song song với số điện thoại |
| Khách **không bắt máy số lạ** | CTA phải nói rõ **ai gọi, khi nào, từ số nào** — thiếu là mất lead đã có |
| Khách đọc giá rồi **quay lại đọc bảo hành** | Khối giá và khối bảo hành nên nằm cạnh nhau, không cách nhau 4 màn |
| Khách thấy **placeholder kỹ thuật** trên trang (`chờ KF-01`, "Chưa có giá") | Mất niềm tin ngay, nặng hơn cả thiếu thông tin → thiếu dữ liệu thì **ẩn khối**, không để lộ ghi chú nội bộ |

> Dòng cuối là bài học thật từ bản audit landing Mũi v3 (`HCI-Knowledge/UIUX LANDING PAGE.md`): placeholder nội bộ lọt ra trang production là lỗi vừa làm hỏng trải nghiệm vừa phơi rủi ro pháp lý.

---

## 8. CROSS-SELL THEO HÀNH VI (chỉ ghi nhận, không bán trên landing đang chạy)
- Cắt mí → trẻ hoá da · nâng mũi · điều trị da.
- Nâng mũi → cắt mí · độn cằm · trẻ hoá.
- Điều trị da → tiêm trẻ hoá · căng da · chăm sóc định kỳ.

Landing chỉ có **một nhiệm vụ**. Cross-sell ghi vào ô ⑦ của Audience Card để CRM dùng về sau, **không** thêm một CTA thứ hai lên trang.

---

## 9. NĂM LỖI HÀNH VI HAY GẶP NHẤT
1. **Viết cho người đã tin** trong khi khách đang ở mức nhận thức 4 → thiếu bằng chứng ở đúng chỗ khách do dự.
2. **Gỡ sai rào cản** — khách lo riêng tư mà trang nói về công nghệ.
3. **Trả lời nghĩa đen** — "không đau" (vi phạm R1) thay vì "phác đồ giảm đau, bác sĩ chỉ định".
4. **Dùng một trang cho mọi nhiệt độ** — khách nóng phải cuộn 9 màn mới thấy nút đặt lịch.
5. **Khoét sâu nỗi sợ để tạo động lực** — khách này đã sợ sẵn; khoét thêm làm họ đóng tab, và là rủi ro tuân thủ.


===== KF-13-noi-so-phan-doi.md =====

# KF-13 — NỖI SỢ & PHẢN ĐỐI THEO DỊCH VỤ ★
Version: 1.0 · Cập nhật: 2026-10-16
Dùng cho: màn 2 (Vấn đề) · màn 8 (FAQ) · ô ④ của Audience Card · chọn thứ tự trust màn 3→7.

> **Ba luật khi dùng file này**
> ① Mỗi phản đối phải có **câu trả lời** VÀ **bằng chứng** đi kèm. Nêu nỗi sợ mà không trả lời là khoét sâu → vi phạm `KF-11`.
> ② Câu trả lời mẫu dưới đây đã rà qua bảng từ cấm. **Không viết lại thành câu chắc chắn hơn** ("không đau", "không biến chứng") — đó là R1.
> ③ Bằng chứng cụ thể (số ca, case, ảnh) phải lấy từ `KF-14`. Chưa có → `[PLACEHOLDER: cần … từ KF-14]`.

---

## 1. THỨ TỰ TRUST THEO BL — quyết định bố cục màn 3→7

| BL | Nỗi sợ số 1 | Thứ tự trust bắt buộc | ⛔ Cấm riêng của BL |
|---|---|---|---|
| **PTTM / Hàm mặt** (KPS) | Sai bác sĩ → biến chứng | Bác sĩ → case giống mình → quy trình an toàn (gây mê, hồi sức) → brand | Không hứa mốc hồi phục cứng |
| **Giảm béo / Hút mỡ** (KWL) | Không hiệu quả, nguy hiểm | Khoa học + đội chuyên gia → quy trình **"dám từ chối"** → câu chuyện thật | **Không before/after cơ thể**, không ngôn từ miệt thị cân nặng (R12) |
| **Nha khoa** (KDT) | Đau, hỏng, không bền | Công nghệ + bảo hành → bác sĩ → case nụ cười | Không hứa "dùng vĩnh viễn" |
| **Da / Trẻ hoá** (KBS) | Tiền mất tật mang | Công nghệ chính danh → kết quả thực → bác sĩ (chỉ người đã duyệt) | Không nêu tên thương mại thuốc/filler/botox (R7) |
| **Spa / Wellness** (KWN) | Bị chèo kéo, mất tiền oan | Giá minh bạch → review → không gian, trải nghiệm | Không bán thêm trong landing |

**Thứ tự này không đổi theo sở thích người viết.** Đổi thứ tự = đặt bằng chứng vào chỗ khách chưa cần, và để trống chỗ khách đang do dự.

---

## 2. PTTM / HÀM MẶT — mắt · mũi · hàm mặt · vòng 1 · Lipo 360

| # | Phản đối (lời khách) | Rào cản | Câu trả lời mẫu (đã rà từ cấm) | Bằng chứng cần |
|---|---|---|---|---|
| 1 | "Có đau không?" | SỢ | "Ca mổ thực hiện với phác đồ giảm đau và gây tê/gây mê **do bác sĩ chỉ định** sau khi khám. Sau mổ bạn được hướng dẫn giảm sưng đau theo gói chăm sóc hậu phẫu." | Quy trình chuẩn y khoa · gói hậu phẫu |
| 2 | "Biến chứng thì sao?" | SỢ | "Ca được thực hiện tại tuyến bệnh viện có giấy phép, trong môi trường vô khuẩn, có **hội đồng chuyên môn giám sát** và xét nghiệm tổng quát trước mổ. Mọi tình huống đều có quy trình xử lý và theo dõi." | Số giấy phép KCB · quy trình · hội đồng chuyên môn |
| 3 | "Nghỉ bao lâu mới đi làm được?" | NGẠI | "Thời gian hồi phục thường trong **khoảng [X–Y] ngày**, *tùy cơ địa mỗi người*. Bác sĩ sẽ giúp bạn chọn thời điểm mổ phù hợp với lịch công việc." | Mốc hồi phục theo dịch vụ `[CHỜ CẬP NHẬT từ chuyên môn]` |
| 4 | "Ai sẽ mổ cho tôi? Bác sĩ đó làm ca này nhiều chưa?" | NGỜ | "Bác sĩ chuyên khoa **trực tiếp khám và trực tiếp thực hiện**. Hồ sơ chuyên môn và ca đã thực hiện của bác sĩ được công bố." | Tên bác sĩ đã duyệt (R4) + case cùng dạng |
| 5 | "Ảnh before-after kia là thật không?" | NGỜ | "Case trên trang là khách hàng thật, **đã có văn bản đồng ý sử dụng hình ảnh**. Kết quả từng người khác nhau, *phụ thuộc cơ địa*." | Case có consent (R5) |
| 6 | "Hỏng thì ai chịu?" | NGỜ | "Có chế độ **bảo hành minh bạch** và tái khám định kỳ. Trường hợp cần theo dõi hoặc chỉnh sửa được xử lý theo chính sách đã công bố." | Chính sách bảo hành `[CHỜ CẬP NHẬT bản chính thức]` |
| 7 | "Giá có phát sinh không?" | NGỜ | "Chi phí được báo sau khi khám, nêu rõ **những gì nằm trong giá**: xét nghiệm, ca mổ, thuốc, tái khám. Giá trên trang là giá tham khảo." | Bảng giá công khai (dữ liệu động) |
| 8 | "Người nhà tôi phản đối" | NGẠI | "Bạn có thể đặt **buổi hội chẩn có người thân cùng tham dự**, hoặc nhận tài liệu tư vấn để xem lại cùng gia đình." | Lịch hội chẩn · tài liệu mang về |
| 9 | "Tôi làm ở nơi khác bị hỏng, sửa được không?" | NGỜ (cực đoan) | "Ca sửa lại cần **khám và hội chẩn trước** để đánh giá tình trạng hiện tại; bác sĩ sẽ nói rõ phương án khả thi và cả giới hạn của nó." | Bác sĩ chuyên ca khó + case sửa lại ⛔ **Không phán xét nơi cũ (R6)** |
| 10 | "Tôi ở tỉnh, làm ở chi nhánh gần nhà được không?" | NGẠI | "Bạn **khám và tư vấn tại [viện tỉnh]**, ca phẫu thuật thực hiện tại **[tuyến bệnh viện]**. Tái khám có thể làm tại cơ sở gần nhà." | ⚠️ Bắt buộc nói rõ — R3, xem `KF-11` |

---

## 3. GIẢM BÉO / HÚT MỠ (KWL) — BL có rào pháp lý nặng nhất

| # | Phản đối | Rào cản | Câu trả lời mẫu | Bằng chứng cần |
|---|---|---|---|---|
| 1 | "Có hiệu quả thật không hay mất tiền vô ích?" | NGỜ | "Phác đồ xây sau khi đánh giá chỉ số cơ thể và tình trạng sức khoẻ. Bác sĩ nói rõ mức cải thiện **có thể kỳ vọng** và điều kiện để giữ kết quả." | Cơ sở khoa học của phương pháp · đội chuyên gia |
| 2 | "Hút mỡ có nguy hiểm không?" | SỢ | "Đây là can thiệp y khoa, chỉ thực hiện tại **tuyến bệnh viện có giấy phép**, sau xét nghiệm và đánh giá của bác sĩ. Không phải ai cũng có chỉ định." | Giấy phép · quy trình · xét nghiệm |
| 3 | "Tôi có làm được không?" | SỢ | "Có trường hợp bác sĩ **khuyến nghị không thực hiện** và đề xuất hướng khác an toàn hơn. Buổi khám là để trả lời chính câu hỏi này." | Quy trình **"dám từ chối"** — đây là trust mạnh nhất của BL này |
| 4 | "Giảm rồi có béo lại?" | NGỜ | "Kết quả duy trì lâu dài khi kết hợp chế độ theo hướng dẫn; đội chuyên gia theo dõi theo lịch tái khám." ⛔ không viết "vĩnh viễn" | Lộ trình theo dõi |
| 5 | "Cho tôi xem ảnh trước-sau" | NGỜ | "Chúng tôi chia sẻ **câu chuyện của khách hàng thật** (có đồng ý) thay vì ảnh so sánh cơ thể." | ⛔ **Không before/after cơ thể** — R12 + policy Meta/Google/TikTok |

> **Luật riêng của BL này:** mọi nội dung phải tránh ảnh cơ thể so sánh, ngôn từ miệt thị cân nặng và lời hứa số kg. Vi phạm là bị nền tảng từ chối quảng cáo **và** rủi ro pháp lý. Thay bằng: khoa học → quy trình dám từ chối → câu chuyện thật.

---

## 4. NHA KHOA (KDT)

| # | Phản đối | Rào cản | Câu trả lời mẫu | Bằng chứng cần |
|---|---|---|---|---|
| 1 | "Bọc răng sứ có phải mài nhiều không?" | SỢ | "Mức mài do bác sĩ quyết định sau khi chụp phim và đánh giá men răng; phương án bảo tồn tối đa được ưu tiên." | Quy trình chụp phim · bác sĩ |
| 2 | "Dùng được bao lâu?" | NGỜ | "Độ bền phụ thuộc vật liệu, cơ địa và chế độ chăm sóc; có **chế độ bảo hành theo chính sách công bố**." ⛔ không "vĩnh viễn / trọn đời" | Chính sách bảo hành + tên vật liệu có hồ sơ (R7) |
| 3 | "Niềng răng đau và lâu quá" | NGẠI | "Lộ trình thường tính theo **khoảng [X–Y] tháng** tuỳ mức độ; bác sĩ nêu rõ các mốc và lịch tái khám ngay từ buổi đầu." | Lộ trình `[CHỜ CẬP NHẬT từ chuyên môn]` |
| 4 | "Implant có an toàn với người lớn tuổi?" | SỢ | "Cần khám, chụp phim và đánh giá sức khoẻ toàn thân trước; có trường hợp bác sĩ đề xuất phương án khác." | Quy trình · bác sĩ đúng chuyên khoa (R4) |

> Rào cản chốt của nha khoa khác PTTM: **NGỜ về vật liệu** nặng hơn **SỢ về kết quả thấy bằng mắt**. Vì vậy công nghệ + bảo hành đi trước bác sĩ.

---

## 5. DA / TRẺ HOÁ (KBS)

| # | Phản đối | Rào cản | Câu trả lời mẫu | Bằng chứng cần |
|---|---|---|---|---|
| 1 | "Làm xong mặt có bị đơ không?" | SỢ | "Liều và vị trí do bác sĩ chỉ định theo từng gương mặt, hướng tới kết quả hài hoà với nét tự nhiên của bạn." | Bác sĩ đã duyệt · case cùng độ tuổi |
| 2 | "Thiết bị/thuốc có chính danh không?" | NGỜ | "Chỉ sử dụng thiết bị và vật tư **cơ sở đang có, đúng tính năng và số lưu hành**." ⛔ không nêu tên thương mại thuốc/filler/botox | Hồ sơ thiết bị (R7) |
| 3 | "Bao nhiêu lần mới thấy kết quả?" | NGỜ | "Số liệu trình tuỳ tình trạng da, bác sĩ nêu rõ sau khi soi da; mức cải thiện *phụ thuộc cơ địa*." | Liệu trình `[CHỜ CẬP NHẬT]` |
| 4 | "Giá có bị đội lên không?" | NGỜ | "Giá công khai theo liệu trình, nêu rõ phần nào tính thêm nếu có." | Bảng giá (dữ liệu động) |

---

## 6. SPA / WELLNESS (KWN)

| # | Phản đối | Rào cản | Câu trả lời mẫu |
|---|---|---|---|
| 1 | "Vào rồi bị chèo kéo mua thêm" | NGẠI | "Bạn chọn đúng dịch vụ đã đặt; mọi đề xuất thêm chỉ nêu khi bạn hỏi." |
| 2 | "Giá niêm yết rồi có phụ phí không?" | NGỜ | "Giá công khai theo từng dịch vụ, không phụ phí ngoài bảng giá." |
| 3 | "Có đúng người có chuyên môn làm không?" | NGỜ | "Kỹ thuật viên được đào tạo theo quy trình; các bước có chỉ định y khoa do bác sĩ thực hiện." |

---

## 7. PHẢN ĐỐI CHUNG — áp cho mọi BL, dùng cho màn 8 (FAQ)

| Phản đối | Câu trả lời mẫu |
|---|---|
| "Để tôi tìm hiểu thêm đã" | "Bạn có thể **nhận đánh giá từ bác sĩ trước**, chưa cần quyết định gì. Buổi khám là để bạn có đủ thông tin." |
| "Gọi cho tôi làm gì, tôi chỉ muốn hỏi giá" | "Bạn có thể **hỏi qua Zalo** trước, không cần để lại số điện thoại." |
| "Tôi không bắt máy số lạ" | Nói rõ trên trang: **ai gọi · khi nào · từ đầu số nào**. |
| "Trang này nói gì cũng hay như các nơi khác" | Thay tính từ bằng thứ kiểm chứng được: số giấy phép · tên chứng chỉ · chính sách bảo hành · case đúng phân khúc. |

---

## 8. CHỌN 5–7 CÂU CHO FAQ NHƯ THẾ NÀO
1. Lấy **2 câu** thuộc rào cản nặng nhất của chân dung đang nhắm (`KF-12` mục 3).
2. Lấy **1 câu** về giá, **1 câu** về hồi phục, **1 câu** về bảo hành — ba câu này luôn có mặt.
3. Lấy **1 câu** từ mục 7 (phản đối chung) đúng với nhiệt độ của tệp.
4. Nếu landing có khách tỉnh → **bắt buộc** thêm câu số 10 ở mục 2 (tuyến cơ sở).
5. ⛔ Không xếp FAQ theo thứ tự "dễ trả lời trước". Xếp theo **thứ tự khách lo**.

---

## 9. CẦN BỔ SUNG TỪ CHUYÊN MÔN
Những ô dưới đây đang `[CHỜ CẬP NHẬT]` và **không được tự điền**:
- Mốc hồi phục theo từng dịch vụ (dạng khoảng, có bác sĩ xác nhận).
- Lộ trình/số liệu trình của nha khoa và da liễu.
- Bản chính thức của chính sách bảo hành theo từng nhóm dịch vụ.
- Danh sách trường hợp "bác sĩ khuyến nghị không thực hiện" của KWL — đây là trust mạnh nhất của BL đó, rất đáng lấy cho đủ.


===== KF-14-proof-bank.md =====

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
| **Ảnh trước – sau** (công khai) | `/hinh-anh-khach-hang/` | ✅ có ảnh, **9 nhóm dịch vụ**, đã khai có đồng ý khách hàng |
| **Kho ảnh nội bộ** | **Album Kangnam** — https://hcigroup.vn/app/albumkn/ | ✅ **nguồn ảnh làm việc** — thư viện theo chủ đề + thẻ tag, cần đăng nhập |
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

> ⚠️ **Trạng thái 2026-10-16: trang công khai đang trống** — hiển thị *"Chưa có ca nào trong nhóm này."*
> → **Lấy ảnh case từ kho nội bộ** (mục 5.1) thay vì chờ trang công khai. Trang `/case-thuc-te/` vẫn là nơi case **được publish**, nên ca nào đã lên đó thì ưu tiên dùng — khách tự kiểm chứng được.

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

### 5.1 Kho ảnh nội bộ — **Album Kangnam**
> https://hcigroup.vn/app/albumkn/ · *"Thư Viện Ảnh Theo Chủ Đề"* của HCI Group

**Đây là nguồn ảnh làm việc chính** khi `/case-thuc-te/` chưa có ca. Cấu trúc:

| Trường | Dùng để |
|---|---|
| **Chủ đề / Album** | gom theo dịch vụ hoặc chiến dịch — chọn đúng album của dịch vụ landing |
| **Thẻ tag** | lọc nhanh; dùng để đánh dấu trạng thái pháp lý (xem luật dưới) |
| **Tiêu đề + mô tả ảnh** | ghi mốc thời gian chụp và tình trạng — **chép nguyên vào landing** |
| Ngày tải lên · kích thước · độ phân giải | kiểm ảnh có đủ chất lượng cho hero `4/5` hay case `1/1` |

**Cách dùng với agent:** app **cần đăng nhập**, có phân quyền (Quản trị viên · Biên tập viên · Thành viên) và API riêng cho ứng dụng ngoài — **phải có khoá API do Quản trị viên cấp và API đang bật**. Agent **không tự lấy ảnh được**: người làm landing chọn ảnh trong album, rồi đưa agent **link ảnh + tiêu đề + mô tả + mốc thời gian**. App có chức năng **chia sẻ album / chia sẻ thẻ tag** — dùng link chia sẻ đó để bàn giao cho agent hoặc cho dev.

> ⛔ **Ảnh nằm trong kho nội bộ KHÔNG đồng nghĩa đã có consent.** Kho là chỗ *lưu* ảnh, không phải chỗ *cấp phép*. Rào **R5** vẫn đòi **văn bản đồng ý** của từng khách.
> 🔧 **Đề xuất quy ước tag** để giải quyết luôn việc còn treo số 3: mỗi ảnh case gắn một trong ba tag — `consent-ok` (có văn bản đồng ý, còn hiệu lực) · `consent-cho` (đang xin) · `consent-het-han`. Thêm tag `phap-che-duyet` khi Pháp chế đã duyệt hình. Khi đó bộ lọc tag của app **chính là bảng kê consent**, không cần dựng file riêng.

> 🔶 **Chưa có:** bảng kê ảnh ↔ mã case ↔ ngày consent ↔ hạn consent. Trang public không hiển thị dữ liệu này; hoặc dựng bằng quy ước tag ở trên, hoặc xin CSKH/Pháp chế bản nội bộ.

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
| 2 | **Nạp case lên `/case-thuc-te/`** (trang công khai đang trống — ảnh đã có sẵn trong kho nội bộ) | Màn 5 bản publish |
| 3 | **Đánh dấu consent cho ảnh trong Album Kangnam** (quy ước tag ở mục 5.1) | Màn 5 — rào R5 |
| 4 | **CCHN cho 4 bác sĩ còn thiếu** + xác nhận 6 bác sĩ `status` trống + **giải quyết lệch Louis Truong / Frankie Vu** | Màn 4 với các bác sĩ đó |
| 5 | **Chính sách bảo hành bản chi tiết** | Màn 7 |
| 6 | **Mốc hồi phục dạng khoảng** theo từng dịch vụ, bác sĩ xác nhận | Màn 6 + FAQ |
| 7 | **Danh mục thiết bị/vật tư** được phép nêu tên + số lưu hành | Màn 3 — rào R7 |
| 8 | Làm rõ phạm vi con số **"3.000.000 ca"** và dữ liệu rating/review | Badge màn 1 |
| 9 | **Bác sĩ nhóm nha khoa** — hiện không có trong dữ liệu live | Màn 4 của landing KDT |

Mỗi lần lấy xong một mục: cập nhật file này, ghi ngày + người duyệt, và ghi một dòng vào `doc/CHANGELOG.md`.


===== KF-15-block-library.md =====

# KF-15 — THƯ VIỆN KHỐI LANDING (Landing Block Library)
Version: 1.0 · Cập nhật: 2026-10-16
Dùng cho: mục **D. Bản đồ màn** của output `/landing`, và khi dựng HTML ở `/prototype`.

> **Luật nền:** mỗi khối sinh ra để trả lời **đúng một** câu hỏi của khách. Chọn khối theo **câu hỏi**, không theo "trang kia có khối này nên mình cũng có".
> Khối không trả lời câu hỏi nào trong `KF-12` → **bỏ khối đó**. Đó là cách giữ trang ngắn mà không mất chuyển đổi.

---

## 1. BẢNG KHỐI — 9 màn × khối được phép dùng

| Màn | Câu hỏi của khách | Khối | Mã | Thành phần tối thiểu |
|---|---|---|---|---|
| **1 Hero** | "Có đúng thứ mình tìm không?" | Hero message-match | `B-H1` | Ảnh/`.ph` hero · H1 nhắc nguyên văn lời hứa ad · 1 dòng sub · CTA chính · **2–3 badge trust** |
| 1 | (biến thể Google Search) | Hero trả lời truy vấn | `B-H2` | H1 = câu trả lời trực tiếp (giá tham khảo / địa chỉ / bác sĩ) · CTA gọi |
| 1 | (biến thể giai đoạn 3) | Hero gọi nỗi lo + trả lời ngay | `B-H3` | H1 gọi tên nỗi lo · **ngay dưới là câu trả lời**, không cách màn |
| **2 Vấn đề** | "Họ có hiểu mình không?" | Gọi tên nỗi đau | `B-P1` | 3–4 dòng tình trạng, **viết bằng lời khách** · không liệt kê kỹ thuật |
| 2 | | Quiz / chọn tình trạng | `B-P2` | 3–5 câu, kết quả dẫn vào micro-CTA (dùng cho tệp Lạnh) |
| **3 Giải pháp** | "Cách nào? Khác gì nơi khác?" | Phương pháp & công nghệ | `B-S1` | Tabs hoặc bảng so sánh (⛔ không 4 thẻ dàn dọc) · tên kỹ thuật đúng DMKT (R2/R7) |
| 3 | | Điểm khác biệt kiểm chứng được | `B-S2` | 3 tiêu chí **đo được** (giấy phép · chứng chỉ · bảo hành), ⛔ không tính từ |
| **4 Người làm** | "Ai làm cho mình?" | Thẻ bác sĩ | `B-D1` | Ảnh thật `3/4` · tên + chức danh · **chuyên khoa khớp dịch vụ** · 1 câu triết lý · (R4) |
| 4 | | Bộ lọc bác sĩ theo cơ sở | `B-D2` | Chip `[Tất cả] [HN] [TP.HCM]` — dùng khi > 4 bác sĩ |
| **5 Bằng chứng** | "Người giống mình ra sao?" | Case đúng phân khúc | `B-E1` | 2–3 case **cùng chân dung**, tab/swipe · consent (R5) |
| 5 | | Case HTLX | `B-E2` | Clip/ảnh đã phát sóng + ghi rõ số phát sóng |
| 5 | | Câu chuyện khách hàng (chữ) | `B-E3` | **Dùng thay before/after cho BL giảm cân** (R12) |
| **6 Quy trình** | "Mình sẽ trải qua những gì?" | Quy trình 5 bước | `B-Q1` | 5 bước · vô khuẩn · hội đồng chuyên môn giám sát |
| 6 | | Hậu phẫu & tái khám | `B-Q2` | Mốc hồi phục **dạng khoảng** + *"tùy cơ địa mỗi người"* |
| 6 | | Quy trình "dám từ chối" | `B-Q3` | **Trust mạnh nhất của BL giảm cân** — nêu trường hợp bác sĩ khuyến nghị không làm |
| **7 Giá / Offer** | "Bao nhiêu? Có đáng không?" | Bảng giá tham khảo | `B-C1` | Giá **động** + chữ "tham khảo" · nêu rõ **cái gì nằm trong giá** |
| 7 | | 6 quyền lợi | `B-C2` | 6 ô, **bảo hành minh bạch đặt cạnh giá** (`KF-12` mục 7) |
| 7 | | Trả góp | `B-C3` | Dữ liệu động, ⛔ không tự tính lãi |
| **8 FAQ** | "Mình còn lo gì?" | FAQ xử lý phản đối | `B-F1` | 5–7 câu chọn theo `KF-13` mục 8, **xếp theo thứ tự khách lo** |
| **9 Chốt** | "Giờ làm gì?" | Micro-conversion | `B-M1` | Bottom sheet chọn dịch vụ / chọn ưu đãi / đặt khám miễn phí — **đứng trước form** |
| 9 | | Form booking | `B-R1` | ≤ 3 trường · checkbox dữ liệu cá nhân · `.privacy` dưới nút · nút Zalo song song |
| 9 | | Thank-you view | `B-T1` | 5 thành phần (§7.5 bộ não) — là một màn CX, không phải `alert()` |
| xuyên suốt | — | Sticky bar | `B-X1` | **Gọi \| Zalo \| Đặt lịch**, `max-width:480px` |
| xuyên suốt | — | Footer pháp nhân | `B-X2` | Logo · **dòng giấy phép 287/BYT-GPHĐ nguyên văn** · hotline · hệ thống cơ sở · social · Bộ Công Thương |

---

## 2. BỘ KHỐI THEO NHIỆT ĐỘ — chọn nhanh

| Tệp | Khối dùng | Số màn |
|---|---|---|
| **Lạnh** (FB/TikTok TOF) | `B-H1` → `B-P2` → `B-S1` → `B-D1` → `B-E1` → `B-Q1` → `B-C2` → `B-F1` → `B-M1` → `B-R1` | đủ 9 |
| **Ấm** (FB MOF, Google so sánh) | `B-H1` → `B-P1` → `B-S2` → `B-D1` → `B-E1` → `B-Q1` → `B-C1` → `B-F1` → `B-M1` → `B-R1` | 7–9 |
| **Giai đoạn 3 — từ khoá nỗi sợ** | `B-H3` → **câu trả lời** → `B-Q1`/`B-Q2` → `B-D1` → `B-E1` → `B-C1` → `B-F1` → `B-R1` | 6–7 |
| **Nóng** (BOF retarget, Google brand) | `B-H2` → `B-D1` hoặc `B-E1` → `B-C1` → `B-R1` | 4–5 |
| **CDP / ZNS** | `B-H1` (nhận diện **mềm**) → `B-C2` → `B-R1` | 3–4 |
| **Việt kiều** | `B-H1` → `B-D1` → lịch trình về nước → `B-E1` → `B-R1` (CTA video call) | 5 |

⛔ Tệp Nóng không được nhận bộ 9 màn: bắt khách đã sẵn sàng cuộn 9 màn là cách đánh mất lead dễ nhất.

---

## 3. MAP SANG COMPONENT WORDPRESS

| Mã khối | Component / mẫu production | Trạng thái |
|---|---|---|
| `B-X2` footer | `footer_kn_3_1_0` | ✅ có sẵn |
| `B-R1` form + `B-M1` bottom sheet | `template/dep-ven-tron.html` (`.reg`, `.select-btn`, `.sheet`) | ✅ chép nguyên |
| `B-T1` thank-you | `.view` của trang production | ✅ chép nguyên |
| `B-X1` sticky bar | `.sticky-bar` | ✅ có sẵn, nhớ `max-width:480px` |
| `B-H1`/`B-H2`/`B-H3` hero | — | 🔶 dựng mới theo `KF-09` |
| `B-D1` thẻ bác sĩ | — | 🔶 dựng mới |
| `B-E1` case tab/swipe | — | 🔶 dựng mới |
| `B-S1` tabs công nghệ | — | 🔶 dựng mới (yêu cầu từ audit Mũi v3) |
| Toàn bộ còn lại | — | ❓ **CHƯA CÓ bảng component WP chính thức** → điền khi team dev chốt |

> 🔶 **Việc còn treo:** chưa có bảng ánh xạ chính thức mã khối ↔ component WordPress của theme `SCI_Theme_v3`. Hiện agent dựng single-file HTML theo `KF-09`; dev port sang component sau. Khi có bảng chính thức, cập nhật cột này.

---

## 4. KHỐI BỊ CẤM
| Khối | Vì sao |
|---|---|
| Popup chặn màn đầu | Chặn message-match ngay giây thứ 1 |
| Đồng hồ đếm ngược **tự reset** | Khan hiếm giả — `KF-11` mục 5 |
| "Chỉ còn N suất" không có thật | Khan hiếm giả |
| Before/after **cơ thể** (giảm cân) | R12 + policy nền tảng |
| Khối hiển thị lịch sử dịch vụ của khách (CDP) | Lộ dữ liệu sức khoẻ |
| Khối có **placeholder nội bộ hiển thị ra ngoài** | Mất niềm tin + phơi rủi ro pháp lý → **ẩn khối** thay vì để `[CHỜ CẬP NHẬT]` lên production |
| CTA thứ hai cạnh tranh với CTA chính | Một landing = một nhiệm vụ |
| Video autoplay có tiếng | Khách đang ở nơi công cộng |

---

## 5. LUẬT GHÉP KHỐI
1. **CTA lặp sau mỗi 2–3 màn**, cùng một màu, cùng một hành động chính.
2. **Micro-conversion đứng trước form**, sau khối gỡ nỗi sợ.
3. **Khối giá và khối bảo hành đứng cạnh nhau** — khách đọc giá rồi quay lại tìm bảo hành.
4. **Khối bằng chứng đứng cạnh ảnh mặt người** — khách cuộn nhanh và dừng ở ảnh người.
5. Một màn có hơn **4 thẻ cùng loại** → chuyển sang tabs / carousel / bộ lọc.
6. Mỗi khối trong bản đồ màn phải ghi: **mã khối · câu hỏi nó trả lời · bằng chứng nó dùng (mã từ `KF-14`)**. Thiếu cột bằng chứng là chưa dựng xong bản đồ.


===== KF-16-performance-log.md =====

# KF-16 — PERFORMANCE LOG (vòng học của agent)
Version: 1.0 — **khung trống, chờ dữ liệu thật** · Cập nhật: 2026-10-16

> **Đọc file này TRƯỚC mỗi landing mới.** Có pattern đã thắng cho **cùng kênh + cùng BL** → ưu tiên pattern đó. Không có dữ liệu cho cặp đó → nói rõ với người dùng rằng đây là lần đầu, và trang này là **bản để học**.
>
> Cập nhật file này là việc của người vận hành, không phải của agent. **Agent không được tự điền số vào đây.**

---

## 1. CÁCH DÙNG
1. Trước khi làm: tra bảng mục 3 theo cặp **kênh × BL**.
2. Sau khi chạy: điền một dòng vào mục 3, kèm ngày và link landing.
3. Mỗi sprint: đọc mục 4, rút pattern, ghi vào mục 5.

**Chỉ ghi 4 chỉ số, đúng thứ tự quan trọng:**

| Chỉ số | Định nghĩa | Vì sao đứng ở vị trí này |
|---|---|---|
| **CVR** | lead / visit | Chỉ số của trang |
| **Tỉ lệ kết nối** | lead liên lạc được / lead | Phân biệt lead thật với lead rác — **trang có CVR cao mà kết nối thấp là trang hỏng** |
| **Booking rate** | booking / lead kết nối | Chỉ số của chất lượng thông điệp |
| **Show-up rate** | đến khám / booking | Chỉ số cuối, nói lên trang có hứa đúng thứ khách nhận được hay không |

⛔ Không ghi: lượt xem · time-on-page · scroll depth · like. Chúng không trả lời câu hỏi "trang này có hiệu quả không".

---

## 2. MẪU MỘT DÒNG LOG

```
| 2026-10-20 | FB MOF | Mũi (KPS) | /lp/nang-mui-mof-t10 | H3 trả lời trước | Micro: gửi ảnh | 4,8% | 71% | 38% | 62% | Hero đổi sang góc Bác sĩ thắng góc Case |
```

---

## 3. BẢNG LOG — kênh × BL

| Ngày | Kênh | BL / dịch vụ | Landing | Kiểu hero | Nấc CTA | CVR | Kết nối | Booking | Show-up | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | *chưa có dữ liệu* |

> ❓ **Bảng đang trống.** Mọi đề xuất "pattern đã thắng" trước khi bảng này có dữ liệu đều là **giả định**, phải nói rõ là giả định.

---

## 4. KẾT QUẢ A/B

| Ngày | Landing | Giả thuyết | Biến thể A | Biến thể B | Chỉ số đo | Kết quả | Kết luận |
|---|---|---|---|---|---|---|---|
| | | | | | | | *chưa có dữ liệu* |

**Luật A/B của gói này:**
- Mỗi lần test **một biến** (hero, nấc CTA, thứ tự trust, độ dài trang). Test hai biến cùng lúc thì không biết cái nào thắng.
- Khai trước **ngưỡng kết luận** và **thời hạn đánh giá**, trước khi bật test.
- Chỉ số kết luận là **booking rate**, không phải CVR — một biến thể tăng CVR mà giảm booking là biến thể xấu.

---

## 5. PATTERN ĐÃ RÚT ĐƯỢC

| # | Pattern | Áp cho | Bằng chứng (dòng log nào) | Độ tin |
|---|---|---|---|---|
| | | | | *chưa có* |

**Giả thuyết đang chờ kiểm chứng** — ghi ra đây để không quên, nhưng ⛔ **không dùng như sự thật**:
1. Landing giai đoạn 3 dùng hero `B-H3` (gọi nỗi lo → trả lời ngay) cho CVR tốt hơn hero khát khao. *Cơ sở: luật nền của hệ thống, chưa có số của landing.*
2. Tệp FB có nút Zalo song song form cho tỉ lệ kết nối cao hơn trang chỉ có form. *Cơ sở: FB inbox là kênh lead chính + trục riêng tư.*
3. Nhóm khách 2 (doanh nhân) phản hồi tốt hơn với trang ít chữ, không khuyến mãi ồn. *Cơ sở: chân dung `KF-12`.*
4. Nêu rõ **ai gọi, khi nào, từ số nào** làm tăng tỉ lệ kết nối. *Cơ sở: hành vi không bắt máy số lạ.*

Mỗi giả thuyết ở trên nên được biến thành **một test** ở mục 4. Khi có kết quả: chuyển lên mục 5 kèm số, hoặc gạch bỏ.

---

## 6. LANDING ĐÃ AUDIT (`/audit`)

| Ngày | Landing | Điểm scorecard | Lỗi nặng nhất | Đã sửa? |
|---|---|---|---|---|
| — | LP Mũi v3 (`HCI-Knowledge/UIUX LANDING PAGE.md`) | *chưa chấm bằng scorecard này* | Placeholder nội bộ lọt production · bác sĩ chưa duyệt hồ sơ · số liệu "95%" không nguồn · quá tải thông tin | 🔶 theo bản yêu cầu chỉnh sửa |

> Dòng trên là bản audit do người thật viết, trước khi có agent này. Đáng chạy lại bằng `/audit` để có điểm theo scorecard và so sánh được với các landing sau.

