"""
test_runner.py - Chạy test case kiểm thử hộp đen cho 8 bài toán Python
"""

from bai_tap import (
    chu_vi_hinh_chu_nhat,
    dien_tich_hinh_chu_nhat,
    giai_phuong_trinh_bac2,
    so_ngay_trong_thang,
    la_so_nguyen_to,
    tinh_tong_xen_ke,
    ucln,
    giai_thua,
    tong_giai_thua,
)

PASS = "PASS"
FAIL = "FAIL"
results = []


def run_test(bai, ma_tc, mo_ta, func, args, ket_qua_mong_doi, loai_exception=None):
    """
    Chạy một test case.
    - loai_exception: nếu mong đợi hàm ném ngoại lệ, truyền class ngoại lệ đó.
    """
    try:
        actual = func(*args)
        if loai_exception:
            status = FAIL
            note = f"Mong đợi {loai_exception.__name__} nhưng nhận được: {actual}"
        else:
            if isinstance(ket_qua_mong_doi, float) or isinstance(actual, float):
                status = PASS if abs(actual - ket_qua_mong_doi) < 1e-9 else FAIL
            else:
                status = PASS if actual == ket_qua_mong_doi else FAIL
            note = f"Actual: {actual}"
    except Exception as e:
        if loai_exception and isinstance(e, loai_exception):
            status = PASS
            note = f"Exception đúng: {type(e).__name__}: {e}"
        else:
            status = FAIL
            note = f"Exception không mong đợi: {type(e).__name__}: {e}"

    results.append({
        "Bài": bai,
        "TC": ma_tc,
        "Mô tả": mo_ta,
        "Trạng thái": status,
        "Ghi chú": note,
    })
    print(f"[{status}] {bai} - {ma_tc}: {mo_ta} | {note}")


# =============================================================================
# BÀI 1: Chu vi hình chữ nhật
# =============================================================================
print("\n" + "="*60)
print("BÀI 1: Chu vi hình chữ nhật")
print("="*60)

run_test("Bài 1", "TC01", "Hợp lệ: a=5, b=3 → 16",
         chu_vi_hinh_chu_nhat, (5, 3), 16)
run_test("Bài 1", "TC02", "Hợp lệ: a=1, b=1 → 4",
         chu_vi_hinh_chu_nhat, (1, 1), 4)
run_test("Bài 1", "TC03", "Biên hợp lệ: a=0.1, b=0.1 → 0.4",
         chu_vi_hinh_chu_nhat, (0.1, 0.1), 0.4)
run_test("Bài 1", "TC04", "Hợp lệ: a=10, b=5 → 30",
         chu_vi_hinh_chu_nhat, (10, 5), 30)
run_test("Bài 1", "TC05", "Không hợp lệ: a=-1 → ValueError",
         chu_vi_hinh_chu_nhat, (-1, 3), None, ValueError)
run_test("Bài 1", "TC06", "Không hợp lệ: a=0 → ValueError",
         chu_vi_hinh_chu_nhat, (0, 5), None, ValueError)
run_test("Bài 1", "TC07", "Ngoại lệ: a='abc' → TypeError",
         chu_vi_hinh_chu_nhat, ("abc", 3), None, TypeError)
run_test("Bài 1", "TC08", "Ngoại lệ: b=None → TypeError",
         chu_vi_hinh_chu_nhat, (5, None), None, TypeError)

# =============================================================================
# BÀI 2: Diện tích hình chữ nhật
# =============================================================================
print("\n" + "="*60)
print("BÀI 2: Diện tích hình chữ nhật")
print("="*60)

run_test("Bài 2", "TC01", "Hợp lệ: a=5, b=3 → 15",
         dien_tich_hinh_chu_nhat, (5, 3), 15)
run_test("Bài 2", "TC02", "Hợp lệ: a=2.5, b=4 → 10.0",
         dien_tich_hinh_chu_nhat, (2.5, 4), 10.0)
run_test("Bài 2", "TC03", "Biên hợp lệ: a=0.001, b=100 → 0.1",
         dien_tich_hinh_chu_nhat, (0.001, 100), 0.1)
run_test("Bài 2", "TC04", "Hợp lệ: a=7, b=7 → 49",
         dien_tich_hinh_chu_nhat, (7, 7), 49)
run_test("Bài 2", "TC05", "Không hợp lệ: a=-2 → ValueError",
         dien_tich_hinh_chu_nhat, (-2, 5), None, ValueError)
run_test("Bài 2", "TC06", "Không hợp lệ: b=0 → ValueError",
         dien_tich_hinh_chu_nhat, (4, 0), None, ValueError)
run_test("Bài 2", "TC07", "Ngoại lệ: a=None → TypeError",
         dien_tich_hinh_chu_nhat, (None, 5), None, TypeError)
