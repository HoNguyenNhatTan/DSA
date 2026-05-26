def tim_kiem_ma_tran(M, x):
    for r in range(len(M)):          
        for c in range(len(M[r])):   
            if M[r][c] == x:
                return r, c          
    return -1, -1

if __name__ == "__main__":
    print("Nhập ma trận (mỗi hàng cách nhau bằng dấu phẩy, các số cách nhau bằng dấu cách)")
    print("Ví dụ mẫu: 5 8 1 , 3 9 7 , 2 6 4") 
    chuoi_nhap = input("Mời nhập ma trận: ")
    
    M = [[int(num) for num in row.split()] for row in chuoi_nhap.split(",")]
    x = int(input("Nhập giá trị x cần tìm: "))
    
    dong, cot = tim_kiem_ma_tran(M, x)
    print(f"Ma trận thu được: {M}")
    print(f"Vị trí đầu tiên tìm thấy giá trị {x} là ô: ({dong}, {cot})") 