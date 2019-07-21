# Given an array of n elements, create a new array which is a rotation of given array and hamming distance between both the arrays is maximum.
# Hamming distance between two arrays or strings of equal length is the number of positions at which the corresponding character(elements) are different.


# eg :
#        Book and Look have a Hamming distance of 1 because it takes 1 word change from 'B'ook to 'L'ook
#        Objective is to find all the hamming distances of the original array and its rotations
#        And to pick the maximum of all hamming distances

def getExtendedArr(arr):
    arrSize = len(arr)
    brr = [0] * 2 * arrSize
    for i in range(2 * arrSize):
        brr[i] = arr[i % arrSize]
    return brr


def maxHammingDistance(arr):
    brr = getExtendedArr(arr)
    arrSize = len(arr)
    brrSize = len(brr)
    k = 1
    maxHamming = 0
    while k + arrSize - 1 <= brrSize - 1:
        currHamming = 0
        for j in range(arrSize):
            if brr[k + j] != arr[j]:
                currHamming = currHamming + 1

        if currHamming > maxHamming:
            maxHamming = currHamming

        k = k + 1
    return maxHamming

arr = [1, 1, 1]

print(maxHammingDistance(arr))
