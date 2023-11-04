def partition(x, arr):
    left = []
    right = []
    for i in arr:
        if i < x:
            left.append(i)
        else:
            right.append(i)
    print(len(left), len(right), sep='\n')


if __name__ == '__main__':
    n = int(input())
    if n == 0:
        ps = input()
        arr = []
    else:
        arr = [int(a) for a in input().split(' ')]
    x = int(input())
    partition(x, arr)
