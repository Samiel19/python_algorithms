def mean_lev(x, students):
    result = []
    for i in range(x):
        if i == 0:
            result.append(sum(students) - students[0] * x)
        else:
            result.append(
                result[i-1] - (students[i] - students[i - 1]) *
                (x - i) + (students[i] - students[i - 1]) * (i)
                )
    print(*result, ' ')


if __name__ == '__main__':
    x = int(input())
    students = [int(a) for a in input().split(' ')]
    mean_lev(x, students)
