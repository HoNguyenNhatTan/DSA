def tim_tat_ca(a, x):
    danh_sach_vi_tri = []
    for i in range(len(a)):
        if a[i] == x:
            danh_sach_vi_tri.append(i)  
    return danh_sach_vi_tri

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập mảng (VD: 4 1 4 9 4): ").split()] 
    x = int(input("Nhập giá trị x cần tìm: "))
    
    ket_qua = tim_tat_ca(a, x)
    print(f"Danh sách các vị trí xuất hiện của {x}: {ket_qua}")