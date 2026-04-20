from bai_tap import (
    chu_vi_hinh_chu_nhat, dien_tich_hinh_chu_nhat,
    giai_phuong_trinh_bac2, so_ngay_trong_thang,
    la_so_nguyen_to, tinh_tong_xen_ke, ucln, tong_giai_thua,
)

PASS = "PASS"
FAIL = "FAIL"
results = []


def run_test(bai, ma_tc, mo_ta, func, args, ket_qua_mong_doi):
    try:
        actual = func(*args)
        if isinstance(ket_qua_mong_doi, float) or isinstance(actual, float):
            status = PASS if abs(actual - ket_qua_mong_doi) < 1e-9 else FAIL
        else:
            status = PASS if actual == ket_qua_mong_doi else FAIL
        note = f"Actual: {actual}"
    except Exception as e:
        status = FAIL
        note = f"Exception không mong đợi: {type(e).__name__}: {e}"

    results.append({"Bài": bai, "TC": ma_tc, "Mô tả": mo_ta,
                    "Trạng thái": status, "Ghi chú": note})
    print(f"[{status}] {bai} - {ma_tc}: {mo_ta} | {note}")


print("=" * 60)
print("BÀI 1: Chu vi hình chữ nhật - Dữ liệu hợp lệ")
print("=" * 60)
run_test("Bài 1", "TC01", "a=5, b=3 → 16",          chu_vi_hinh_chu_nhat, (5, 3),     16)
run_test("Bài 1", "TC02", "a=1, b=1 → 4 (giá trị nhỏ)", chu_vi_hinh_chu_nhat, (1, 1), 4)
run_test("Bài 1", "TC03", "a=0.1, b=0.1 → 0.4 (biên dưới hợp lệ)", chu_vi_hinh_chu_nhat, (0.1, 0.1), 0.4)
run_test("Bài 1", "TC04", "a=10, b=5 → 30 (giá trị lớn)", chu_vi_hinh_chu_nhat, (10, 5), 30)

print("\n" + "=" * 60)
print("BÀI 2: Diện tích hình chữ nhật - Dữ liệu hợp lệ")
print("=" * 60)
run_test("Bài 2", "TC01", "a=5, b=3 → 15",           dien_tich_hinh_chu_nhat, (5, 3),      15)
run_test("Bài 2", "TC02", "a=2.5, b=4 → 10.0 (số thực)", dien_tich_hinh_chu_nhat, (2.5, 4), 10.0)
run_test("Bài 2", "TC03", "a=0.001, b=100 → 0.1 (biên dưới hợp lệ)", dien_tich_hinh_chu_nhat, (0.001, 100), 0.1)
run_test("Bài 2", "TC04", "a=7, b=7 → 49 (hình vuông)",  dien_tich_hinh_chu_nhat, (7, 7),    49)

print("\n" + "=" * 60)
print("BÀI 3: Giải phương trình bậc 2 - Dữ liệu hợp lệ")
print("=" * 60)
run_test("Bài 3", "TC01", "Δ>0: a=1,b=-5,c=6 → 2 nghiệm phân biệt",
         giai_phuong_trinh_bac2, (1, -5, 6),
         "Phương trình có 2 nghiệm phân biệt: x1 = 3.0, x2 = 2.0")
run_test("Bài 3", "TC02", "Δ=0: a=1,b=-2,c=1 → nghiệm kép",
         giai_phuong_trinh_bac2, (1, -2, 1),
         "Phương trình có nghiệm kép: x = 1.0")
run_test("Bài 3", "TC03", "Δ<0: a=1,b=2,c=5 → vô nghiệm thực",
         giai_phuong_trinh_bac2, (1, 2, 5),
         "Phương trình vô nghiệm (delta < 0).")
run_test("Bài 3", "TC04", "a=0,b=2,c=-4 → phương trình bậc 1",
         giai_phuong_trinh_bac2, (0, 2, -4),
         "Phương trình bậc 1, nghiệm duy nhất: x = 2.0")

