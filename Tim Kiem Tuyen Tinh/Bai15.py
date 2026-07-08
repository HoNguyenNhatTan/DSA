import math

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def tim_snt_dau_tien(a):
    for i in range(len(a)):
        if la_so_nguyen_to(a[i]):
            return a[i], i  
    return None, -1

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập mảng số nguyên dương (VD: 4 6 9 7 11): ").split()] 
    
    gia_tri, vi_tri = tim_snt_dau_tien(a)
    if vi_tri != -1:
        print(f"Số nguyên tố đầu tiên là {gia_tri} tại vị trí {vi_tri}") 
    else:
        print("Mảng không có số nguyên tố nào!")