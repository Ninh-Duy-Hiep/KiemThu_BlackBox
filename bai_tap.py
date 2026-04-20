import math


# Bài 1: Tính chu vi hình chữ nhật
def chu_vi_hinh_chu_nhat(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("Chiều dài phải là số thực.")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Chiều rộng phải là số thực.")
    if a <= 0:
        raise ValueError("Chiều dài phải lớn hơn 0.")
    if b <= 0:
        raise ValueError("Chiều rộng phải lớn hơn 0.")
    return 2 * (a + b)


# Bài 2: Tính diện tích hình chữ nhật
def dien_tich_hinh_chu_nhat(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("Chiều dài phải là số thực.")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Chiều rộng phải là số thực.")
    if a <= 0:
        raise ValueError("Chiều dài phải lớn hơn 0.")
    if b <= 0:
        raise ValueError("Chiều rộng phải lớn hơn 0.")
    return a * b


# Bài 3: Giải phương trình bậc 2: ax² + bx + c = 0
def giai_phuong_trinh_bac2(a, b, c):
    for name, val in [("a", a), ("b", b), ("c", c)]:
        if not isinstance(val, (int, float)) or isinstance(val, bool):
            raise TypeError(f"Hệ số {name} phải là số thực.")

    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm."
            else:
                return "Phương trình vô nghiệm."
        else:
            x = -c / b
            return f"Phương trình bậc 1, nghiệm duy nhất: x = {x}"

    delta = b**2 - 4 * a * c

    if delta < 0:
        return "Phương trình vô nghiệm (delta < 0)."
    elif delta == 0:
        x = -b / (2 * a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"


# Bài 4: Tính số ngày của một tháng
def so_ngay_trong_thang(thang, nam):
    if not isinstance(thang, int) or isinstance(thang, bool):
        raise TypeError("Tháng phải là số nguyên.")
    if not isinstance(nam, int) or isinstance(nam, bool):
        raise TypeError("Năm phải là số nguyên.")
    if thang < 1 or thang > 12:
        raise ValueError("Tháng phải từ 1 đến 12.")
    if nam <= 0:
        raise ValueError("Năm phải lớn hơn 0.")

    # Kiểm tra năm nhuận
    la_nam_nhuan = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

    ngay_trong_thang = {
        1: 31, 2: 29 if la_nam_nhuan else 28, 3: 31,
        4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }
    return ngay_trong_thang[thang]


# Bài 5: Kiểm tra n có phải là số nguyên tố hay không
def la_so_nguyen_to(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n phải là số nguyên.")
    if n < 0:
        raise ValueError("n phải là số không âm.")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


# Bài 6: Tính tổng S = 1 - 2 + 3 - 4 + ... + n
def tinh_tong_xen_ke(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n phải là số nguyên.")
    if n < 1:
        raise ValueError("n phải lớn hơn hoặc bằng 1.")

    tong = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            tong += i
        else:
            tong -= i
    return tong


# Bài 7: Tìm ƯCLN của a và b
def ucln(a, b):
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("a phải là số nguyên.")
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("b phải là số nguyên.")
    if a < 0 or b < 0:
        raise ValueError("a và b phải là số không âm.")
    if a == 0 and b == 0:
        raise ValueError("Không xác định ƯCLN(0, 0).")

    while b != 0:
        a, b = b, a % b
    return a


# Bài 8: Tính S = 1! + 2! + 3! + ... + n!
def giai_thua(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n phải là số nguyên.")
    if n < 0:
        raise ValueError("n phải là số không âm.")
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)


def tong_giai_thua(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n phải là số nguyên.")
    if n < 1:
        raise ValueError("n phải lớn hơn hoặc bằng 1.")

    tong = 0
    for i in range(1, n + 1):
        tong += giai_thua(i)
    return tong


if __name__ == "__main__":
    print("=== Bài 1: Chu vi hình chữ nhật ===")
    print(chu_vi_hinh_chu_nhat(5, 3))

    print("\n=== Bài 2: Diện tích hình chữ nhật ===")
    print(dien_tich_hinh_chu_nhat(5, 3))

    print("\n=== Bài 3: Giải phương trình bậc 2 ===")
    print(giai_phuong_trinh_bac2(1, -5, 6))
    print(giai_phuong_trinh_bac2(1, -2, 1))
    print(giai_phuong_trinh_bac2(1, 2, 5))

    print("\n=== Bài 4: Số ngày trong tháng ===")
    print(so_ngay_trong_thang(2, 2024))
    print(so_ngay_trong_thang(2, 2023))

    print("\n=== Bài 5: Kiểm tra số nguyên tố ===")
    print(la_so_nguyen_to(17))
    print(la_so_nguyen_to(4))

    print("\n=== Bài 6: Tổng xen kẽ ===")
    print(tinh_tong_xen_ke(5))

    print("\n=== Bài 7: ƯCLN ===")
    print(ucln(12, 8))

    print("\n=== Bài 8: Tổng giai thừa ===")
    print(tong_giai_thua(3))
    print(tong_giai_thua(5))
