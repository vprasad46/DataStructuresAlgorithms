def pairPresent(arr, sum):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == sum:
            return i, j
        elif arr[i] + arr[j] > sum:
            j = j - 1
        elif arr[i] + arr[j] < sum:
            i = i + 1
    return False


arr = [1, 2, 3, 4, 5, 8]

start = pairPresent(arr, 8.5)

if type(start) == tuple:
    print(str(arr[start[0]]) + " and " + str(arr[start[1]]))
else:
    print("The sum cannot be formed from the pairs of numbers present in this array")
