# CHANGELOG — Agent-LDP-Kangnam

---

## v1.2.3 — 2026-10-16 · trang hướng dẫn rút về 3 mục

Trang đang gánh quá nhiều thứ mà agent đã biết sẵn. Rút về đúng ba việc người dùng cần:
**① cài đặt trên hệ thống AI · ② prompt mẫu · ③ link kiến thức.**

**Bỏ hẳn bốn mục:** *Bảy/Tám lệnh* · *Trước khi publish* (cổng R4/R3 + checklist 10 ô) · *Dữ liệu* · *Việc còn treo*.
Toàn bộ nội dung đó **vẫn nằm trong bộ não và `knowledge/`** — agent áp dụng khi chạy, người cài không cần đọc.

**Gộp:** bảng 8 file tri thức chuyển vào trong mục Cài đặt (vì đó là việc phải upload), không còn là mục riêng.
**Giữ một dòng:** tên 8 lệnh nằm gọn trong phần mở đầu mục Prompt mẫu.

**Mục 3 — Kiến thức** chỉ còn bảng dẫn đường: [bản đặc tả gốc](https://claude.ai/artifact/SJqCtgkuSakBrbj2jQ9WD3) · [Album Kangnam](https://hcigroup.vn/app/albumkn/) · tám file `knowledge/` · output mẫu · tài liệu người mới. Giữ lại đúng một cảnh báo: **ảnh trong kho ≠ đã có consent**.

Dọn luôn CSS và JS chết sau khi bỏ mục (`ul.check`, `.pill`, khối localStorage của checklist): template giảm 27.413 → 26.050 ký tự.

**Kết quả:** phần chữ của trang còn **48 KB**, trong đó 23 KB là 42 thẻ prompt — thứ người ta mở trang để lấy.

| Mục | Ký tự |
|---|---|
| 1 · Cài đặt (3 tab + 3 thẻ copy + bảng 8 file) | 6.775 |
| 2 · Prompt mẫu (42 thẻ, 4 nhóm lọc) | 23.278 |
| 3 · Kiến thức (bảng link) | 1.767 |

> Checklist 10 ô trước khi publish đã bị bỏ khỏi trang. Nếu đội vận hành cần nó dạng tick được, nói để dựng thành một trang riêng thay vì nhồi lại vào đây.

---

## v1.2.2 — 2026-10-16 · nối kho ảnh nội bộ Album Kangnam

Trang công khai `/case-thuc-te/` vẫn trống, nhưng **ảnh case đã có sẵn** trong kho nội bộ: **Album Kangnam** — <https://hcigroup.vn/app/albumkn/> (*"Thư Viện Ảnh Theo Chủ Đề"* của HCI Group). Đã nối nguồn này vào tri thức.

**App có gì dùng được:** Chủ đề/Album (gom theo dịch vụ hoặc chiến dịch) · **thẻ tag** (lọc nhanh) · tiêu đề + mô tả từng ảnh · ngày tải lên · kích thước · độ phân giải · chia sẻ album / chia sẻ thẻ tag. Có đăng nhập, phân quyền (Quản trị viên · Biên tập viên · Thành viên) và **API cho ứng dụng ngoài** (cần khoá API do Quản trị viên cấp và API đang bật).

**Hai luật mới ghi vào bộ não:**
- ⛔ **Ảnh trong kho ≠ đã có consent.** Kho là chỗ *lưu* ảnh, không phải chỗ *cấp phép* — rào **R5** vẫn đòi văn bản đồng ý của từng khách.
- **Agent không tự lấy ảnh từ kho** (cần đăng nhập / khoá API). Người làm landing chọn ảnh rồi đưa agent **link ảnh + tiêu đề + mô tả + mốc thời gian chụp**.

**Đề xuất giải quyết luôn việc còn treo số 3** (bảng kê consent): gắn mỗi ảnh case một trong ba tag — `consent-ok` · `consent-cho` · `consent-het-han`, thêm `phap-che-duyet` khi Pháp chế duyệt hình. Khi đó **bộ lọc tag của app chính là bảng kê consent**, không phải dựng file riêng.

### Sửa gì
- `KF-14` → thêm **mục 5.1 Kho ảnh nội bộ** (cấu trúc, cách bàn giao cho agent, quy ước tag); mục 4 đổi từ *"đây là mục chặn số 1"* sang *"lấy ảnh từ kho nội bộ, `/case-thuc-te/` là nơi publish"*; mục 9 đổi thứ tự việc còn thiếu.
- `KF-01` §0 + `SYSTEM-PROMPT` §1.1 → thêm dòng **Kho ảnh nội bộ**, kèm hai luật trên.
- `SYSTEM-PROMPT-NGAN` → thêm vào mục Nguồn dữ liệu; nén 7 chỗ để vẫn vừa: **7.984 / 8.000**.
- Trang hướng dẫn → bảng Dữ liệu thêm dòng kho nội bộ (có link), thêm khối cảnh báo consent, đổi bảng *Việc còn treo*.

---

## v1.2.1 — 2026-10-16 · thống nhất cách đặt tên

Agent có hai tên song song: thư mục là `Agent-LDP-Kangnam` còn tài liệu gọi là *KLA — Kangnam Landing Agent*. **Thống nhất về `Agent-LDP-Kangnam`** cho mọi nơi.

| Chỗ | Trước | Sau |
|---|---|---|
| Định danh trong bộ não | *Bạn là **Kangnam Landing Agent (KLA)*** | *Bạn là **Agent-LDP-Kangnam*** |
| Tên project khi cài (Claude · ChatGPT · Gemini) | `KLA — Kangnam Landing Agent` | `Agent-LDP-Kangnam` |
| Tiêu đề + H1 trang hướng dẫn | *Kangnam Landing Agent* | *Agent-LDP-Kangnam* |
| File sinh ra | `tools/huong-dan-kla.*` | `tools/huong-dan.*` |
| `id` khối dữ liệu trong trang | `kla-payload` | `huong-dan-payload` |
| Khoá localStorage của checklist | `kla-checklist-v1` | `ldp-kangnam-checklist-v1` |

Chỗ nào trước đây viết *"spec KLA"* / *"palette KLA"* nay đổi thành **"bản đặc tả gốc"** — rõ hơn, vì đó là tài liệu nguồn chứ không phải tên agent. 12 file đã sửa, soát lại còn **0 chỗ** dùng tên cũ.

**Nhân tiện:** bộ não bump lên `Version: 1.2` cho khớp CHANGELOG (đang kẹt ở 1.0); bản ngắn **7.953 / 8.000** ký tự — tên mới dài hơn "KLA" nên đã nới thêm margin; `lp-skeleton.html` đổi nhãn phiên bản v1.0 → v1.2.

> ⚠️ Ai đã tạo project trên Claude/ChatGPT/Gemini bằng tên cũ thì **đổi tên project** cho khớp. Nội dung dán vào không đổi, chỉ cần dán lại Thẻ A hoặc Thẻ B bản mới.

---

## v1.2 — 2026-10-16 · chế độ hỏi dẫn `/wizard`

Người dùng thường chỉ biết *"tôi muốn làm landing Hàm mặt"* chứ chưa có brief. Trước v1.2 agent chỉ hỏi gộp tối đa 3 câu rồi tự giả định phần còn lại — đủ cho người đã quen, nhưng người mới không biết mình đang thiếu gì.

**Thêm `/wizard` — hỏi dẫn 3 vòng × 3 câu**, mỗi câu kèm phương án chọn sẵn và lựa chọn *"để agent chọn"*; chốt lại sau từng vòng, đủ 9 ô thì in **BRIEF ĐÃ KHOÁ** rồi hỏi một câu *"Chạy /landing luôn chứ?"*.

| Vòng | Khoá cái gì | Ba câu |
|---|---|---|
| 1 | Khung trang | dịch vụ con · kênh · **ad copy / keyword nguyên văn** |
| 2 | Người đọc trang | chân dung · nhiệt độ + mức nhận thức · cơ sở + tuyến |
| 3 | Vật liệu đang có | CTA mục tiêu · offer · bác sĩ / ảnh case / bảng giá đã có chưa |

**Hai cổng chặn sớm** — agent dừng giữa chừng thay vì hỏi hết rồi mới báo lỗi: ① đại phẫu + cơ sở không phải tuyến bệnh viện → dừng ở vòng 2, nêu hai cách xử lý R3 · ② tên bác sĩ không có trong danh sách live → không ghi vào brief, nêu bốn cổng R4.

**Phương án chọn sẵn lấy từ tri thức, không bịa:** dịch vụ con từ `KF-01` mục 5 · kênh từ ma trận §5.1 · chân dung từ `KF-12` mục 3 · cơ sở từ `KF-01` mục 2. Trường pháp lý vẫn **không bao giờ** được giả định, kể cả khi người dùng chọn *"để agent chọn"*.

### Sửa gì
- `SYSTEM-PROMPT.md` → thêm **§4.1** chế độ hỏi dẫn, thêm `/wizard` vào bảng lệnh (7 → **8 lệnh**), sửa luật tự suy lệnh.
- `SYSTEM-PROMPT-NGAN.md` → thêm mục `/wizard` rút gọn; cắt mục VÒNG HỌC và nén 8 chỗ khác để vẫn vừa giới hạn: **7.989 / 8.000 ký tự**. Nhân tiện sửa R4 từ 3 cổng thành **4 cổng** cho khớp bộ não.
- **Thêm `prompts/prompt-wizard.md`** — prompt khởi động, **10 prompt một dòng cho 10 nhóm dịch vụ**, bản dùng khi đã có sẵn một phần, bảng 3 vòng, và 6 câu trả lời nhanh khi đang trong vòng hỏi.
- `doc/02-cau-lenh.md` + `README.md` → cập nhật 8 lệnh.
- Trang hướng dẫn → nhóm prompt mới **Hỏi dẫn (18 thẻ)**, tổng **42 mẫu prompt**.

---

## v1.1 — 2026-10-16 · nối agent với dữ liệu live

Người dùng chỉ định **5 nguồn dữ liệu chính thống**. Đã lấy dữ liệu thật về, đối chiếu, sửa knowledge và thêm script chụp lại.

| Nguồn | Lấy được gì |
|---|---|
| `/doi-ngu-bac-si/` | **16 bác sĩ** trong JSON nhúng `kn-doctors-data` + Dr. Richard Huy giới thiệu riêng — mỗi người có **CCHN · chuyên khoa · cơ sở · cờ `verified` · số năm · số ca · ảnh** |
| menu chính | **10 nhóm dịch vụ** (ảnh người dùng gửi, khớp site) |
| `/chi-nhanh/` | **7 cơ sở tại 7 tỉnh thành** = 2 bệnh viện + 5 viện thẩm mỹ |
| `/case-thuc-te/` | 4 nhóm lọc · **trang đang trống** ("Chưa có ca nào trong nhóm này") |
| `/hinh-anh-khach-hang/` | **9 nhóm** ảnh trước–sau, đã khai consent + câu miễn trừ chuẩn |

### Sửa gì
- **`KF-01` → v1.1**: thêm **§0 Nguồn dữ liệu chính thống**; thay bảng cơ sở (7, bỏ dòng "viện TM 194 Trường Chinh" không có thật); thay danh sách bác sĩ bằng **bảng 17 người kèm CCHN + `verified`**; taxonomy **tách Da Liễu / Trị Sắc Tố thành 2 nhóm** (menu thật có 10 nhóm, bản cũ gộp còn 9); sửa email liên hệ theo site.
- **`KF-14` → v1.1**: mục 1 thành bảng nguồn + trạng thái; case và ảnh trước–sau có nguồn thật; thêm câu miễn trừ nguyên văn của site để dùng lại; thêm cảnh báo `/case-thuc-te/` đang trống.
- **`SYSTEM-PROMPT`**: thêm **§1.1 Nguồn dữ liệu**; §9.1 đổi luật bác sĩ thành **3 cổng** (có trong danh sách live · đúng chuyên khoa + đúng cơ sở · `verified` + có CCHN); §9.7 chốt con số 7 cơ sở.
- **`SYSTEM-PROMPT-NGAN`** → v1.1, thêm mục Nguồn dữ liệu, vẫn **7.993 ký tự** (giới hạn 8.000).
- **Thêm `tools/fetch-du-lieu.py`** — chụp lại 5 nguồn, in ra: tổng bác sĩ · ai thiếu CCHN · ai chưa `verified` · số cơ sở · case trống hay không · số nhóm ảnh. Ghi snapshot JSON vào `out/`.

### Ba phát hiện đáng chú ý
1. **`Dr. Jolie Huynh` không còn tồn tại** — trang `/doi-ngu-bac-si/jolie-huynh/` trả **404** và tên này không có trong danh sách live, nhưng **vẫn đang nằm trong `kn-ho-so-thuong-hieu.md` của `Agent-AdsOptimize-Kangnam`**. Hai slug khác cũng 404: `bac-si-dr-hong-vu`, `le-thi-thuy`. → Đã loại khỏi `KF-01`. **Cần sửa cả ở agent nguồn.**
2. **Site tự đánh dấu `status: verified`** cho từng bác sĩ — 10/16 verified, **6 người để trống**; và **4 người không có số CCHN** (Alex Han · Nicolas Hung · Felix Tran · Frankie Vu). Đây là tín hiệu duyệt sẵn có, agent dùng làm cổng R4.
3. **`/case-thuc-te/` đang trống** → màn 5 của mọi landing hiện phải dùng ảnh từ `/hinh-anh-khach-hang/` hoặc placeholder. Đây là mục chặn số 1 lúc này.

---

## v1.0 — 2026-10-16 · bản đầu

**Nguồn gốc:** bản đặc tả gốc *Custom Instructions* (artifact `SJqCtgkuSakBrbj2jQ9WD3`), đối chiếu và nối với tri thức Kangnam đang có trong repo.

### Đã dựng
| File | Nội dung |
|---|---|
| `SYSTEM-PROMPT.md` | Bộ não đầy đủ §0–§14 (Claude Project / Gemini) |
| `SYSTEM-PROMPT-NGAN.md` | Bản 7.991 ký tự cho ChatGPT Custom GPT |
| `knowledge/KF-01-ho-so-thuong-hieu.md` | Thương hiệu · bác sĩ · cơ sở + tuyến · taxonomy · dữ liệu động |
| `knowledge/KF-09-design-system.md` | Token production v3.0 · khung trang · form · ô ảnh tạm |
| `knowledge/KF-11-cong-phap-ly.md` | Cổng pháp lý + bảng rào **R0–R12** + checklist 13 ô |
| `knowledge/KF-12-hanh-vi-khach-hang.md` | ★ Lõi hành vi: 6 nhóm · 3 rào cản · 5 mức nhận thức · 6 giai đoạn · hành vi trên trang |
| `knowledge/KF-13-noi-so-phan-doi.md` | ★ Nỗi sợ & phản đối theo 5 BL, kèm câu trả lời đã rà từ cấm |
| `knowledge/KF-14-proof-bank.md` | Ngân hàng bằng chứng + trạng thái pháp lý từng loại |
| `knowledge/KF-15-block-library.md` | 24 mã khối `B-*` map 9 màn + bộ khối theo nhiệt độ |
| `knowledge/KF-16-performance-log.md` | Khung vòng học (đang trống, chờ dữ liệu thật) |
| `template/lp-skeleton.html` | Khung HTML một file: 9 màn · form + bottom sheet · sticky bar · thank-you view |
| `prompts/` | `prompt-landing.md` · `prompt-audit.md` · `prompt-variant.md` |
| `doc/` | `01-cai-dat` · `02-cau-lenh` · `03-output-mau` · `04-prompt-nguoi-moi` · `CHANGELOG` |

### Khác với spec gốc — và vì sao

| # | Spec gốc | Bản này | Lý do |
|---|---|---|---|
| 1 | KF-01→KF-11 "đã có" | Gom lại còn **3 file** (`KF-01`, `KF-09`, `KF-11`) lấy từ tri thức repo | Repo đã có brand profile, design system và rào R0–R11 thật. Dùng lại thay vì tạo file rỗng |
| 2 | KF-12→KF-16 "cần dựng" | **Đã dựng cả 5** | Đây là 5 file làm agent chạy được; `KF-12` và `KF-13` là lõi của yêu cầu "xuất phát từ hành vi khách" |
| 3 | Palette `#294573 / #3A6CAE / teal / gold / nude / peach` | Dùng **token production `#074E84` / `#EF6103`**; palette đó ghi lại ở `KF-09` mục 1 là **chưa dùng** | Token production đã kiểm tương phản WCAG và khớp trang đang chạy. Dùng palette mới sẽ làm landing mới lệch hệ thống → **cần brand/pháp chế chốt** (xem *Việc còn treo* #3) |
| 4 | "R12" được nhắc như rào có sẵn | Thêm **R12 mới** vào bảng, gắn cờ 🆕 chờ pháp chế đánh số | Bảng rào gốc của repo chỉ có R0–R11. R12 gom giới hạn hình ảnh cơ thể của policy Meta/Google/TikTok — giới hạn thật, nhưng mã số chưa chính thức |
| 5 | "2 bệnh viện + 7 cơ sở chi nhánh" | **Không dùng con số nào**, ghi `[CHỜ XÁC MINH]` | Ba nguồn trong repo nói khác nhau (xem *Việc còn treo* #2) |
| 6 | 3 vai "CRO + copywriter + UX/UI" | Định lượng **60/25/15** | Để agent biết khi xung đột thì nghiêng về đâu: CRO thắng "đẹp" |
| 7 | — | Thêm `KF-12` mục 7 **hành vi trên trang** và mục 9 **5 lỗi hành vi** | Lấy từ bản audit landing Mũi v3 — bài học thật, không phải suy luận |
| 8 | — | Thêm luật **"thiếu dữ liệu thì ẩn khối, không để placeholder lộ ra production"** | Landing Mũi v3 từng để `chờ KF-01`, `Chưa có giá` lên trang thật |

---

## ✅ ĐÃ GIẢI QUYẾT ở v1.1

| # | Việc | Kết quả |
|---|---|---|
| ~~1~~ | Bảng bác sĩ × dịch vụ × cơ sở | ✅ **Có đủ từ nguồn live** — 17 bác sĩ kèm chuyên khoa, cơ sở, CCHN, cờ verified (`KF-01` mục 4). Còn lại chỉ là xác minh 4 CCHN thiếu + 6 người chưa verified |
| ~~2~~ | Số cơ sở hệ thống | ✅ **Chốt: 7 cơ sở** (2 bệnh viện + 5 viện thẩm mỹ) theo `/chi-nhanh/` |
| — | Taxonomy dịch vụ | ✅ **10 nhóm** theo menu chính, tách Da Liễu / Trị Sắc Tố |

---

## 🔶 VIỆC CÒN TREO — cần người thật chốt

| # | Việc | Chặn gì | Ai chốt |
|---|---|---|---|
| **1** | **Nạp case lên `/case-thuc-te/`** — trang đang trống | Màn 5 của **mọi** landing | Marketing + CSKH |
| **2** | **Bảng kê ảnh ↔ consent ↔ hạn consent** (bản nội bộ) | Màn 5 — rào **R5**. Trang public khai "có đồng ý" nhưng không lộ dữ liệu kiểm chứng | CSKH + pháp chế |
| **3** | **CCHN cho 4 bác sĩ thiếu** (Alex Han · Nicolas Hung · Felix Tran · Frankie Vu) + xác nhận **6 bác sĩ `status` trống** | Màn 4 khi dùng các bác sĩ đó — rào **R4** | Chuyên môn + HR |
| **4** | **Bản chính thức chính sách bảo hành** theo nhóm dịch vụ | Màn 7 (giá/offer) | Pháp chế |
| **5** | **Mốc hồi phục dạng khoảng** theo từng dịch vụ, có bác sĩ xác nhận | Màn 6 và FAQ — `KF-13` mục 9 | Chuyên môn |
| **6** | **Danh mục thiết bị/vật tư được phép nêu tên** + số lưu hành | Màn 3 — rào **R7** | Kho vật tư + pháp chế |
| **7** | **Bảng màu cho landing:** token production hay palette của spec gốc | `KF-09` mục 1. Trộn hai bảng làm trang mới lệch trang đang chạy | Brand + pháp chế |
| **8** | **Mã chính thức cho rào R12** (hình ảnh cơ thể & giảm cân) | `KF-11` mục 2 | Pháp chế |
| **9** | **Phạm vi giấy phép chi tiết từng viện thẩm mỹ** — `/chi-nhanh/` chỉ nói chung "da, spa, tiểu phẫu" | Landing local — rào **R3** | Pháp chế |
| **10** | **Làm rõ con số "hơn 3.000.000 ca"** và dữ liệu `rating`/`reviews` trên trang bác sĩ | Badge màn 1 · khối review | Pháp chế |
| **11** | **Bác sĩ nhóm nha khoa** — không có trong dữ liệu live | Màn 4 của landing KDT | Chuyên môn |
| **12** | **Bảng ánh xạ mã khối `B-*` ↔ component WordPress** `SCI_Theme_v3` | `KF-15` mục 3 | Dev |
| **13** | **GXNNDQC cho từng landing** | Rào **R9** — không có thì không được phát hành | Pháp chế (Sở Y tế) |

**Thứ tự nên làm: 1 → 2 → 3 → 4.** Bốn mục này mở nốt màn 4, 5 và 7 — sau đó agent xuất được landing gần như không còn placeholder.

### Việc cần làm ở agent khác
`Agent-AdsOptimize-Kangnam/knowledge/kn-ho-so-thuong-hieu.md` vẫn liệt kê **Dr. Jolie Huynh** (trang 404) và vẫn ghi cơ sở theo bảng 8 dòng cũ. Cần đồng bộ với `KF-01` v1.1 của agent này.

---

## Dự kiến v1.1 — khi có dữ liệu

- Điền `KF-14` phần bác sĩ và case (sau việc còn treo #1, #5).
- Mở `KF-16` bằng 3–5 dòng log thật → chuyển 4 giả thuyết ở mục 5 thành pattern có số.
- Bổ sung `KF-15` mục 3 bảng component WordPress.
- Chạy `/audit` lại landing Mũi v3 bằng scorecard để có mốc so sánh đầu tiên.
- Nếu *Việc còn treo #3* chốt chọn palette của spec gốc: cập nhật `KF-09` + `template/lp-skeleton.html`, kiểm lại toàn bộ tương phản.
