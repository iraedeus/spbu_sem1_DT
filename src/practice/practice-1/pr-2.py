def swap(arr, n, m):
    arr.reverse()
    arr[0:m] = arr[m-1:-1:-1]
    return arr

print(swap([1,2,3,4], 1, 3))