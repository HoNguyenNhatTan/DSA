def tim_min_max_mot_lan(a):
    if not a: 
        print("Mảng rỗng!")
        return

    val_min = val_max = a[0]
    pos_min = pos_max = 0
    
    for i in range(1, len(a)):
        if a[i] < val_min:
            val_min = a[i]
            pos_min = i
        if a[i] > val_max:
            val_max = a[i]
            pos_max = i
            
    print(f"Giá trị nhỏ nhất: {val_min} tại vị trí {pos_min}")
    print(f"Giá trị lớn nhất: {val_max} tại vị trí {pos_max}")

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập mảng số nguyên: ").split()]
    tim_min_max_mot_lan(a)