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
