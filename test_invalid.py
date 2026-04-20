from bai_tap import (
    chu_vi_hinh_chu_nhat, dien_tich_hinh_chu_nhat,
    giai_phuong_trinh_bac2, so_ngay_trong_thang,
    la_so_nguyen_to, tinh_tong_xen_ke, ucln, tong_giai_thua,
)

PASS = "PASS"
FAIL = "FAIL"
results = []


def run_test(bai, ma_tc, mo_ta, func, args, loai_exception):
    try:
        actual = func(*args)
        status = FAIL
        note = f"Mong đợi {loai_exception.__name__} nhưng nhận được: {actual}"
    except Exception as e:
        if isinstance(e, loai_exception):
            status = PASS
            note = f"Exception đúng: {type(e).__name__}: {e}"
        else:
            status = FAIL
            note = f"Sai exception: mong {loai_exception.__name__}, nhận {type(e).__name__}: {e}"

    results.append({"Bài": bai, "TC": ma_tc, "Mô tả": mo_ta,
                    "Trạng thái": status, "Ghi chú": note})
    print(f"[{status}] {bai} - {ma_tc}: {mo_ta} | {note}")


print("=" * 60)
print("BÀI 1: Chu vi hình chữ nhật - Không hợp lệ / Ngoại lệ")
print("=" * 60)
run_test("Bài 1", "TC05", "a=-1 (âm) → ValueError",        chu_vi_hinh_chu_nhat, (-1, 3),     ValueError)
run_test("Bài 1", "TC06", "a=0 (biên không hợp lệ) → ValueError", chu_vi_hinh_chu_nhat, (0, 5), ValueError)
run_test("Bài 1", "TC07", "a='abc' (sai kiểu) → TypeError", chu_vi_hinh_chu_nhat, ("abc", 3),  TypeError)
run_test("Bài 1", "TC08", "b=None (sai kiểu) → TypeError",  chu_vi_hinh_chu_nhat, (5, None),   TypeError)

print("\n" + "=" * 60)
print("BÀI 2: Diện tích hình chữ nhật - Không hợp lệ / Ngoại lệ")
print("=" * 60)
run_test("Bài 2", "TC05", "a=-2 (âm) → ValueError",         dien_tich_hinh_chu_nhat, (-2, 5),  ValueError)
run_test("Bài 2", "TC06", "b=0 (biên không hợp lệ) → ValueError", dien_tich_hinh_chu_nhat, (4, 0), ValueError)
run_test("Bài 2", "TC07", "a=None (sai kiểu) → TypeError",  dien_tich_hinh_chu_nhat, (None, 5), TypeError)
run_test("Bài 2", "TC08", "b='x' (sai kiểu) → TypeError",   dien_tich_hinh_chu_nhat, (3, "x"),  TypeError)

print("\n" + "=" * 60)
print("BÀI 3: Giải phương trình bậc 2 - Không hợp lệ / Ngoại lệ")
print("=" * 60)
run_test("Bài 3", "TC07", "a='x' (sai kiểu) → TypeError",   giai_phuong_trinh_bac2, ("x", 1, 0), TypeError)
run_test("Bài 3", "TC08", "b=None (sai kiểu) → TypeError",  giai_phuong_trinh_bac2, (1, None, 0), TypeError)
run_test("Bài 3", "TC09", "c='z' (sai kiểu) → TypeError",   giai_phuong_trinh_bac2, (1, 2, "z"), TypeError)

print("\n" + "=" * 60)
print("BÀI 4: Số ngày trong tháng - Không hợp lệ / Ngoại lệ")
print("=" * 60)
run_test("Bài 4", "TC07", "tháng=0 (biên dưới không hợp lệ) → ValueError", so_ngay_trong_thang, (0, 2024),    ValueError)
run_test("Bài 4", "TC08", "tháng=13 (biên trên không hợp lệ) → ValueError", so_ngay_trong_thang, (13, 2024),  ValueError)
run_test("Bài 4", "TC09", "năm=0 → ValueError",              so_ngay_trong_thang, (1, 0),       ValueError)
run_test("Bài 4", "TC10", "tháng='abc' → TypeError",         so_ngay_trong_thang, ("abc", 2024), TypeError)
run_test("Bài 4", "TC11", "năm='xy' → TypeError",            so_ngay_trong_thang, (1, "xy"),    TypeError)

print("\n" + "=" * 60)
print("BÀI 5: Kiểm tra số nguyên tố - Không hợp lệ / Ngoại lệ")
print("=" * 60)
run_test("Bài 5", "TC07", "n=-5 (âm) → ValueError",           la_so_nguyen_to, (-5,),   ValueError)
run_test("Bài 5", "TC08", "n=-1 (biên âm) → ValueError",      la_so_nguyen_to, (-1,),   ValueError)
run_test("Bài 5", "TC09", "n=3.5 (số thực) → TypeError",      la_so_nguyen_to, (3.5,),  TypeError)
run_test("Bài 5", "TC10", "n='abc' (chuỗi) → TypeError",      la_so_nguyen_to, ("abc",), TypeError)

print("\n" + "=" * 60)
print("BÀI 6: Tổng xen kẽ - Không hợp lệ / Ngoại lệ")
print("=" * 60)
run_test("Bài 6", "TC05", "n=0 (biên dưới không hợp lệ) → ValueError", tinh_tong_xen_ke, (0,),     ValueError)
run_test("Bài 6", "TC06", "n=-3 (âm) → ValueError",            tinh_tong_xen_ke, (-3,),    ValueError)
run_test("Bài 6", "TC07", "n='abc' → TypeError",               tinh_tong_xen_ke, ("abc",),  TypeError)
run_test("Bài 6", "TC08", "n=1.5 (số thực) → TypeError",       tinh_tong_xen_ke, (1.5,),   TypeError)

print("\n" + "=" * 60)
print("BÀI 7: ƯCLN - Không hợp lệ / Ngoại lệ")
print("=" * 60)
run_test("Bài 7", "TC07", "a=-4 (âm) → ValueError",            ucln, (-4, 8),   ValueError)
run_test("Bài 7", "TC08", "a=0, b=0 → ValueError",             ucln, (0, 0),    ValueError)
run_test("Bài 7", "TC09", "a='a' (sai kiểu) → TypeError",      ucln, ("a", 5),  TypeError)
run_test("Bài 7", "TC10", "b=2.5 (số thực) → TypeError",       ucln, (4, 2.5),  TypeError)

print("\n" + "=" * 60)
print("BÀI 8: Tổng giai thừa - Không hợp lệ / Ngoại lệ")
print("=" * 60)
run_test("Bài 8", "TC05", "n=0 (biên dưới không hợp lệ) → ValueError", tong_giai_thua, (0,),    ValueError)
run_test("Bài 8", "TC06", "n=-1 (âm) → ValueError",            tong_giai_thua, (-1,),   ValueError)
run_test("Bài 8", "TC07", "n=2.5 (số thực) → TypeError",       tong_giai_thua, (2.5,),  TypeError)
run_test("Bài 8", "TC08", "n='a' (chuỗi) → TypeError",         tong_giai_thua, ("a",),  TypeError)

print("\n" + "=" * 60)
print("TỔNG KẾT - ISSUE #2: Dữ liệu không hợp lệ, biên, ngoại lệ")
print("=" * 60)
total = len(results)
passed = sum(1 for r in results if r["Trạng thái"] == PASS)
print(f"Tổng: {total} | PASS: {passed} | FAIL: {total - passed} | Tỉ lệ: {passed/total*100:.1f}%")
