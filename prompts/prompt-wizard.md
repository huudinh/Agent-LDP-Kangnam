# PROMPT MẪU — `/wizard` (hỏi dẫn từ đầu)

Dùng khi bạn **chỉ biết mình muốn làm landing cho dịch vụ nào**, chưa có brief. Agent sẽ hỏi dẫn theo vòng, mỗi vòng tối đa 3 câu, mỗi câu kèm phương án chọn sẵn — bạn chỉ việc chọn A/B/C hoặc gõ *"để agent chọn"*.

Hết 3 vòng, agent in ra **Brief đã khoá** (9 dòng) rồi hỏi đúng một câu *"Chạy `/landing` luôn chứ?"*.

---

## A. Prompt khởi động

```
/wizard [tên dịch vụ]

Tôi mới chỉ biết muốn làm landing cho dịch vụ này, chưa có brief.
Hỏi dẫn giúp tôi: mỗi vòng tối đa 3 câu, mỗi câu kèm phương án chọn sẵn
và một lựa chọn "để agent chọn".

Chốt lại sau từng vòng. Đủ 9 ô thì in Brief đã khoá rồi hỏi tôi có chạy /landing không.
Trường pháp lý (bác sĩ · cơ sở · tuyến · giá) thì cứ để [CHỜ CẬP NHẬT], đừng đoán.
```

---

## B. Mười prompt một dòng — chọn đúng nhóm dịch vụ của bạn

| Nhóm dịch vụ | Prompt |
|---|---|
| Mắt | `/wizard Dịch vụ Mắt — tạo mắt 2 mí. Hỏi dẫn giúp tôi, mỗi vòng tối đa 3 câu, có phương án chọn sẵn.` |
| Mũi | `/wizard Dịch vụ Mũi — nâng mũi cấu trúc. Hỏi dẫn giúp tôi, mỗi vòng tối đa 3 câu, có phương án chọn sẵn.` |
| Hàm mặt | `/wizard Hàm Mặt — chỉnh hàm hô. Hỏi dẫn giúp tôi, mỗi vòng tối đa 3 câu, có phương án chọn sẵn. Nhớ kiểm tuyến cơ sở vì đây là đại phẫu.` |
| Thẩm mỹ Vòng 1 | `/wizard Thẩm mỹ Vòng 1 — nâng ngực. Hỏi dẫn giúp tôi, mỗi vòng tối đa 3 câu, có phương án chọn sẵn. Nhớ kiểm tuyến cơ sở vì đây là đại phẫu.` |
| Lipo 360 – Mỡ – Mông | `/wizard Lipo 360 — giảm mỡ. Hỏi dẫn giúp tôi, mỗi vòng tối đa 3 câu. Nhắc tôi luật R12: không before/after cơ thể.` |
| Trẻ hóa da | `/wizard Trẻ Hóa Da — trẻ hóa công nghệ cao. Hỏi dẫn giúp tôi, mỗi vòng tối đa 3 câu, có phương án chọn sẵn.` |
| Da liễu | `/wizard Da Liễu — trị nám tàn nhang. Hỏi dẫn giúp tôi, mỗi vòng tối đa 3 câu, có phương án chọn sẵn.` |
| Trị sắc tố | `/wizard Trị Sắc Tố — xóa xăm. Hỏi dẫn giúp tôi, mỗi vòng tối đa 3 câu, có phương án chọn sẵn.` |
| Kangnam Clinic | `/wizard Kangnam Clinic — triệt lông. Hỏi dẫn giúp tôi, mỗi vòng tối đa 3 câu, có phương án chọn sẵn.` |
| Nha khoa | `/wizard Nha Khoa — bọc răng sứ. Hỏi dẫn giúp tôi, mỗi vòng tối đa 3 câu. Nhớ đổi thứ tự trust theo KF-13 mục 4.` |

Đổi tên dịch vụ con trong prompt cho khớp việc bạn đang làm — danh mục đầy đủ ở `KF-01` mục 5.

---

## C. Khi đã có sẵn một phần thông tin

```
/wizard [tên dịch vụ]

Tôi đã có sẵn:
- Kênh: [vd Facebook MOF, tệp retarget 7 ngày]
- Ad copy nguyên văn: "[chép đúng từng chữ]"
- Cơ sở: [vd 190 Trường Chinh, Hà Nội]

Chỉ hỏi tôi những ô còn thiếu, đừng hỏi lại ba ô trên.
Ô nào tôi không biết thì cho tôi chọn "để agent chọn".
```

---

## D. Ba vòng agent sẽ hỏi — biết trước để chuẩn bị

| Vòng | Khoá cái gì | Ba câu |
|---|---|---|
| **1** | Khung trang | ① dịch vụ cụ thể trong nhóm · ② kênh & vị trí · ③ **ad copy / keyword nguyên văn** |
| **2** | Người đọc trang | ④ chân dung (6 nhóm `KF-12`) · ⑤ nhiệt độ + mức nhận thức · ⑥ cơ sở + tuyến |
| **3** | Vật liệu đang có | ⑦ CTA mục tiêu · ⑧ offer · ⑨ bác sĩ / ảnh case / bảng giá đã có chưa |

**Ô quan trọng nhất là ③.** Chép ad copy hoặc keyword **đúng từng chữ**, kể cả lỗi chính tả — đó là thứ khoá message-match, và là tiêu chí 20 điểm của scorecard.

**Agent sẽ dừng giữa chừng trong hai trường hợp:**
- Dịch vụ **đại phẫu** mà cơ sở bạn khai **không phải tuyến bệnh viện** → dừng ngay ở vòng 2, nêu hai cách xử lý R3 trước khi hỏi tiếp.
- Bạn khai tên bác sĩ **không có trong danh sách live** → dừng, không ghi tên đó vào brief.

---

## E. Câu trả lời nhanh khi đang trong vòng hỏi

| Muốn gì | Gõ |
|---|---|
| Để agent tự chọn ô này | `để agent chọn` |
| Bỏ qua, điền sau | `để trống, tôi bổ sung sau` |
| Xem lại những gì đã chốt | `tóm lại tôi đã chốt gì rồi?` |
| Sửa một ô đã chốt | `sửa ô [số]: [giá trị mới]` |
| Dừng hỏi, chạy luôn với giả định | `đủ rồi, cứ làm — ghi rõ GIẢ ĐỊNH ở đầu` |
| Hỏi vì sao cần ô này | `vì sao ô này quan trọng?` |
