def tim_kiem_ten_sv(ds_ten, ten_tim):
    ten_tim_lower = ten_tim.lower()  
    for i in range(len(ds_ten)):
        if ds_ten[i].lower() == ten_tim_lower:  
            return i
    return -1

if __name__ == "__main__":
    nhap_chuoi = input("Nhập danh sách tên SV (cách nhau bởi dấu phẩy): ")
    ds_ten = [ten.strip() for ten in nhap_chuoi.split(",")]
    
    ten_tim = input("Nhập tên sinh viên cần tìm kiếm: ")
    
    vi_tri = tim_kiem_ten_sv(ds_ten, ten_tim)
    print(f"Mảng chuỗi: {ds_ten}")
    print(f"Kết quả vị trí tìm thấy: {vi_tri}")