def swap(arr, n, m):
    if n + m != len(arr):
        return None
    arr.reverse()
    arr[0:m] = arr[m-1::-1]
    arr[m:] = arr[len(arr)-1:m-1:-1]
    return arr


def format_arr(input_arr):
    return [int(i) for i in input_arr.split(',')]


if __name__ == '__main__':
    print('Enter your array in format x1,x2...xn: ')
    array_input = input('')
    n = int(input('Enter number n: '))
    m = int(input('Enter number m: '))

    print('\nResult is: ')
    print(swap(format_arr(array_input), n, m))