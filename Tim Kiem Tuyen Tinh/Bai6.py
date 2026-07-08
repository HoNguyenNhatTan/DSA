def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i  
    return -1  

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập các phần tử của mảng: ").split()]
    x = int(input("Nhập giá trị x cần tìm: "))
    
    ket_qua = linear_search(a, x)
    print(f"Vị trí đầu tiên của {x} trong mảng là: {ket_qua}")