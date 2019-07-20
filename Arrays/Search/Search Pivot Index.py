# Search Algorithm for sorted arrays: Binary Search

def search(arr, start, end):
    middle = int((start + end) / 2)
    if start != 0 and end != 0:
        if arr[middle] < arr[middle - 1]:
            return middle - 1
        elif arr[middle] > arr[middle + 1]:
            return middle + 1
        elif arr[middle] > arr[end]:
            return search(arr, middle + 1, end)
        else:
            return search(arr, start, middle - 1)
    else:
         return 0


arr = [7, 9, 11, 12, 13, 14]

print(search(arr, 0, len(arr) - 1))
