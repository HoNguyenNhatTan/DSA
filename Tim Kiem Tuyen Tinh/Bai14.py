def tim_vi_tri_chan_dau(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:  
            return i       
    return -1

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập mảng số nguyên (VD: 3 7 11 8 5 4): ").split()] 
    
    vi_tri = tim_vi_tri_chan_dau(a)
    if vi_tri != -1:
        print(f"Số chẵn đầu tiên là {a[vi_tri]} tại vị trí {vi_tri}") 
    else:
        print(f"Kết quả: {vi_tri} (Mảng không có số chẵn)")