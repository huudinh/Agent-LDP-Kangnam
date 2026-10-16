# PROMPT MẪU — `/landing` (dựng landing trọn bộ)

Dán nguyên khối dưới vào chat với agent, điền phần trong `[ ]`. Thiếu trường có `*` thì agent sẽ hỏi lại (tối đa 3 câu) — điền trước cho nhanh.

---

## A. Bản đầy đủ (dùng khi đã có brief)

```
/landing

BRIEF
1* Kênh & vị trí: [vd Google Search – nhóm từ khoá giá; hoặc FB MOF – tệp LAL khách mũi]
2* Ad copy / keyword NGUYÊN VĂN: "[chép đúng từng chữ, không diễn đạt lại]"
3* Dịch vụ & BL: [vd Nâng mũi cấu trúc — KPS]
4* Đối tượng / tệp: [vd nữ 25–35, công sở, Hà Nội]
5* Nhiệt độ: [Lạnh / Ấm / Nóng / Khách hiện hữu]
6  Offer: [vd khám + hội chẩn miễn phí với bác sĩ chuyên khoa] (bỏ trống nếu chưa có)
7* CTA mục tiêu: [Đặt lịch / Chat Zalo / Gửi ảnh / Quiz]
8* Cơ sở áp dụng + tuyến: [vd 190 Trường Chinh HN — tuyến bệnh viện]
9  KPI: [vd CVR ≥ 4%, CPL ≤ xxx, booking rate ≥ 35%]

YÊU CẦU THÊM
- Xuất theo output chuẩn A→K.
- Chấm scorecard thật, nêu rõ chỗ nào đang yếu.
- Liệt kê đầy đủ [CHỜ CẬP NHẬT] / [PLACEHOLDER] ở mục I.
- Chưa dựng HTML. Hỏi tôi trước khi sang /prototype.
```

---

## B. Bản tối thiểu (khi chỉ có từ khoá hoặc mẫu quảng cáo)

```
/landing

Tôi có cụm từ khoá/mẫu ad này: "[chép nguyên văn]"
Dịch vụ: [tên dịch vụ]. Cơ sở: [tên cơ sở].
Các trường còn lại cứ giả định hợp lý, nhưng ghi rõ GIẢ ĐỊNH ở đầu output
và để [CHỜ CẬP NHẬT] cho mọi trường pháp lý.
```

---

## C. Bản cho landing local (có khách tỉnh) — nhớ khai cách xử lý tuyến

```
/landing

BRIEF
1* Kênh: Google Search local — [tên tỉnh]
2* Keyword nguyên văn: "[vd nâng ngực Đà Nẵng]"
3* Dịch vụ & BL: [dịch vụ đại phẫu] — KPS
4* Đối tượng: khách tại [tỉnh]
5* Nhiệt độ: Ấm
7* CTA mục tiêu: Đặt khám tại cơ sở địa phương
8* Cơ sở: [viện tỉnh] — KHÔNG có giấy phép đại phẫu
   → Xử lý theo cách ①: hero nói rõ "tư vấn/đặt khám tại [viện tỉnh],
     phẫu thuật tại [tuyến bệnh viện]".

Kiểm cổng R3 trước khi viết chữ nào. Nếu tôi khai sai tuyến, dừng và nói cho tôi biết.
```

---

## D. Prompt phụ — chạy sau khi đã có output A→K

| Mục đích | Prompt |
|---|---|
| Dựng file HTML | `/prototype — dùng output vừa rồi, theo KF-09, kèm bảng kê ảnh cần cấp.` |
| Siết riêng CTA | `/cta — form đang có 5 trường, rút còn 3 và viết lại microcopy + thank-you.` |
| Xin thêm phương án hero | `Viết thêm 3 headline màn 1 theo góc [Bác sĩ / Case / Nỗi sợ được trả lời], giữ nguyên message-match.` |
| Đổi chân dung | `Giữ nguyên dịch vụ và kênh, đổi chân dung sang nhóm [số] ở KF-12. Nói rõ cái gì phải đổi theo.` |
| Chuyển kênh | `/variant [kênh mới]` |
| Đề xuất test | `/ab — 3 giả thuyết, mỗi giả thuyết nêu chỉ số kết luận và thời hạn đánh giá.` |

---

## E. Ba câu để ép agent không lười

Dùng khi output có mùi chung chung:

1. *"Đổi tên Kangnam thành một phòng khám khác thì copy này còn đúng không? Nếu còn đúng thì viết lại."*
2. *"Mỗi khối trong bản đồ màn đang dùng bằng chứng nào trong KF-14? Liệt kê ra. Khối nào không có thì ghi placeholder."*
3. *"Màn 1 đang trả lời câu hỏi đầu tiên trong đầu khách ở ô ⑥ của Audience Card chưa? Dẫn chứng bằng chính câu đó."*
