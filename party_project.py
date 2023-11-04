def party_project(students, left, right):
    max_groups = students // left
    else_st = students % left
    if left <= (left + else_st / max_groups) <= right:
        print('YES')
    else:
        print('NO')


n = int(input())
for i in range(n):
    students, left, right = [int(x) for x in input().split(' ')]
    party_project(students, left, right)
