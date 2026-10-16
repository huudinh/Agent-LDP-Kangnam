# 02 — TÁM LỆNH CỦA AGENT

| Lệnh | Việc agent làm | Input tối thiểu | Output |
|---|---|---|---|
| `/wizard` | **Hỏi dẫn từ đầu** — 3 vòng × 3 câu, mỗi câu có phương án chọn sẵn | **chỉ cần tên dịch vụ** | BRIEF ĐÃ KHOÁ 9 dòng → chạy tiếp `/landing` |
| `/brief` | Chuẩn hoá brief đã có, hỏi trường thiếu (tối đa 3 câu) | một brief dở dang | brief 9 trường đã chuẩn hoá |
| `/landing` | Dựng trọn bộ | brief đủ trường `*` | output A→K |
| `/audit` | Chấm landing hiện có | URL hoặc nội dung + kênh + ad copy | điểm scorecard + danh sách lỗi theo mức + phần viết lại |
| `/variant` | Chuyển sang kênh khác | landing master + kênh mới | phần KHÁC master + scorecard mới |
| `/cta` | Tối ưu riêng CTA · form · thank-you | CTA hiện tại | bảng CTA × 4 câu hỏi + bản viết lại |
| `/ab` | Đề xuất test | landing + chỉ số đang có | 3 giả thuyết + chỉ số kết luận + thời hạn |
| `/prototype` | Xuất HTML một file | output `/landing` | file `.html` mobile-first + bảng kê ảnh |

Không gọi lệnh → agent tự suy (**chỉ có tên dịch vụ → `/wizard`** · có brief → `/landing` · có URL → `/audit` · có landing cũ + kênh mới → `/variant`) và **nói rõ đã chọn lệnh nào**.

---

## 0. `/wizard` — khi chỉ biết tên dịch vụ

Dùng khi bạn chưa có brief: *"tôi muốn làm landing Hàm mặt"*. Agent hỏi dẫn **theo vòng, mỗi vòng tối đa 3 câu**, mỗi câu kèm phương án chọn sẵn và lựa chọn *"để agent chọn"*. Sau mỗi vòng nó chốt lại một dòng rồi mới hỏi tiếp — ⛔ không bắn 9 câu một lúc.

| Vòng | Khoá cái gì | Ba câu |
|---|---|---|
| **1** | Khung trang | dịch vụ con · kênh · **ad copy / keyword nguyên văn** |
| **2** | Người đọc trang | chân dung (6 nhóm `KF-12`) · nhiệt độ + mức nhận thức · cơ sở + tuyến |
| **3** | Vật liệu đang có | CTA mục tiêu · offer · bác sĩ / ảnh case / bảng giá **đã có chưa** |

Đủ 9 ô → agent in **BRIEF ĐÃ KHOÁ** rồi hỏi đúng một câu *"Chạy `/landing` luôn chứ?"*.

**Agent dừng giữa chừng trong hai trường hợp:** dịch vụ đại phẫu mà cơ sở khai không phải tuyến bệnh viện (dừng ở vòng 2, nêu hai cách xử lý R3) · bạn khai tên bác sĩ không có trong danh sách live (không ghi tên đó vào brief).

Gõ *"đủ rồi, cứ làm"* bất cứ lúc nào → agent dừng hỏi, giả định các ô còn lại **trừ trường pháp lý**, ghi khối GIẢ ĐỊNH rồi chạy tiếp.

Prompt mẫu cho cả 10 nhóm dịch vụ: [`prompts/prompt-wizard.md`](../prompts/prompt-wizard.md).

---

## 1. `/brief` — dùng khi chưa biết mình thiếu gì

Agent hỏi tối đa **3 câu, gộp một lần**. Nó **không** tự giả định: tên bác sĩ · cơ sở · tuyến · giá · ưu đãi · số liệu.

Nói *"cứ làm"* → agent giả định các trường **không phải pháp lý**, ghi khối **GIẢ ĐỊNH** ở đầu output, và vẫn để `[CHỜ CẬP NHẬT]` cho trường pháp lý.

**Trường quan trọng nhất là số 2 — ad copy/keyword nguyên văn.** Thiếu nó thì không khoá được message-match, và trang trượt ngay tiêu chí 20 điểm.

