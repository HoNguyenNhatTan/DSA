def tim_vi_tri_cuoi_cung(a, x):
    # Duyệt từ len(a)-1 lùi dần về vị trí 0 bước nhảy -1
    for i in range(len(a) - 1, -1, -1): 
        if a[i] == x:
            return i  
    return -1

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập mảng số nguyên: ").split()]
    x = int(input("Nhập giá trị x cần tìm vị trí cuối: "))
    
    vi_tri = tim_vi_tri_cuoi_cung(a, x)
    print(f"Vị trí xuất hiện cuối cùng của {x} là: {vi_tri}")