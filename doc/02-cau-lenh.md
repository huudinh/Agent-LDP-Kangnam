# 02 — BẢY LỆNH CỦA AGENT

| Lệnh | Việc agent làm | Input tối thiểu | Output |
|---|---|---|---|
| `/brief` | Chuẩn hoá brief, hỏi trường thiếu (tối đa 3 câu) | một ý tưởng chiến dịch | brief 9 trường đã chuẩn hoá |
| `/landing` | Dựng trọn bộ | brief đủ trường `*` | output A→K |
| `/audit` | Chấm landing hiện có | URL hoặc nội dung + kênh + ad copy | điểm scorecard + danh sách lỗi theo mức + phần viết lại |
| `/variant` | Chuyển sang kênh khác | landing master + kênh mới | phần KHÁC master + scorecard mới |
| `/cta` | Tối ưu riêng CTA · form · thank-you | CTA hiện tại | bảng CTA × 4 câu hỏi + bản viết lại |
| `/ab` | Đề xuất test | landing + chỉ số đang có | 3 giả thuyết + chỉ số kết luận + thời hạn |
| `/prototype` | Xuất HTML một file | output `/landing` | file `.html` mobile-first + bảng kê ảnh |

Không gọi lệnh → agent tự suy (có brief → `/landing` · có URL → `/audit` · có landing cũ + kênh mới → `/variant`) và **nói rõ đã chọn lệnh nào**.

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
/brief  →  /landing  →  (sửa theo scorecard)  →  /prototype
                                                     ↓
                                              publish + đo
                                                     ↓
                                   ghi KF-16  →  /ab hoặc /variant
```

Với trang đã chạy: `/audit` → sửa → `/cta` → ghi `KF-16`.
