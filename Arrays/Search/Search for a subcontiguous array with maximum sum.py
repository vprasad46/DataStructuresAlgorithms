def getSubContiguousArrayOfMaximumSum(arr):
    arrSize = len(arr)
    maxSum = arr[0]
    currentSum = maxSum
    maxStartIndex = 0
    maxEndIndex = 0
    currentStartIndex = 0
    currentEndIndex = 0
    for i in range(1, arrSize):
        if arr[i] > currentSum + arr[i]:
            currentStartIndex = i
            currentEndIndex = i
            currentSum = arr[i]

        else:
            currentSum = currentSum + arr[i]
            currentEndIndex = i

        if currentSum > maxSum:
            maxStartIndex = currentStartIndex
            maxEndIndex = currentEndIndex
            maxSum = currentSum

    return maxStartIndex, maxEndIndex, maxSum


arr = [-2, -3, 4, -1, -2, 7, -5, -3]
result = getSubContiguousArrayOfMaximumSum(arr)
print("The maximum sum obtained from the given array " + str(arr) + " is " + str(result[2]))
print("The array starting index : " + str(result[0] + 1) + " and ending index: " + str(result[1] + 1))
