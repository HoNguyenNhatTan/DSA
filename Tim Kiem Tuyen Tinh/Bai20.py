danh_ba = []

while True:
    print("\n1. Them")
    print("2. Tim so theo ten")
    print("3. Tim ten theo so")
    print("4. Dem dau so")
    print("0. Thoat")

    chon = input("Chon: ")

    if chon == "1":
        ten = input("Nhap ten: ")
        sdt = input("Nhap sdt: ")

        danh_ba.append([ten, sdt])

    elif chon == "2":
        ten = input("Nhap ten can tim: ")

        for i in danh_ba:
            if i[0] == ten:
                print(i[1])

    elif chon == "3":
        sdt = input("Nhap sdt can tim: ")

        for i in danh_ba:
            if i[1] == sdt:
                print(i[0])

    elif chon == "4":
        dau = input("Nhap dau so: ")
        dem = 0

        for i in danh_ba:
            if i[1].startswith(dau):
                dem += 1

        print(dem)

    elif chon == "0":
        break