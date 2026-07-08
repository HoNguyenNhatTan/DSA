def tim_phan_tu_gan_x_nhat(a, x):
    if not a: 
        return None, -1
        
    min_diff = abs(a[0] - x)  
    val_gan_nhat = a[0]
    pos_gan_nhat = 0
    
    for i in range(1, len(a)):
        diff = abs(a[i] - x)  
        if diff < min_diff:
            min_diff = diff
            val_gan_nhat = a[i]
            pos_gan_nhat = i
            
    return val_gan_nhat, pos_gan_nhat

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập mảng số (VD: 10 22 28 29 40): ").split()] 
    x = int(input("Nhập giá trị x cần so sánh (VD: 26): ")) 
    
    gia_tri, vi_tri = tim_phan_tu_gan_x_nhat(a, x)
    print(f"Phần tử gần nhất với {x} là {gia_tri} tại vị trí {vi_tri}") 