run_test("Bài 2", "TC08", "Ngoại lệ: b='x' → TypeError",
         dien_tich_hinh_chu_nhat, (3, "x"), None, TypeError)

# =============================================================================
# BÀI 3: Giải phương trình bậc 2
# =============================================================================
print("\n" + "="*60)
print("BÀI 3: Giải phương trình bậc 2")
print("="*60)

run_test("Bài 3", "TC01", "Hợp lệ delta>0: a=1,b=-5,c=6 → 2 nghiệm",
         giai_phuong_trinh_bac2, (1, -5, 6), "Phương trình có 2 nghiệm phân biệt: x1 = 3.0, x2 = 2.0")
run_test("Bài 3", "TC02", "Hợp lệ delta=0: a=1,b=-2,c=1 → nghiệm kép",
         giai_phuong_trinh_bac2, (1, -2, 1), "Phương trình có nghiệm kép: x = 1.0")
run_test("Bài 3", "TC03", "Hợp lệ delta<0: a=1,b=2,c=5 → vô nghiệm",
         giai_phuong_trinh_bac2, (1, 2, 5), "Phương trình vô nghiệm (delta < 0).")
run_test("Bài 3", "TC04", "Biên: a=0,b=2,c=-4 → bậc 1",
         giai_phuong_trinh_bac2, (0, 2, -4), "Phương trình bậc 1, nghiệm duy nhất: x = 2.0")
run_test("Bài 3", "TC05", "Không hợp lệ: a=0,b=0,c=5 → vô nghiệm",
         giai_phuong_trinh_bac2, (0, 0, 5), "Phương trình vô nghiệm.")
run_test("Bài 3", "TC06", "Không hợp lệ: a=0,b=0,c=0 → vô số nghiệm",
         giai_phuong_trinh_bac2, (0, 0, 0), "Phương trình có vô số nghiệm.")
run_test("Bài 3", "TC07", "Ngoại lệ: a='x' → TypeError",
         giai_phuong_trinh_bac2, ("x", 1, 0), None, TypeError)

# =============================================================================
# BÀI 4: Số ngày trong tháng
# =============================================================================
print("\n" + "="*60)
print("BÀI 4: Số ngày trong tháng")
print("="*60)

run_test("Bài 4", "TC01", "Hợp lệ: tháng 1/2024 → 31",
         so_ngay_trong_thang, (1, 2024), 31)
run_test("Bài 4", "TC02", "Hợp lệ: tháng 4/2024 → 30",
         so_ngay_trong_thang, (4, 2024), 30)
run_test("Bài 4", "TC03", "Hợp lệ năm nhuận: tháng 2/2024 → 29",
         so_ngay_trong_thang, (2, 2024), 29)
run_test("Bài 4", "TC04", "Hợp lệ không nhuận: tháng 2/2023 → 28",
         so_ngay_trong_thang, (2, 2023), 28)
run_test("Bài 4", "TC05", "Biên: tháng 12/2024 → 31",
         so_ngay_trong_thang, (12, 2024), 31)
run_test("Bài 4", "TC06", "Không hợp lệ: tháng 0 → ValueError",
         so_ngay_trong_thang, (0, 2024), None, ValueError)
run_test("Bài 4", "TC07", "Không hợp lệ: tháng 13 → ValueError",
         so_ngay_trong_thang, (13, 2024), None, ValueError)
run_test("Bài 4", "TC08", "Không hợp lệ: năm 0 → ValueError",
         so_ngay_trong_thang, (1, 0), None, ValueError)
run_test("Bài 4", "TC09", "Ngoại lệ: tháng 'abc' → TypeError",
         so_ngay_trong_thang, ("abc", 2024), None, TypeError)

# =============================================================================
# BÀI 5: Kiểm tra số nguyên tố
# =============================================================================
print("\n" + "="*60)
print("BÀI 5: Kiểm tra số nguyên tố")
print("="*60)

run_test("Bài 5", "TC01", "Hợp lệ: n=2 → True",
         la_so_nguyen_to, (2,), True)
run_test("Bài 5", "TC02", "Hợp lệ: n=17 → True",
         la_so_nguyen_to, (17,), True)
run_test("Bài 5", "TC03", "Hợp lệ: n=4 → False",
         la_so_nguyen_to, (4,), False)
run_test("Bài 5", "TC04", "Hợp lệ: n=97 → True",
         la_so_nguyen_to, (97,), True)
run_test("Bài 5", "TC05", "Biên: n=1 → False",
         la_so_nguyen_to, (1,), False)
run_test("Bài 5", "TC06", "Biên: n=0 → False",
         la_so_nguyen_to, (0,), False)
run_test("Bài 5", "TC07", "Không hợp lệ: n=-5 → ValueError",
         la_so_nguyen_to, (-5,), None, ValueError)
run_test("Bài 5", "TC08", "Ngoại lệ: n=3.5 → TypeError",
         la_so_nguyen_to, (3.5,), None, TypeError)

