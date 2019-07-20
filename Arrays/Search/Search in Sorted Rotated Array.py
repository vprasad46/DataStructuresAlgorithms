# Search Algorithm for Sorted Rotated Array


def search(arr, start, end, len, searchElement):
    middle = int((start + end) / 2)
    if end > 0 and middle < len and start != end:
        if arr[middle] == searchElement:
            return middle
        elif arr[middle] < searchElement:
            return search(arr, middle + 1, end, len, searchElement)
        elif arr[middle] > searchElement:
            return search(arr, start, middle - 1, len, searchElement)


def pivot(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return i + 1
    return -1


arr = [5, 6, 7, 8, 1, 2, 4]
searchElement = 3

pivotIndex = pivot(arr)

if pivotIndex == -1:
    print("This is not a sorted rotated array")
elif arr[pivotIndex] == searchElement:
    print("The searchElement is found at the index: " + str(pivotIndex))
elif arr[pivotIndex - 1] >= searchElement >= arr[0]:
    print("The searchElement is found at the index: " + str(search(arr, 0, pivotIndex - 1, pivotIndex, searchElement)))
elif searchElement >= arr[pivotIndex + 1]:
    print("The searchElement is found at the index: " + str(
        search(arr, pivotIndex + 1, len(arr), len(arr) - pivotIndex + 1, searchElement)))
