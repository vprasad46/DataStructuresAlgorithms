
# Write a function rotate(ar[], d) that rotates left  arr[]  by d elements.

def leftrotate(arr):
    temp = arr[0]
    size = len(arr)
    for i in range(size-1):
        arr[i] = arr[i+1]
    arr[size-1] = temp
    return arr

def rotate(arr,n):
    for i in range(n):
        leftrotate(arr)


arr = [1,2,3,4,5]

rotate(arr,1)

print(arr)