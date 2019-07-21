def sumFromSubArray(arr, sum):
    currentSum = arr[0] + arr[1]
    i = 0
    j = 1
    arrSize = len(arr)
    while i < j < arrSize and i != j:
        if currentSum == sum:
            return i+1, j+1
        elif currentSum > sum:
            currentSum -= arr[i]
            i += 1
        elif currentSum < sum:
            j += 1
            currentSum += arr[j]
    return None


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print("The sum can be got from the array : " + str(sumFromSubArray(arr, 2.5)))
