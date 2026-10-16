# PROMPT MẪU — `/variant` (chuyển landing master sang kênh khác)

`/variant` **không phải** đổi màu và sửa headline. Đổi kênh = đổi **nhiệt độ** + **mức nhận thức** → đổi **độ dài trang**, **nấc CTA** và **thứ tự trust**. Nếu agent chỉ sửa chữ mà giữ nguyên bố cục, bắt nó làm lại.

---

## A. Prompt chuẩn

```
/variant [kênh mới]

LANDING MASTER
- Đang chạy cho kênh: [kênh cũ] · nhiệt độ [..] · dịch vụ [..]
- Output master: [dán lại bản đồ màn + copy, hoặc nói "dùng output ở trên"]

KÊNH MỚI
- Kênh & vị trí: [vd ZNS cho tệp CDP khách đã làm da > 6 tháng]
- Ad copy / tin nhắn nguyên văn ở kênh mới: "[chép đúng]"
- Nhiệt độ: [..]
- CTA mục tiêu: [..]

YÊU CẦU
1. Nói rõ ba thứ ĐỔI và lý do: độ dài trang · nấc CTA · thứ tự trust.
2. Khoá lại message-match mới (3 yếu tố của nội dung kênh mới).
3. Chỉ xuất phần KHÁC master, đừng chép lại phần giống.
4. Chấm lại scorecard cho biến thể.
```

---

## B. Bảng chuyển kênh — cái gì buộc phải đổi

| Chuyển | Đổi độ dài | Đổi nấc CTA | Đổi gì nữa |
|---|---|---|---|
| **FB TOF → Google Search** | 9 màn → 4–6 màn | Micro → Macro/gọi | Màn 1 phải **trả lời thẳng truy vấn** (giá / địa chỉ / bác sĩ), bỏ phần giáo dục |
| **Google Search → FB TOF** | ngắn → đủ 9 màn | Macro → Micro | Thêm màn 2–3 (vấn đề + quiz), thêm câu chuyện thật |
| **FB MOF → FB BOF** | TB → ngắn | Mid → Macro | Đẩy offer + bằng chứng lên trước, **khan hiếm phải thật** |
| **Bất kỳ → CDP/ZNS** | → 3–4 màn | → Macro | Nhận diện **mềm**; ⛔ không hiển thị lịch sử dịch vụ / sức khoẻ |
| **Bất kỳ → Việt kiều** | → 5 màn | → Mid (video call) | Thêm lịch trình về nước + tư vấn từ xa; kiểm R8 (4 điều kiện) |
| **Bản thường → bản local** | giữ | giữ | ⚠️ Kiểm **R3 tuyến cơ sở** trước mọi thứ khác; sửa footer + hero |

---

## C. Ba biến thể hay dùng nhất

### C1. Sang CDP / ZNS (khách hiện hữu)
```
/variant CDP-ZNS

Tệp: khách đã làm [dịch vụ cũ] cách đây > [n] tháng.
Tin ZNS nguyên văn: "[chép đúng]"
CTA: đặt lịch ưu tiên.

Luật phải tuân:
- Nhận diện MỀM ("ưu đãi dành riêng cho khách hàng thân thiết Kangnam").
- ⛔ Không nhắc tên dịch vụ khách đã làm, không nhắc tình trạng sức khoẻ.
- Trang 3–4 màn, vào thẳng quyền lợi + form.
```

### C2. Sang bản local của viện tỉnh
```
/variant local-[tỉnh]

Cơ sở: [viện tỉnh] — KHÔNG có giấy phép đại phẫu.
Chạy cổng R3 trước. Hero phải ghi rõ "tư vấn/đặt khám tại [viện tỉnh],
phẫu thuật tại [tuyến bệnh viện]". Footer chỉ liệt kê cơ sở đúng phạm vi.
Nếu dịch vụ này không được mời ở tuyến tỉnh, nói cho tôi biết và đề xuất
đưa cụm từ khoá vào phủ định thay vì dựng trang.
```

### C3. Sang chân dung khác (cùng kênh)
```
/variant giữ-kênh-đổi-chân-dung

Chân dung mới: nhóm [số] ở KF-12 ([tên nhóm]).
Nói rõ: nỗi sợ số 1 đổi thành gì · thứ tự trust đổi ra sao ·
giọng đổi thế nào · bằng chứng nào phải thay.
Giữ nguyên message-match nếu ad không đổi.
```

---

## D. Luật chống "biến thể giả"

Một biến thể chỉ được gọi là biến thể khi **ít nhất một** trong bốn thứ này đổi:
① số màn · ② nấc CTA · ③ thứ tự trust · ④ chân dung nhắm tới.

Chỉ đổi headline và ảnh → đó là **A/B test**, không phải biến thể kênh. Dùng `/ab` cho việc đó.
