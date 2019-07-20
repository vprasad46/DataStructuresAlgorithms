# Search Algorithm for sorted arrays: Binary Search

def search(arr, start, end, searchElement):
    middle = int((start + end) / 2)
    if end > 0 and middle < len(arr) and start != end:
        if arr[middle] == searchElement:
            return middle
        elif arr[middle] < searchElement:
            return search(arr, middle + 1, end, searchElement)
        elif arr[middle] > searchElement:
            return search(arr, start, middle - 1, searchElement)


arr = [1, 2, 3, 4, 5]
print("The value is found at index: " + str(search(arr, 0, len(arr), 3)))
