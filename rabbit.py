def rabbit(field):
    result = max(field[0])
    for i in range(1, len(field)):
        for j in range(1, len(field[i])):
            if field[i][j] == 0:
                continue
            elif 0 in (field[i-1][j], field[i][j-1], field[i-1][j-1]):
                continue
            else:
                field[i][j] = min(
                    field[i-1][j], field[i][j-1], field[i-1][j-1]
                    ) + 1
        if max(field[i]) > result:
            result = max(field[i])
    print(result)

    print(*field, sep='\n')


if __name__ == '__main__':
    n, m = [int(a) for a in input().split(' ')]
    field = [[int(a) for a in input().split(' ')] for y in range(n)]
    rabbit(field)
