# 04 — DÀNH CHO NGƯỜI MỚI (chưa từng dùng agent nào)

Không cần đọc 8 file knowledge. Đọc trang này là dùng được.

---

## 1. Agent này làm gì cho bạn

Nó làm **landing page cho một chiến dịch cụ thể** của Kangnam: viết copy từng màn, chọn bố cục, viết CTA và form, chấm điểm trang, và dựng file HTML nếu bạn cần.

**Nó không làm:** chạy quảng cáo · publish trang · duyệt pháp chế · viết bài SEO · tư vấn khách.

**Điều quan trọng nhất cần biết:** nó được thiết kế để **không bịa**. Thiếu giá, thiếu tên bác sĩ, thiếu case thì nó ghi `[CHỜ CẬP NHẬT]` chứ không điền bừa. Thấy nhiều `[CHỜ CẬP NHẬT]` trong output nghĩa là nó đang làm đúng, và đó là danh sách việc bạn cần đi lấy.

---

## 2. Chuẩn bị 4 thứ trước khi mở chat

| # | Cần gì | Ví dụ | Vì sao |
|---|---|---|---|
| 1 | **Mẫu quảng cáo hoặc từ khoá, chép nguyên văn** | `"nâng mũi bao nhiêu tiền"` | Khách bấm vào trang vì câu này. Màn đầu phải nhắc lại nó |
| 2 | **Kênh nào đổ vào** | Google Search / FB MOF / ZNS | Quyết định trang dài hay ngắn |
| 3 | **Dịch vụ + cơ sở** | Nâng mũi cấu trúc — 190 Trường Chinh HN | Quyết định được quảng cáo gì (luật tuyến cơ sở) |
| 4 | **Bạn muốn khách làm gì** | Đặt lịch / chat Zalo / gửi ảnh | Quyết định nút chính |

Thiếu cái nào agent cũng hỏi lại, nhưng chuẩn bị trước thì xong trong một lượt.

---

## 3. Câu lệnh đầu tiên — copy nguyên khối này

```
/landing

Kênh: [vd Google Search]
Keyword/ad nguyên văn: "[chép đúng từng chữ]"
Dịch vụ: [vd nâng mũi cấu trúc]
Cơ sở: [vd 190 Trường Chinh, Hà Nội]
Khách: [vd nữ 25–35, công sở]
Tôi muốn khách: [vd đặt lịch khám]

Các trường còn lại cứ giả định hợp lý, nhưng ghi rõ GIẢ ĐỊNH ở đầu,
và để [CHỜ CẬP NHẬT] cho mọi thứ liên quan pháp lý.
```

Agent sẽ trả về 11 mục **A→K**. Xem mẫu đầy đủ ở [`03-output-mau.md`](03-output-mau.md).

---

## 4. Đọc output: ba mục quan trọng nhất

| Mục | Tên | Đọc để biết |
|---|---|---|
| **B** | Audience Card | Agent có hiểu đúng khách của bạn không. **Sai ở đây thì cả trang sai** — sửa ngay, đừng đọc tiếp |
| **I** | Kết quả cổng pháp lý | Trang có được phép chạy chưa, và còn thiếu gì |
| **J** | Scorecard | Trang đang yếu ở đâu. ≥80 là giao được *(với điều kiện mục I pass)* |

Ba mục còn lại đọc khi cần: **E** copy để duyệt nội dung · **D + G** cho designer · **H + K** cho đội media.

---

## 5. Bốn lần agent sẽ "cãi" bạn — và nó đúng

1. **"Đà Nẵng là viện tỉnh, không được mời nâng ngực."**
   → Đại phẫu chỉ làm ở tuyến bệnh viện (HN · TP.HCM). Đây là **phạm vi giấy phép**, không phải chuyện hiệu suất quảng cáo.
2. **"Không viết tên bác sĩ này vì chưa xác minh chuyên khoa."**
   → Gắn bác sĩ sai chuyên khoa là vi phạm. Thà để trống.
3. **"Không viết 'cam kết đẹp 100%' / 'không biến chứng' / '3 ngày đi làm được'."**
   → Những câu này bị cấm trong quảng cáo dịch vụ khám chữa bệnh.
4. **"Chưa có ad copy nguyên văn thì chưa dựng được màn 1."**
   → Không có câu khách vừa đọc thì không biết phải nhắc lại cái gì.

Gặp bốn tình huống này thì đi lấy dữ liệu, đừng ép agent bỏ qua.

---

## 6. Năm câu hỏi thường gặp

**Agent có tự lấy giá mới nhất không?**
Có nếu nền tảng bật được web (Claude/ChatGPT có browsing). Không thì nó để `[GIÁ ĐỘNG]` và bạn dán giá từ `/bang-gia/` vào. **Đừng để nó dùng giá cũ.**

**Nó dựng được file HTML chạy thật không?**
Được — gõ `/prototype`. File ra là **một file `.html` tự chứa**, mở bằng trình duyệt là xem được trên mobile. Nhưng còn ô ảnh tạm; phải thay ảnh thật trước khi publish.

**Tôi đã có landing rồi, dùng được không?**
Được, và đây thường là cách nhanh thấy kết quả nhất: gõ `/audit [URL]` kèm **triệu chứng** (vd *"CVR ổn nhưng không ai bắt máy"*). Xem [`02-cau-lenh.md`](02-cau-lenh.md) mục 3.

**Một trang chạy được nhiều kênh không?**
Không nên. Khách Google (đã sẵn sàng) và khách TikTok (đang lướt) cần hai trang khác nhau. Làm xong trang chính rồi gõ `/variant [kênh]`.

**Output có `[CHỜ CẬP NHẬT]` nhiều quá, agent kém à?**
Ngược lại. Mỗi `[CHỜ CẬP NHẬT]` là một chỗ nếu bịa thì có rủi ro. Danh sách đó chính là việc cần làm — ưu tiên theo `knowledge/KF-14-proof-bank.md` mục 8.

---

## 7. Sai lầm hay gặp nhất của người mới

| Sai | Hệ quả | Thay bằng |
|---|---|---|
| Diễn đạt lại ad copy cho "gọn" | Mất message-match — lỗi nặng nhất, 20 điểm | Chép **nguyên văn**, kể cả lỗi chính tả của ad |
| Nói "làm cho tôi một landing nâng mũi" | Agent không biết kênh, nhiệt độ → trang chung chung | Khai đủ 4 thứ ở mục 2 |
| Nhắm nhiều nhóm khách cùng một trang | Trang không nói với ai | Một trang một nhóm, phần còn lại dùng `/variant` |
| Bỏ qua mục B, đọc thẳng copy | Duyệt chữ đẹp cho một chân dung sai | Đọc **B trước E** |
| Publish luôn file `/prototype` | Placeholder nội bộ lộ ra trang thật | Thay ảnh + chạy checklist pháp lý trước |

---

## 8. Xong rồi làm gì

1. Publish → đo **4 chỉ số**: CVR · tỉ lệ lead kết nối · booking · show-up.
2. Sau 14 ngày, ghi một dòng vào `knowledge/KF-16-performance-log.md`.
3. Landing sau sẽ tốt hơn vì agent đọc được dòng đó.

Bước 2 là bước mọi người bỏ, và là bước duy nhất làm agent khá hơn theo thời gian.
