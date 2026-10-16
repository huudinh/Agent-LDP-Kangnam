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
