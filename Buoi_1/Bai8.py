def dem_xuat_hien(a, x):
    count = 0
    for item in a:
        if item == x:
            count += 1  
    return count

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập mảng (VD: 2 5 2 7 2): ").split()] 
    x = int(input("Nhập giá trị x cần đếm: "))
    
    so_lan = dem_xuat_hien(a, x)
    print(f"Số lần phần tử {x} xuất hiện trong mảng là: {so_lan}")