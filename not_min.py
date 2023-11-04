def not_min(A, left, right):
    x = 'NOT FOUND'
    for a in A[left: right + 1]:
        if a != min(A[left: right + 1]):
            x = a
            break
    print(x)


if __name__ == '__main__':
    x_slices = [int(x) for x in input().split(' ')]
    slices = x_slices[-1]
    A = [int(a) for a in input().split(' ')]
    l_r = []
    for i in range(slices):
        left_right = [int(x) for x in input().split(' ')]
        l_r.append(left_right)

    for slice in l_r:
        not_min(A, slice[0], slice[1])