---

## 2. `/landing` — lệnh chính

Chạy đúng 3 tầng: **nguồn & đối tượng → trải nghiệm 9 màn → CTA**. Xuất 11 mục A→K (xem [`03-output-mau.md`](03-output-mau.md)).

**Agent sẽ chặn bạn trong 4 trường hợp:**
1. Brief thiếu trường `*` → hỏi lại trước khi làm.
2. Dịch vụ đại phẫu gắn vào cơ sở không có giấy phép đại phẫu (R3) → dừng, yêu cầu chọn cách xử lý.
3. Tên bác sĩ không có trong `KF-01` → `[CHỜ CẬP NHẬT]`, không viết tên.
4. Cổng pháp lý fail → **không xuất trang**, chỉ xuất danh sách vướng gì + ai phải duyệt.

Đây là tính năng, không phải lỗi. Agent dễ dãi ở bốn chỗ này thì nó đang tạo rủi ro thay vì tạo lead.

---

## 3. `/audit` — chấm trang đang chạy

Đưa kèm **triệu chứng** thì audit mới đúng chỗ:

| Triệu chứng | Nghi phạm số 1 |
|---|---|
| CTR tốt, không ai điền form | sai message-match / sai kiểu landing so với nhiệt độ |
| Lead nhiều, không ai bắt máy | CTA thiếu câu "bấm xong thì sao" |
| Bắt máy nhưng không booking | gỡ sai rào cản của chân dung |
| Booking nhiều, show-up thấp | trang hứa khác thứ khách nhận được |

Chi tiết + prompt mẫu: [`prompts/prompt-audit.md`](../prompts/prompt-audit.md).

---

## 4. `/variant` — chuyển kênh

Đổi kênh = đổi **nhiệt độ** → buộc đổi **độ dài trang · nấc CTA · thứ tự trust**.
Chỉ đổi headline và ảnh thì **không phải** biến thể — đó là A/B test, dùng `/ab`.
Bảng chuyển kênh: [`prompts/prompt-variant.md`](../prompts/prompt-variant.md).

---

## 5. `/cta` — siết phần sinh lead

Agent lập bảng **CTA × 4 câu hỏi** (tại sao tin · tại sao bây giờ · được gì · bấm xong thì sao), ô nào trống thì viết luôn câu nên dùng. Kèm: rút form về ≤ 3 trường, viết lại microcopy, dựng thank-you đủ 5 thành phần.

Thường đây là lệnh cho ROI cao nhất trên một trang đã chạy: nó sửa đoạn **lead → kết nối**, chỗ mất tiền âm thầm nhất.

---

## 6. `/ab` — đề xuất test

Mỗi giả thuyết gồm: **biến đổi gì · vì sao nghĩ nó thắng · chỉ số kết luận · ngưỡng · thời hạn đánh giá**.

Hai luật: ① mỗi test **một biến**; ② chỉ số kết luận là **booking rate**, không phải CVR — biến thể tăng CVR mà giảm booking là biến thể xấu.

---

## 7. `/prototype` — xuất HTML

Ra **một file `.html` tự chứa**, mobile-first, theo `KF-09`, dùng [`template/lp-skeleton.html`](../template/lp-skeleton.html) làm khung.

Luôn kèm **BẢNG KÊ ẢNH CẦN CẤP** (màn · tỉ lệ · nội dung cần · ai duyệt). Không có bảng này thì trang **chưa giao xong**.

⚠️ File xuất ra vẫn còn `figure.ph` và `[CHỜ CẬP NHẬT]` — đó là đúng. **Trước khi publish phải thay hết hoặc ẩn khối.** Placeholder nội bộ lọt ra production là lỗi đã từng xảy ra ở landing Mũi v3.

---

## Thứ tự dùng điển hình

```
/wizard →  /landing  →  (sửa theo scorecard)  →  /prototype
                                                     ↓
                                              publish + đo
                                                     ↓
                                   ghi KF-16  →  /ab hoặc /variant
```

Với trang đã chạy: `/audit` → sửa → `/cta` → ghi `KF-16`.
