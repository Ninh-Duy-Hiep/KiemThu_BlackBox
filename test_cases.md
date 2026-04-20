# Danh Sách Test Case - Kiểm Thử Hộp Đen (Black-Box Testing)

## Kỹ thuật áp dụng

- **Phân lớp tương đương (Equivalence Partitioning):** Chia đầu vào thành các lớp hợp lệ và không hợp lệ.
- **Phân tích giá trị biên (Boundary Value Analysis):** Kiểm tra giá trị tại ranh giới của mỗi lớp.
- **Dữ liệu không hợp lệ & ngoại lệ:** Kiểu sai, None, chuỗi ký tự.

---

## Bài 1: Chu Vi Hình Chữ Nhật

| TC   | Loại              | a     | b    | Kết quả mong đợi |
| ---- | ----------------- | ----- | ---- | ---------------- |
| TC01 | Hợp lệ            | 5     | 3    | 16               |
| TC02 | Hợp lệ            | 1     | 1    | 4                |
| TC03 | Biên hợp lệ       | 0.1   | 0.1  | 0.4              |
| TC04 | Hợp lệ            | 10    | 5    | 30               |
| TC05 | Không hợp lệ      | -1    | 3    | ValueError       |
| TC06 | Biên không hợp lệ | 0     | 5    | ValueError       |
| TC07 | Ngoại lệ          | "abc" | 3    | TypeError        |
| TC08 | Ngoại lệ          | 5     | None | TypeError        |

---

## Bài 2: Diện Tích Hình Chữ Nhật

| TC   | Loại              | a     | b   | Kết quả mong đợi |
| ---- | ----------------- | ----- | --- | ---------------- |
| TC01 | Hợp lệ            | 5     | 3   | 15               |
| TC02 | Hợp lệ            | 2.5   | 4   | 10.0             |
| TC03 | Biên hợp lệ       | 0.001 | 100 | 0.1              |
| TC04 | Hợp lệ            | 7     | 7   | 49               |
| TC05 | Không hợp lệ      | -2    | 5   | ValueError       |
| TC06 | Biên không hợp lệ | 4     | 0   | ValueError       |
| TC07 | Ngoại lệ          | None  | 5   | TypeError        |
| TC08 | Ngoại lệ          | 3     | "x" | TypeError        |

---

## Bài 3: Giải Phương Trình Bậc 2 (ax² + bx + c = 0)

| TC   | Loại                     | a   | b   | c   | Kết quả mong đợi            |
| ---- | ------------------------ | --- | --- | --- | --------------------------- |
| TC01 | Hợp lệ (Δ > 0)           | 1   | -5  | 6   | x1 = 3.0, x2 = 2.0          |
| TC02 | Hợp lệ (Δ = 0)           | 1   | -2  | 1   | Nghiệm kép: x = 1.0         |
| TC03 | Hợp lệ (Δ < 0)           | 1   | 2   | 5   | Vô nghiệm (delta < 0)       |
| TC04 | Biên: a=0, bậc 1         | 0   | 2   | -4  | Phương trình bậc 1, x = 2.0 |
| TC05 | Không hợp lệ: a=b=0, c≠0 | 0   | 0   | 5   | Vô nghiệm                   |
| TC06 | Không hợp lệ: a=b=c=0    | 0   | 0   | 0   | Vô số nghiệm                |
| TC07 | Ngoại lệ                 | "x" | 1   | 0   | TypeError                   |

---

## Bài 4: Số Ngày Trong Tháng

| TC   | Loại                 | Tháng | Năm  | Kết quả mong đợi |
| ---- | -------------------- | ----- | ---- | ---------------- |
| TC01 | Hợp lệ (31 ngày)     | 1     | 2024 | 31               |
| TC02 | Hợp lệ (30 ngày)     | 4     | 2024 | 30               |
| TC03 | Hợp lệ (năm nhuận)   | 2     | 2024 | 29               |
| TC04 | Hợp lệ (không nhuận) | 2     | 2023 | 28               |
| TC05 | Biên hợp lệ          | 12    | 2024 | 31               |
| TC06 | Biên không hợp lệ    | 0     | 2024 | ValueError       |
| TC07 | Biên không hợp lệ    | 13    | 2024 | ValueError       |
| TC08 | Không hợp lệ         | 1     | 0    | ValueError       |
| TC09 | Ngoại lệ             | "abc" | 2024 | TypeError        |

---

## Bài 5: Kiểm Tra Số Nguyên Tố

| TC   | Loại            | n   | Kết quả mong đợi |
| ---- | --------------- | --- | ---------------- |
| TC01 | Hợp lệ (NT)     | 2   | True             |
| TC02 | Hợp lệ (NT lớn) | 17  | True             |
| TC03 | Hợp lệ (hợp số) | 4   | False            |
| TC04 | Hợp lệ (NT lớn) | 97  | True             |
| TC05 | Biên: n=1       | 1   | False            |
| TC06 | Biên: n=0       | 0   | False            |
| TC07 | Không hợp lệ    | -5  | ValueError       |
| TC08 | Ngoại lệ        | 3.5 | TypeError        |

---

## Bài 6: Tổng S = 1 - 2 + 3 - 4 + ... + n

| TC   | Loại              | n     | Kết quả mong đợi |
| ---- | ----------------- | ----- | ---------------- |
| TC01 | Hợp lệ            | 1     | 1                |
| TC02 | Hợp lệ (chẵn)     | 4     | -2               |
| TC03 | Hợp lệ (lẻ)       | 5     | 3                |
| TC04 | Hợp lệ            | 10    | -5               |
| TC05 | Biên không hợp lệ | 0     | ValueError       |
| TC06 | Không hợp lệ      | -3    | ValueError       |
| TC07 | Ngoại lệ          | "abc" | TypeError        |

---

## Bài 7: Tìm ƯCLN

| TC   | Loại         | a   | b   | Kết quả mong đợi |
| ---- | ------------ | --- | --- | ---------------- |
| TC01 | Hợp lệ       | 12  | 8   | 4                |
| TC02 | Hợp lệ (NT)  | 7   | 5   | 1                |
| TC03 | Hợp lệ       | 100 | 25  | 25               |
| TC04 | Hợp lệ       | 36  | 48  | 12               |
| TC05 | Biên: a=b=1  | 1   | 1   | 1                |
| TC06 | Biên: a=0    | 0   | 5   | 5                |
| TC07 | Không hợp lệ | -4  | 8   | ValueError       |
| TC08 | Không hợp lệ | 0   | 0   | ValueError       |
| TC09 | Ngoại lệ     | "a" | 5   | TypeError        |

---

## Bài 8: Tổng S = 1! + 2! + ... + n!

| TC   | Loại              | n   | Kết quả mong đợi |
| ---- | ----------------- | --- | ---------------- |
| TC01 | Hợp lệ            | 1   | 1                |
| TC02 | Hợp lệ            | 3   | 9 (1+2+6)        |
| TC03 | Hợp lệ            | 5   | 153              |
| TC04 | Hợp lệ            | 4   | 33               |
| TC05 | Biên không hợp lệ | 0   | ValueError       |
| TC06 | Không hợp lệ      | -1  | ValueError       |
| TC07 | Ngoại lệ          | 2.5 | TypeError        |
| TC08 | Ngoại lệ          | "a" | TypeError        |