# =============================================================================
# BÀI 6: Tổng S = 1 - 2 + 3 - ... + n
# =============================================================================
print("\n" + "="*60)
print("BÀI 6: Tổng S = 1 - 2 + 3 - 4 + ... + n")
print("="*60)

run_test("Bài 6", "TC01", "Hợp lệ: n=1 → 1",
         tinh_tong_xen_ke, (1,), 1)
run_test("Bài 6", "TC02", "Hợp lệ: n=4 → -2",
         tinh_tong_xen_ke, (4,), -2)
run_test("Bài 6", "TC03", "Hợp lệ: n=5 → 3",
         tinh_tong_xen_ke, (5,), 3)
run_test("Bài 6", "TC04", "Hợp lệ: n=10 → -5",
         tinh_tong_xen_ke, (10,), -5)
run_test("Bài 6", "TC05", "Không hợp lệ: n=0 → ValueError",
         tinh_tong_xen_ke, (0,), None, ValueError)
run_test("Bài 6", "TC06", "Không hợp lệ: n=-3 → ValueError",
         tinh_tong_xen_ke, (-3,), None, ValueError)
run_test("Bài 6", "TC07", "Ngoại lệ: n='abc' → TypeError",
         tinh_tong_xen_ke, ("abc",), None, TypeError)

# =============================================================================
# BÀI 7: ƯCLN
# =============================================================================
print("\n" + "="*60)
print("BÀI 7: Tìm ƯCLN")
print("="*60)

run_test("Bài 7", "TC01", "Hợp lệ: a=12, b=8 → 4",
         ucln, (12, 8), 4)
run_test("Bài 7", "TC02", "Hợp lệ: a=7, b=5 → 1",
         ucln, (7, 5), 1)
run_test("Bài 7", "TC03", "Hợp lệ: a=100, b=25 → 25",
         ucln, (100, 25), 25)
run_test("Bài 7", "TC04", "Hợp lệ: a=36, b=48 → 12",
         ucln, (36, 48), 12)
run_test("Bài 7", "TC05", "Biên: a=1, b=1 → 1",
         ucln, (1, 1), 1)
run_test("Bài 7", "TC06", "Biên: a=0, b=5 → 5",
         ucln, (0, 5), 5)
run_test("Bài 7", "TC07", "Không hợp lệ: a=-4 → ValueError",
         ucln, (-4, 8), None, ValueError)
run_test("Bài 7", "TC08", "Không hợp lệ: a=0, b=0 → ValueError",
         ucln, (0, 0), None, ValueError)
run_test("Bài 7", "TC09", "Ngoại lệ: a='a' → TypeError",
         ucln, ("a", 5), None, TypeError)

# =============================================================================
# BÀI 8: Tổng giai thừa
# =============================================================================
print("\n" + "="*60)
print("BÀI 8: Tổng S = 1! + 2! + ... + n!")
print("="*60)

run_test("Bài 8", "TC01", "Hợp lệ: n=1 → 1",
         tong_giai_thua, (1,), 1)
run_test("Bài 8", "TC02", "Hợp lệ: n=3 → 9 (1+2+6)",
         tong_giai_thua, (3,), 9)
run_test("Bài 8", "TC03", "Hợp lệ: n=5 → 153",
         tong_giai_thua, (5,), 153)
run_test("Bài 8", "TC04", "Hợp lệ: n=4 → 33",
         tong_giai_thua, (4,), 33)
run_test("Bài 8", "TC05", "Không hợp lệ: n=0 → ValueError",
         tong_giai_thua, (0,), None, ValueError)
run_test("Bài 8", "TC06", "Không hợp lệ: n=-1 → ValueError",
         tong_giai_thua, (-1,), None, ValueError)
run_test("Bài 8", "TC07", "Ngoại lệ: n=2.5 → TypeError",
         tong_giai_thua, (2.5,), None, TypeError)
run_test("Bài 8", "TC08", "Ngoại lệ: n='a' → TypeError",
         tong_giai_thua, ("a",), None, TypeError)

# =============================================================================
# Tổng kết
# =============================================================================
print("\n" + "="*60)
print("TỔNG KẾT KẾT QUẢ KIỂM THỬ")
print("="*60)

total = len(results)
passed = sum(1 for r in results if r["Trạng thái"] == PASS)
failed = total - passed

print(f"Tổng số test case: {total}")
print(f"  PASS: {passed}")
print(f"  FAIL: {failed}")
print(f"  Tỉ lệ pass: {passed/total*100:.1f}%")

if failed > 0:
    print("\nDanh sách test FAIL:")
    for r in results:
        if r["Trạng thái"] == FAIL:
            print(f"  - [{r['Bài']}] {r['TC']}: {r['Mô tả']}")
            print(f"    → {r['Ghi chú']}")
