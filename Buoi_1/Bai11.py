def tim_max_va_vi_tri(a):
    if not a:  
        return None, -1
        
    val_max = a[0]  
    pos_max = 0
    
    for i in range(1, len(a)):
        if a[i] > val_max:
            val_max = a[i]  
            pos_max = i     
    return val_max, pos_max

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập mảng số nguyên: ").split()]
    
    gia_tri, vi_tri = tim_max_va_vi_tri(a)
    if vi_tri != -1:
        print(f"Giá trị lớn nhất là: {gia_tri} tại vị trí index: {vi_tri}")
    else:
        print("Mảng rỗng, không có giá trị lớn nhất!")