print("\n" + "=" * 60)
print("BÀI 4: Số ngày trong tháng - Dữ liệu hợp lệ")
print("=" * 60)
run_test("Bài 4", "TC01", "T1/2024 → 31 (tháng có 31 ngày)",  so_ngay_trong_thang, (1, 2024),  31)
run_test("Bài 4", "TC02", "T4/2024 → 30 (tháng có 30 ngày)",  so_ngay_trong_thang, (4, 2024),  30)
run_test("Bài 4", "TC03", "T2/2024 → 29 (năm nhuận)",          so_ngay_trong_thang, (2, 2024),  29)
run_test("Bài 4", "TC04", "T2/2023 → 28 (không nhuận)",        so_ngay_trong_thang, (2, 2023),  28)
run_test("Bài 4", "TC05", "T12/2024 → 31 (tháng biên trên)",   so_ngay_trong_thang, (12, 2024), 31)
run_test("Bài 4", "TC06", "T1/2024 → 31 (tháng biên dưới)",    so_ngay_trong_thang, (1, 2024),  31)

print("\n" + "=" * 60)
print("BÀI 5: Kiểm tra số nguyên tố - Dữ liệu hợp lệ")
print("=" * 60)
run_test("Bài 5", "TC01", "n=2 → True (SNT nhỏ nhất)",       la_so_nguyen_to, (2,),  True)
run_test("Bài 5", "TC02", "n=17 → True (SNT)",               la_so_nguyen_to, (17,), True)
run_test("Bài 5", "TC03", "n=4 → False (hợp số)",            la_so_nguyen_to, (4,),  False)
run_test("Bài 5", "TC04", "n=97 → True (SNT lớn)",           la_so_nguyen_to, (97,), True)
run_test("Bài 5", "TC05", "n=1 → False (biên, không là SNT)", la_so_nguyen_to, (1,),  False)
run_test("Bài 5", "TC06", "n=0 → False (biên, không là SNT)", la_so_nguyen_to, (0,),  False)

print("\n" + "=" * 60)
print("BÀI 6: Tổng xen kẽ - Dữ liệu hợp lệ")
print("=" * 60)
run_test("Bài 6", "TC01", "n=1 → 1 (biên dưới hợp lệ)",   tinh_tong_xen_ke, (1,),  1)
run_test("Bài 6", "TC02", "n=4 → -2 (n chẵn)",             tinh_tong_xen_ke, (4,),  -2)
run_test("Bài 6", "TC03", "n=5 → 3 (n lẻ)",                tinh_tong_xen_ke, (5,),  3)
run_test("Bài 6", "TC04", "n=10 → -5",                     tinh_tong_xen_ke, (10,), -5)

print("\n" + "=" * 60)
print("BÀI 7: ƯCLN - Dữ liệu hợp lệ")
print("=" * 60)
run_test("Bài 7", "TC01", "a=12, b=8 → 4",        ucln, (12, 8),   4)
run_test("Bài 7", "TC02", "a=7, b=5 → 1 (NT)",    ucln, (7, 5),    1)
run_test("Bài 7", "TC03", "a=100, b=25 → 25",      ucln, (100, 25), 25)
run_test("Bài 7", "TC04", "a=36, b=48 → 12",       ucln, (36, 48),  12)
run_test("Bài 7", "TC05", "a=1, b=1 → 1 (biên)",   ucln, (1, 1),    1)
run_test("Bài 7", "TC06", "a=0, b=5 → 5 (biên 0)", ucln, (0, 5),    5)

print("\n" + "=" * 60)
print("BÀI 8: Tổng giai thừa - Dữ liệu hợp lệ")
print("=" * 60)
run_test("Bài 8", "TC01", "n=1 → 1 (biên dưới hợp lệ)", tong_giai_thua, (1,), 1)
run_test("Bài 8", "TC02", "n=3 → 9 (1!+2!+3!)",         tong_giai_thua, (3,), 9)
run_test("Bài 8", "TC03", "n=5 → 153",                   tong_giai_thua, (5,), 153)
run_test("Bài 8", "TC04", "n=4 → 33",                    tong_giai_thua, (4,), 33)

print("\n" + "=" * 60)
print("TỔNG KẾT - ISSUE #1: Dữ liệu hợp lệ")
print("=" * 60)
total = len(results)
passed = sum(1 for r in results if r["Trạng thái"] == PASS)
print(f"Tổng: {total} | PASS: {passed} | FAIL: {total - passed} | Tỉ lệ: {passed/total*100:.1f}%")
