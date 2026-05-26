def tim_sv_theo_ma(ds_sinh_vien, ma_tim):
    for sv in ds_sinh_vien:
        if sv["ma_SV"] == ma_tim:  
            return sv  
    return None

if __name__ == "__main__":
    ds_sinh_vien = [
        {"ma_SV": "B2601", "ho_ten": "Nguyễn Văn An", "diem_TB": 8.5},
        {"ma_SV": "B2602", "ho_ten": "Trần Thị Bình", "diem_TB": 9.2} 
    ]
    
    print("--- Thêm mới 1 sinh viên từ bàn phím ---")
    ma_sv = input("Nhập mã SV mới: ").strip()
    ho_ten = input("Nhập họ tên: ").strip()
    diem_tb = float(input("Nhập điểm TB: "))
    ds_sinh_vien.append({"ma_SV": ma_sv, "ho_ten": ho_ten, "diem_TB": diem_tb})
    
    print("\n--- Tiến hành tìm kiếm ---")
    ma_can_tim = input("Nhập mã SV cần tìm thông tin: ").strip()
    
    ket_qua = tim_sv_theo_ma(ds_sinh_vien, ma_can_tim)
    if ket_qua:
        print("\n=== THÔNG TIN SINH VIÊN TÌM THẤY ===") 
        print(f"Mã số: {ket_qua['ma_SV']}")
        print(f"Họ và tên: {ket_qua['ho_ten']}")
        print(f"Điểm trung bình: {ket_qua['diem_TB']}")
    else:
        print(f"\nThông báo: Không tìm thấy sinh viên nào có mã vạch '{ma_can_tim}'.") 