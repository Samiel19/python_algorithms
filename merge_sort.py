def join(A, B):
    result = []
    i = 0
    j = 0
    while len(A) > i and len(B) > j:
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    if len(A) - i == 0:
        result += B[j:]
    elif len(B) - j == 0:
        result += A[i:]
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return
    point = len(arr) // 2
    A = arr[:point]
    B = arr[point:]
    merge_sort(A)
    merge_sort(B)
    arr[:] = join(A, B)


if __name__ == '__main__':
    n = int(input())
    if n == 0:
        ps = input()
        arr = []
    else:
        arr = [int(a) for a in input().split(' ')]
    merge_sort(arr)
    print(*arr, sep=' ')
