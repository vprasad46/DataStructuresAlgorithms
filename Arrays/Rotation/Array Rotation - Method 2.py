# Fuction to get gcd of a and b
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def leftrotate(arr, d):
    arrSize = len(arr)
    g_c_d = gcd(arrSize, d)

    for i in range(g_c_d):
        temp = arr[i]
        start = i
        while 1:
            if start + g_c_d < arrSize:
                arr[start] = arr[start + g_c_d]
                start += g_c_d
            else:
                arr[start] = temp
                break



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
leftrotate(arr, 5)
print(arr)
