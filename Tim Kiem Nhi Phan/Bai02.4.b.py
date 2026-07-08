def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid

        elif key < arr[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]


key2 = 5
result2 = binary_search(arr, key2)

if result2 != -1:
    print("Tim thay", key2, "tai vi tri:", result2)
else:
    print("Khong tim thay", key2)