def partition(x, arr):
    left = []
    right = []
    mid = []
    for i in arr:
        if i < x:
            left.append(i)
        elif i == x:
            mid.append(i)
        elif i > x:
            right.append(i)
    return left, right, mid


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = sum(arr) // len(arr)
    left, right, mid = partition(mid, arr)
    quick_sort(left)
    quick_sort(right)
    arr[:] = left + mid + right


if __name__ == '__main__':
    n = int(input())
    if n == 0:
        ps = input()
        arr = []
    else:
        arr = [int(a) for a in input().split(' ')]
    quick_sort(arr)
    print(*arr, sep=' ')