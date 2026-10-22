# 01 — CÀI ĐẶT AGENT (15 phút)

Agent này là **prompt + knowledge**, không phải software. Cài = tạo một project trên nền tảng AI, dán bộ não vào ô instructions, nạp 8 file knowledge. Không cần cài gì lên máy.

---

## A. Claude Project (khuyến nghị — ô instructions không giới hạn 8.000 ký tự)

1. Vào [claude.ai](https://claude.ai) → **Projects** → **Create project**.
2. Tên project: `Agent-LDP-Kangnam`.
3. Mở [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) → copy **toàn bộ khối giữa hai vạch ▼▲** → dán vào **Custom instructions** của project.
4. Vào **Project knowledge** → upload **đủ 8 file** trong [`knowledge/`](../knowledge/):

```
KF-01-ho-so-thuong-hieu.md      thương hiệu · bác sĩ · cơ sở + tuyến
KF-09-design-system.md          token · typography · khung trang · form
KF-11-cong-phap-ly.md           cổng pháp lý + rào R0–R12   ← quan trọng nhất
KF-12-hanh-vi-khach-hang.md     hành vi khách               ← lõi của agent
KF-13-noi-so-phan-doi.md        nỗi sợ & phản đối theo BL
KF-14-proof-bank.md             bằng chứng được phép dùng
KF-15-block-library.md          thư viện khối landing
KF-16-performance-log.md        vòng học
```

5. Upload thêm (không bắt buộc nhưng rất nên):
   - [`template/lp-skeleton.html`](../template/lp-skeleton.html) — để `/prototype` dựng đúng khung ngay lần đầu.
6. Mở chat mới trong project → gõ `/brief` để kiểm agent đã nạp tri thức chưa.

**Kiểm nhanh agent đã cài đúng:**
> Gõ: *"Dựng landing nâng ngực cho cơ sở Đà Nẵng."*
> Agent **phải** chặn lại và nói Đà Nẵng là viện thẩm mỹ, không được mời đại phẫu.
> Nếu nó vui vẻ dựng trang → knowledge chưa nạp, hoặc instructions dán thiếu.

---

## B. ChatGPT Custom GPT

Ô Instructions của Custom GPT giới hạn **8.000 ký tự** → dùng bản ngắn.

1. ChatGPT → **Explore GPTs** → **Create**.
2. Tab **Configure**:
   - Name: `Agent-LDP-Kangnam`
   - Instructions: copy khối ▼▲ của [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) (7.989 ký tự).
   - **Knowledge:** upload đủ 8 file `knowledge/` + `template/lp-skeleton.html`.
3. Tắt **Web Browsing** nếu không cần; bật nếu muốn agent tự lấy giá động từ `/bang-gia/`.

> ⚠️ Bản ngắn đã cắt ma trận kênh, bảng thứ tự trust và nhiều luật chi tiết — nó **trông vào knowledge để bù**. Không nạp knowledge thì bản ngắn sẽ bắt đầu đoán, và đoán sai ở chỗ pháp lý.

---

## C. Gemini (Gems)

1. Gemini → **Gems** → **New Gem**.
2. Dán khối ▼▲ của `SYSTEM-PROMPT.md` vào ô **Chỉ dẫn**.
3. Upload 8 file knowledge vào phần tệp của Gem.

---

### Đường dự phòng — upload 1 file thay cho 8 file

Nền tảng chặn số file (**Gemini Gems trần 10 file**) hoặc upload nhiều file một lượt bị lỗi thì dùng bản gộp trong [`goi/`](../goi/):

| File gộp | Cỡ | Thay cho |
|---|---|---|
| [`goi/GOP-tri-thuc.md`](../goi/GOP-tri-thuc.md) | 101 KB | **8 file** `knowledge/` |

Nội dung **giống hệt bản rời** — mỗi phần mở đầu bằng dòng `===== tên file =====` nên Agent vẫn đọc đúng từng module, và tham chiếu chéo `[[tên-file]]` vẫn trỏ đúng.

> ⚠ **Đánh đổi phải biết trước:** dùng bản gộp thì **mất khả năng thay riêng một module** — sửa một file là phải sinh lại và upload lại cả bản gộp. **Bản rời vẫn là đường chính**; bản gộp chỉ để chữa cháy khi chạm trần số file.
>
> Sinh lại sau khi sửa tri thức: `python tools/gop-tham-khao.py`. ⛔ Không sửa tay file trong `goi/`.

---

## D. Dùng ngay trong Claude Code / VS Code (không tạo project)

Mở thư mục `Agent-LDP-Kangnam/` rồi nói:

```
Đọc SYSTEM-PROMPT.md và toàn bộ knowledge/, sau đó hành xử đúng như Agent-LDP-Kangnam.
Chạy /landing với brief sau: …
```

Cách này tiện khi cần dựng file HTML và lưu thẳng vào `out/`.

---

## E. Trước khi dùng thật — ba việc phải làm

| # | Việc | Vì sao |
|---|---|---|
| 1 | Chạy `python tools/fetch-du-lieu.py` để **chụp lại dữ liệu live** và so với `KF-01` mục 2, 4, 5 | Bác sĩ, cơ sở, dịch vụ đổi theo thời gian; bản trong file là bản chụp **2026-10-16** |
| 2 | Đọc `KF-14` mục 9 và **bắt đầu từ mục 1** — nạp case lên `/case-thuc-te/` (trang đang trống) | Đang chặn màn 5 của **mọi** landing |
| 3 | Chốt **bảng màu** dùng cho landing: production `#074E84/#EF6103` (mặc định) hay bảng của spec gốc | Trộn hai bảng làm trang mới lệch trang đang chạy |

Danh sách đủ ở *Việc còn treo* trong [`CHANGELOG.md`](CHANGELOG.md). Agent vẫn chạy được khi chưa xong, nhưng sẽ trả về nhiều `[CHỜ CẬP NHẬT]` hơn cần thiết.

---

## F. Chụp lại dữ liệu live

Năm nguồn chính thống (bác sĩ · dịch vụ · cơ sở · case · ảnh trước–sau) đổi theo thời gian. Script chụp lại và chỉ ra chỗ lệch:

```bash
python tools/fetch-du-lieu.py              # in tóm tắt ra màn hình
python tools/fetch-du-lieu.py --out out/   # ghi thêm snapshot JSON
python tools/fetch-du-lieu.py --chi bac_si co_so   # chỉ lấy vài nguồn
```

Script in ra: tổng số bác sĩ · **ai thiếu CCHN** · **ai chưa `verified`** · số bác sĩ theo từng nhóm chuyên khoa · số cơ sở trên trang · `/case-thuc-te/` còn trống hay không · số nhóm ảnh trước–sau.

> Script **không tự sửa file knowledge**. Mỗi thay đổi về bác sĩ, cơ sở, case đều chạm rào pháp lý (R3, R4, R5) nên phải có người đối chiếu rồi cập nhật `KF-01` / `KF-14` bằng tay, kèm một dòng vào `CHANGELOG.md`.

**Dấu hiệu phải cập nhật ngay:**
- Script báo `khong tim thay kn-doctors-data` → markup trang đội ngũ đã đổi, phải xem lại cách lấy danh sách bác sĩ.
- Số bác sĩ, số cơ sở khác bản trong `KF-01` → site mới hơn, **tin site**.
- Một bác sĩ đang dùng trên landing biến mất khỏi danh sách → **gỡ khỏi trang đang chạy**, không chờ.

---

## G. Cập nhật agent về sau

| Muốn đổi | Sửa file |
|---|---|
| Dữ liệu thương hiệu, bác sĩ, cơ sở | `knowledge/KF-01-ho-so-thuong-hieu.md` |
| Luật pháp lý, rào R | `knowledge/KF-11-cong-phap-ly.md` |
| Token màu, khung trang, form | `knowledge/KF-09-design-system.md` |
| Thêm nỗi sợ / câu trả lời mới | `knowledge/KF-13-noi-so-phan-doi.md` |
| Thêm case / bằng chứng đã duyệt | `knowledge/KF-14-proof-bank.md` |
| Ghi kết quả chạy thật | `knowledge/KF-16-performance-log.md` |
| **Quy trình, scorecard, lệnh** | `SYSTEM-PROMPT.md` **và** `SYSTEM-PROMPT-NGAN.md` (sửa cả hai) |

**Luật:** sửa dữ liệu → sửa file knowledge, **không sửa bộ não**. Sau mỗi lần sửa, upload lại file đó vào project và ghi một dòng vào `CHANGELOG.md`.

**Đổi sang thương hiệu khác:** thay `KF-01` + `KF-11` + `KF-09`, giữ nguyên `SYSTEM-PROMPT.md` và `KF-12`/`KF-15` (hành vi và khung khối gần như dùng chung được cho ngành thẩm mỹ). Nhớ sửa luôn `PAGES` và các hàm `parse_*` trong `tools/fetch-du-lieu.py` cho khớp site mới.
