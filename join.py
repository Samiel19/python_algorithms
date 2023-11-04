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
    print(*result, sep=' ')


if __name__ == '__main__':
    x = int(input())
    if x == 0:
        ps = input()
        A = []
    else:
        A = [int(a) for a in input().split(' ')]
    y = int(input())
    if y == 0:
        ps = input()
        B = []
    else:
        B = [int(a) for a in input().split(' ')]
    join(A, B)
