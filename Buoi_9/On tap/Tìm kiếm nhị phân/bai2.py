def tim_vi_tri(mang, x):

    dau = mang.index(x)
    cuoi = len(mang) - 1 - mang[::-1].index(x)

    print("Đầu:", dau)
    print("Cuối:", cuoi)
    print("Đếm:", cuoi - dau + 1)


tim_vi_tri([1,2,2,2,3],2)