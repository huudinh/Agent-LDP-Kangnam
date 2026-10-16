# PROMPT MẪU — `/audit` (chấm landing đang chạy)

Dùng khi đã có một landing và muốn biết **nó mất lead ở đâu**, không phải muốn biết nó có đẹp không.

---

## A. Audit một URL

```
/audit [URL]

BỐI CẢNH (quan trọng — thiếu cái này thì chỉ chấm được phần kỹ thuật)
- Kênh đang đổ vào: [vd FB MOF — tệp retarget 7 ngày]
- Ad copy / keyword nguyên văn: "[chép đúng]"
- Nhiệt độ tệp: [Lạnh / Ấm / Nóng / Khách hiện hữu]
- Số đang có (nếu có): CVR [..]% · tỉ lệ kết nối [..]% · booking [..]% · show-up [..]%

YÊU CẦU
1. Chấm scorecard theo 6 tiêu chí + cổng pháp lý. Nêu điểm từng tiêu chí.
2. Liệt kê lỗi theo 3 mức: CHẶN (pháp lý / mất lead ngay) · NẶNG · NÊN SỬA.
3. Chỉ rõ lỗi nào đang làm mất lead ở ĐOẠN NÀO (visit→lead, lead→kết nối, lead→booking).
4. Viết lại phần yếu nhất — viết thật, không gợi ý chung chung.
5. Nếu cổng pháp lý fail: nói ngay ở đầu, không chấm tiếp phần còn lại.
```

---

## B. Audit khi chỉ có nội dung (chưa có URL)

```
/audit

Đây là nội dung landing đang dùng:
---
[dán toàn bộ copy theo thứ tự màn, hoặc dán HTML]
---
Kênh: [..] · Keyword/ad nguyên văn: "[..]" · Nhiệt độ: [..]
Chấm theo scorecard và viết lại phần yếu nhất.
```

---

## C. Audit chuyên sâu theo một trục

| Trục cần soi | Prompt |
|---|---|
| Message-match | `/audit [URL] — chỉ soi tiêu chí message-match 20 điểm. Ad copy: "[..]". Chỉ ra 3 chỗ lệch giữa ad và màn 1.` |
| Hành vi & rào cản | `/audit [URL] — trang này đang gỡ rào cản nào, và chân dung của tôi (nhóm [số] KF-12) đang vướng rào cản nào? Chỉ ra chỗ lệch.` |
| CTA | `/audit [URL] — mỗi CTA trên trang có trả lời đủ 4 câu hỏi không? Lập bảng CTA × 4 câu hỏi, ô nào thiếu thì điền câu tôi nên viết.` |
| Mobile | `/audit [URL] — chỉ chạy checklist mobile-first §8, nói rõ ô nào fail và sửa thế nào.` |
| Pháp lý | `/audit [URL] — chỉ chạy cổng pháp lý KF-11 mục 6. Liệt kê theo mã rào R, ghi rõ ai phải duyệt.` |
| Lead chất lượng kém | `/audit [URL] — CVR ổn (4%) nhưng tỉ lệ kết nối chỉ 40%. Soi riêng: form, microcopy, mục "bấm xong thì sao", và thank-you page.` |

---

## D. Bốn triệu chứng → soi ở đâu trước

| Triệu chứng | Nghi phạm số 1 | Soi mục nào |
|---|---|---|
| CTR ad tốt, không ai điền form | **Sai message-match** hoặc sai kiểu landing so với nhiệt độ | Màn 1 · ma trận kênh `KF-12` |
| Lead nhiều, không ai bắt máy | CTA thiếu câu **"bấm xong thì sao"** | `§7.1` · thank-you page |
| Lead bắt máy nhưng không booking | Gỡ **sai rào cản** của chân dung | `KF-13` · thứ tự trust theo BL |
| Booking nhiều, show-up thấp | Trang **hứa khác** thứ khách nhận được | Màn 7 (giá/offer) · mục "được gì" của CTA |

Đưa luôn triệu chứng vào prompt — agent sẽ soi đúng chỗ thay vì chấm dàn đều.

---

## E. Lưu kết quả vào vòng học

Sau mỗi lần audit, thêm một dòng vào `knowledge/KF-16-performance-log.md` mục 6:
**ngày · landing · điểm scorecard · lỗi nặng nhất · đã sửa chưa**. Không ghi lại thì lần sau audit lại từ đầu.
