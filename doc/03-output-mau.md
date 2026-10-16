# 03 — OUTPUT MẪU của `/landing`

Ví dụ dưới đây là **mẫu định dạng**, không phải nội dung đã được duyệt. Mọi ô `[CHỜ CẬP NHẬT]` trong đây là **cố ý** — nó cho thấy agent đang làm đúng: thiếu dữ liệu thì để trống kèm địa chỉ đi lấy, không bịa.

---

## Brief đầu vào

```
/landing
1* Kênh: Google Search — nhóm từ khoá giá
2* Keyword nguyên văn: "nâng mũi cấu trúc giá bao nhiêu"
3* Dịch vụ & BL: Nâng mũi cấu trúc — KPS
4* Đối tượng: nữ 25–38, công sở, Hà Nội
5* Nhiệt độ: Nóng (giai đoạn 4)
6  Offer: khám + hội chẩn miễn phí với bác sĩ chuyên khoa
7* CTA mục tiêu: Đặt lịch khám
8* Cơ sở: 190 Trường Chinh, Hà Nội — tuyến bệnh viện
9  KPI: CVR ≥ 4%, booking rate ≥ 35%
```

---

# A. GIẢ ĐỊNH

- Khách tìm trên **mobile, trong giờ làm việc** → ưu tiên nút gọi và Zalo ngang với form.
- Offer "khám + hội chẩn miễn phí" là **chương trình thường trực**, không phải ưu đãi có hạn → ⛔ không dùng khan hiếm.
- Chưa có số CVR của cặp **Google Search × Mũi** trong `KF-16` → đây là **bản để học**, không phải bản tối ưu theo dữ liệu.

# B. AUDIENCE CARD

