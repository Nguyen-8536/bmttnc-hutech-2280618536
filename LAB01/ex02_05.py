# Nhập số giờ làm mỗi tuần và thù lao trên mỗi giờ làm tiêu chuẩn
so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44  # Số giờ làm chuẩn mỗi tuần
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)  # Số giờ làm vượt chuẩn mỗi tuần
# Tính tổng thu nhập
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
# In ra số tiền thực lĩnh của nhân viên
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")
