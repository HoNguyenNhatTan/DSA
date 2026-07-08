def ton_tai(a, x):
    for item in a:
        if item == x:
            return True  
    return False

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập mảng số nguyên: ").split()]
    x = int(input("Nhập số x cần kiểm tra: "))
    
    if ton_tai(a, x):
        print(f"Kết quả: True ({x} có tồn tại trong mảng)")
    else:
        print(f"Kết quả: False ({x} không tồn tại trong mảng)")