| Ô | Nội dung |
|---|---|
| ① Họ là ai | Nhân viên công sở nữ 25–38 tại Hà Nội, đã tích góp đủ và đang chốt nơi làm — **nhóm 1 (công sở & người tích góp)**, `KF-12` mục 3 |
| ② Họ vừa thấy gì | Kết quả Google cho truy vấn **"nâng mũi cấu trúc giá bao nhiêu"** |
| ③ Nỗi đau / mong muốn | *"Mũi mình thấp, chụp ảnh góc nghiêng là né. Muốn cao tự nhiên, đừng ai nhìn ra là đã làm."* |
| ④ Nỗi sợ số 1 | *"Bỏ cả khoản tiền tích góp rồi hỏng thì sao?"* → rào cản **NGỜ**, bám sát bởi **SỢ** (`KF-13` mục 2, phản đối #6 và #2) |
| ⑤ Mức nhận thức | **5 — sẵn sàng đặt** (truy vấn đã khai giá) |
| ⑥ Câu hỏi đầu tiên khi mở trang | *"Bao nhiêu tiền, và giá đó gồm những gì?"* |
| ⑦ Tầng hệ sinh thái | KPS (mũi) → tầng tiếp theo: cắt mí · trẻ hoá da (ghi cho CRM, **không bán trên trang này**) |

> Mức nhận thức 5 + nhiệt Nóng → **landing ngắn**. Bắt khách này cuộn 9 màn là cách mất lead dễ nhất.

# C. MESSAGE-MATCH LOCK

| Yếu tố của truy vấn | Phải xuất hiện ở màn 1 |
|---|---|
| ① Từ khoá | cụm **"nâng mũi cấu trúc"** + chữ **"chi phí"** nguyên dạng khách tìm |
| ② Hình ảnh / nhân vật | ảnh bác sĩ đang hội chẩn (không phải ảnh mẫu Hàn Quốc chung chung) |
| ③ Offer | **khám + hội chẩn miễn phí với bác sĩ chuyên khoa** |

# D. BẢN ĐỒ MÀN (bản ngắn — 5 màn)

| Màn | Câu hỏi của khách | Khối (`KF-15`) | Trust dùng (`KF-14`) | CTA |
|---|---|---|---|---|
| 1 Hero | "Bao nhiêu tiền?" | `B-H2` hero trả lời truy vấn | B1 giấy phép · B3 KCCS | Macro: Đặt khám · phụ: Gọi |
| 2 Giá & gồm gì | "Giá đó gồm những gì?" | `B-C1` + `B-C2` 6 quyền lợi | B5 · B8 `[CHỜ CẬP NHẬT bảo hành]` | Macro |
| 3 Bác sĩ | "Ai làm cho tôi?" | `B-D1` thẻ bác sĩ | B3 · R4 | – |
| 4 Bằng chứng | "Người giống tôi ra sao?" | `B-E1` case cùng phân khúc | `[PLACEHOLDER: case có consent]` | Macro |
| 5 Chốt | "Giờ làm gì?" | `B-M1` + `B-R1` + `B-T1` | B1 footer | Form + Zalo |
| xuyên suốt | – | `B-X1` sticky Gọi\|Zalo\|Đặt lịch · `B-X2` footer | B1 | – |

**Lý do bỏ màn 2 (vấn đề), 3 (giải pháp), 6 (quy trình), 8 (FAQ dài):** khách mức 5 không cần được thuyết phục rằng họ có vấn đề. Nỗi lo còn lại của họ nằm ở **giá gồm gì** và **ai làm** — hai thứ đó được đẩy lên trước. FAQ rút còn 3 câu gắn vào màn 2 và 4.

# E. COPY TỪNG MÀN

### Màn 1 — Hero (3 phương án headline)

| Góc | Headline | Dùng khi |
|---|---|---|
| **Bác sĩ** | "Nâng mũi cấu trúc: chi phí và phương án do bác sĩ chuyên khoa tư vấn trực tiếp" | mặc định cho nhóm 1 |
| **Case** | "Nâng mũi cấu trúc — xem chi phí theo từng dáng mũi thực tế" | khi đã có case đủ consent |
| **Nỗi sợ được trả lời** | "Chi phí nâng mũi cấu trúc gồm những gì — và được bảo hành thế nào" | khi muốn đánh thẳng rào cản NGỜ |

**Sub:** Khám và hội chẩn miễn phí tại Bệnh viện Thẩm mỹ Kangnam, 190 Trường Chinh, Hà Nội.
**Badge:** `Giấy phép KCB 194/BYT-GPHĐ – Bộ Y tế` · `Bác sĩ chuyên khoa trực tiếp thực hiện` · `[CHỜ KF-02: số năm/số ca của bác sĩ được duyệt]*` *(khi có tên duyệt thì chép đúng số trên site — ⛔ không làm tròn lên)*
**CTA:** `ĐẶT KHÁM MIỄN PHÍ VỚI BÁC SĨ` · phụ: `Gọi [HOTLINE]`
**Dưới nút:** *Miễn phí · Không ràng buộc · Thông tin được bảo mật*

### Màn 2 — Giá & gồm gì
> **Chi phí nâng mũi cấu trúc** — `[GIÁ ĐỘNG từ /bang-gia/]`, **giá tham khảo**; mức chính xác do bác sĩ báo sau khi khám.
> **Trong chi phí có:** gói xét nghiệm tổng quát · ca mổ do bác sĩ chuyên khoa trực tiếp thực hiện · gói chăm sóc hậu phẫu · tái khám định kỳ · **bảo hành minh bạch** `[CHỜ CẬP NHẬT: bản chính thức chính sách bảo hành]`.
> *Hiệu quả phụ thuộc cơ địa mỗi người.*

**FAQ gắn vào màn này (2 câu):** "Giá có phát sinh không?" · "Có trả góp không?" `[GIÁ ĐỘNG]`

### Màn 3 — Bác sĩ

**Chạy 4 cổng R4** (`KF-01` mục 4.2) — trang này là *nâng mũi · tuyến bệnh viện Hà Nội*:

| Ứng viên | ① trong danh sách live | ② đúng chuyên khoa + cơ sở | ③ verified + CCHN | ④ trong KF-02 (duyệt quảng bá) | Kết luận |
|---|---|---|---|---|---|
| Dr. Louis Truong | ✅ | ✅ `mui-mat` · HÀ NỘI | ✅ verified · 035619/BYT-CCHN | ⛔ **K4 ghi "đã gỡ khỏi danh sách duyệt quảng bá"** | ⚠️ **lệch nguồn — dừng, hỏi Pháp chế** |
| Dr. Nicolas Hung | ✅ | ✅ nâng mũi · HÀ NỘI | ⚠️ verified nhưng **không có CCHN** | ❓ chưa rõ | chờ xác minh CCHN |
| Dr. Henry Nguyen | ✅ | ✅ `mui-mat` · HÀ NỘI | ⚠️ **status trống** | ❓ chưa rõ | chờ Pháp chế |
| Dr. Harvey Nguyen | ✅ | ❌ `mui-mat` nhưng **SÀI GÒN** | ✅ | — | ⛔ loại — sai cơ sở |

**Kết luận: không ứng viên nào qua đủ 4 cổng** → khối bác sĩ để `[CHỜ CẬP NHẬT: chờ KF-02 xác nhận bác sĩ mũi tại Hà Nội]` và **ẩn khối trên bản publish**, kèm câu hỏi gửi Pháp chế.

Khuôn copy khi đã có tên duyệt:
> **[Chức danh + Tên]** — BVTM Kangnam Hà Nội · [X] năm kinh nghiệm · [Y] ca*
> *"Một dáng mũi đẹp là dáng hài hoà nhất với các đường nét tự nhiên trên khuôn mặt bạn."*
> *Hiệu quả phụ thuộc cơ địa mỗi người.*
Ảnh chân dung `3/4` lấy `photoSrc` trong dữ liệu live; chức danh + hiệp hội lấy ở trang hồ sơ riêng của bác sĩ.

**Hai bài học từ bảng trên:**
- Dr. Harvey Nguyen có 20 năm và 15.000 ca — con số đẹp nhất bảng. Vẫn **loại**, vì ông ở Sài Gòn còn trang này mời khám Hà Nội. Chọn theo con số đẹp là cách vi phạm R4 phổ biến nhất.
- Dr. Louis Truong **qua cả ba cổng kỹ thuật** nhưng vướng cổng ④. **Cờ `verified` trên web không phải là xác nhận của Pháp chế** — đây chính là lý do cổng ④ tồn tại.

### Màn 4 — Bằng chứng
> `/case-thuc-te/` **đang trống** (`KF-14` mục 4) → lấy ảnh từ **`/hinh-anh-khach-hang/` nhóm Mũi**, chọn 2–3 ảnh gần chân dung nữ 25–38 nhất, **giữ nguyên mốc thời gian chụp** đi kèm.
> `[PLACEHOLDER: 2–3 ảnh trước–sau nhóm Mũi + xác nhận consent còn hiệu lực — KF-14 mục 5]`
> Chú thích bắt buộc, chép đúng câu site đang dùng: *"Hình ảnh là của khách hàng thật đã thực hiện dịch vụ tại Bệnh viện thẩm mỹ Kangnam, được sử dụng khi có sự đồng ý và ghi rõ thời điểm chụp. Kết quả thẩm mỹ phụ thuộc cơ địa từng người."*

### Màn 5 — Chốt
> **Đặt khám cùng bác sĩ chuyên khoa**
> **Sau khi bạn gửi:** bộ phận đặt lịch gọi lại trong `[khung giờ]` từ số `[đầu số]` để xác nhận. Buổi khám miễn phí, không ràng buộc.
> Form: họ tên · SĐT · dịch vụ quan tâm (bottom sheet) · *(tuỳ chọn)* khung giờ muốn được gọi lại.
> Song song: **`Hỏi riêng bác sĩ qua Zalo`**
> **FAQ câu 3:** "Tôi không muốn ai biết mình đi làm mũi." → *Bạn có thể hỏi riêng qua Zalo và chọn khung giờ gọi lại phù hợp. Thông tin chỉ dùng để liên hệ xác nhận.*

# F. BỘ CTA

| Vị trí | Nút | 4 câu hỏi được trả lời ra sao |
|---|---|---|
| Hero | `ĐẶT KHÁM MIỄN PHÍ VỚI BÁC SĨ` | **tin:** badge giấy phép + KCCS ngay dưới nút · **bây giờ:** lịch hội chẩn trong tuần `[xác minh lịch thật]` · **được gì:** bác sĩ đánh giá dáng mũi phù hợp với khuôn mặt bạn · **bấm xong:** gọi lại trong `[khung giờ]` từ `[đầu số]` |
| Màn 2 | `NHẬN BÁO GIÁ THEO DÁNG MŨI CỦA BẠN` | như trên + nêu rõ giá là tham khảo |
| Màn 4 | `XEM PHƯƠNG ÁN PHÙ HỢP VỚI TÔI` | như trên |
| Sticky | `Gọi` \| `Zalo` \| `Đặt lịch` | luôn hiện, 3 kênh cho 3 hoàn cảnh khách |

**Thank-you (5 thành phần):** xác nhận đã nhận · bộ phận nào gọi + khi nào + từ số nào · clip ngắn bác sĩ dặn chuẩn bị gì `[PLACEHOLDER video]` · nút quan tâm Zalo OA · 3 gạch đầu dòng "chuẩn bị cho buổi tư vấn".

# G. SPEC UI & MOBILE

```
┌──────────────────────── 375px ────────────────────────┐
│ [logo]                            [ĐẶT LỊCH] sticky   │
├───────────────────────────────────────────────────────┤
│ ảnh hero 4:5 — bác sĩ đang hội chẩn (ảnh thật)        │
│ H1 28px/800 navy — "chi phí … nâng mũi cấu trúc"      │
│ sub 15px ink-2                                        │
│ [ ĐẶT KHÁM MIỄN PHÍ VỚI BÁC SĨ ]  cam, 19px/800      │
│ miễn phí · không ràng buộc · bảo mật                  │
│ (badge) (badge) (badge)                               │
└───────────────────────────────────────────────────────┘
        ↓ màn 2 giá  → màn 3 bác sĩ → màn 4 case → màn 5 form
┌───────────────────────────────────────────────────────┐
│   Gọi    │    Zalo    │     Đặt lịch (cam)            │  ← sticky 480px
└───────────────────────────────────────────────────────┘
```

**Ảnh cần cấp:** hero `4/5` ảnh bác sĩ hội chẩn (ảnh thật hệ thống) · bác sĩ `3/4` · case `1/1` ×2 · video thank-you `16/9`.
**Mobile checklist:** đạt 8/8 ô §8 — input 16px, nút 52px, hero không lazy, Zalo deep-link cần kiểm trên máy thật.

# H. TRACKING & CRM

- **UTM:** `utm_source=google&utm_medium=cpc&utm_campaign=mui-cautruc-gia&utm_content=lp-short-v1`
- **Event:** `cta_hero` · `cta_price` · `cta_case` · `click_call` · `click_zalo` · `open_service_sheet` · `select_service` · `submit_form` · `follow_oa`
- **Tag lead về CRM:** kênh `google-search` · dịch vụ `mui-cau-truc` · nhiệt `hot` → kích hoạt luồng ZNS xác nhận lịch khám.

# I. KẾT QUẢ CỔNG PHÁP LÝ

| Ô | Kết quả |
|---|---|
| R4 bác sĩ | ⚠️ **chưa pass** — không ứng viên nào qua đủ 4 cổng; Louis Truong qua 3 cổng kỹ thuật nhưng K4 ghi đã gỡ khỏi danh sách duyệt quảng bá → chờ KF-02 |
| R3 tuyến | ✅ pass — nâng mũi cấu trúc tại 190 Trường Chinh (tuyến bệnh viện), footer dùng GP **194/BYT-GPHĐ** |
| R1 từ cấm | ✅ pass — đã rà, không có "số 1 / 100% / vĩnh viễn / không đau" |
| Mốc hồi phục | ✅ không nêu mốc cứng; trang ngắn không có màn hồi phục |
| R7 vật tư | ✅ pass — không nêu tên thương mại vật liệu |
| R5 hình ảnh | ⚠️ **chưa pass** — `/case-thuc-te/` trống; ảnh từ `/hinh-anh-khach-hang/` chưa có bảng kê consent nội bộ |
| Số liệu | ✅ số năm + số ca của bác sĩ lấy đúng dữ liệu live, có gắn `*` |
| Giá | ✅ ghi "tham khảo", lấy động |
| R9 GXNNDQC | ⚠️ **cần xin trước khi phát hành** |

**Danh sách phải bổ sung trước khi publish:**
1. **KF-02 xác nhận bác sĩ mũi được duyệt quảng bá tại Hà Nội** (R4) — *chặn nặng nhất*, và phải giải quyết lệch nguồn ở Dr. Louis Truong
2. 2–3 ảnh trước–sau nhóm Mũi + **xác nhận consent còn hiệu lực** (R5)
3. Bản chính thức chính sách bảo hành (để viết mục "trong chi phí có gì")
4. GXNNDQC (R9)
5. Xác minh lịch hội chẩn thật (để câu "tại sao bây giờ" không thành khan hiếm giả)

# J. SCORECARD

| Tiêu chí | Điểm | Ghi chú |
|---|---|---|
| Message-match | **19**/20 | hero nhắc đúng từ khoá + offer; ảnh hero còn là placeholder |
| Luồng CX đúng nhiệt | **15**/15 | 5 màn cho khách mức nhận thức 5 |
| Trust đủ & đúng thứ tự BL | **12**/20 | PTTM cần "bác sĩ → case" mà **cả hai đang placeholder** (bác sĩ chờ KF-02, case chờ ảnh có consent) |
| CTA | **20**/20 | đủ 4 câu hỏi, form 3 trường, thank-you đủ 5 thành phần |
| Mobile-first | **15**/15 | đạt 8/8 |
| UI nhất quán `KF-09` | **10**/10 | token production, một màu CTA |
| **Cổng pháp lý** | **chưa pass** | R4 + R5 + R9 |
| **TỔNG** | **91/100** nhưng **CHƯA ĐƯỢC GIAO** | cổng pháp lý chưa pass → giữ ở trạng thái chờ KF-02 + ảnh case + GXNNDQC |

> Đây là tình huống thường gặp nhất: **bố cục tốt, thiếu nguyên liệu**. Việc cần làm không phải viết lại trang, mà là đi lấy 5 mục ở mục I. Thứ tự lấy theo `KF-14` mục 9.
> Lưu ý cách đọc điểm: 91/100 **không** có nghĩa trang gần xong. Cổng pháp lý fail là fail — điểm chỉ nói bố cục và copy đã ổn, phần còn lại là đi xin dữ liệu.

# K. A/B & KPI

| # | Giả thuyết | A | B | Chỉ số kết luận | Ngưỡng | Đánh giá sau |
|---|---|---|---|---|---|---|
| 1 | Khách mức 5 phản hồi tốt hơn với headline nói **"gồm những gì"** hơn headline nói **"chi phí"** | góc Bác sĩ | góc Nỗi sợ được trả lời | **booking rate** | chênh ≥ 15% tương đối | 14 ngày hoặc ≥ 100 lead/nhánh |
| 2 | Đưa **bảo hành lên ngay cạnh giá** ở màn 2 làm tăng tỉ lệ kết nối | bảo hành ở màn 2 | bảo hành ở màn 5 | **tỉ lệ lead kết nối** | chênh ≥ 10% tương đối | 14 ngày |

**Theo dõi:** CVR (lead/visit) · tỉ lệ lead kết nối · booking rate · show-up rate.
**Mốc đánh giá lại:** sau **14 ngày** hoặc khi đủ 100 lead/nhánh, tuỳ cái nào đến trước. Ghi kết quả vào `KF-16` mục 3 và 4.

---

## Đọc output này như thế nào

| Nếu bạn là | Đọc mục |
|---|---|
| Người duyệt nội dung | **I** rồi **E** |
| Pháp chế | **I** — có đủ mã rào và ai phải duyệt |
| Designer / dev | **D**, **G**, rồi `/prototype` |
| Performance / media | **C**, **H**, **K** |
| Người quyết ngân sách | **J** rồi **K** |
