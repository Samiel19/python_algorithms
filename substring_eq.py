def string_substring(string, start_1, start_2, length):
    breakpoint = 0
    if start_1 == start_2:
        print('yes')
        return
    try:
        while string[start_1 + breakpoint] == string[start_2 + breakpoint]:
            breakpoint += 1
            if breakpoint == length:
                print('yes')
                return
    except IndexError:
        print('no')
        return
    print('no')


if __name__ == '__main__':
    string = input()
    n = int(input())
    for i in range(n):
        length, start_1, start_2 = [int(a) for a in input().split(' ')]
        string_substring(string, start_1, start_2, length)