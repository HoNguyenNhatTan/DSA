def linear_search_sentinel(a, x):
    n = len(a)
    a.append(x)  
    
    i = 0
    while a[i] != x:  
        i += 1
        
    a.pop()  
    
    if i < n:  
        return i
    return -1

if __name__ == "__main__":
    a = [int(item) for item in input("Nhập mảng số nguyên: ").split()]
    x = int(input("Nhập giá trị x cần tìm: "))
    
    vi_tri = linear_search_sentinel(a, x)
    print(f"Vị trí tìm kiếm (bằng lính canh): {vi_tri}")