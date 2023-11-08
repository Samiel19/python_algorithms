def z_func_naive(string):
    z = [0]*len(string)
    begin = string[0]
    for i in range(1, len(string)):
        if string[i] == begin:
            start_1 = 0
            start_2 = i
            while start_2 < len(z) and string[start_1] == string[start_2]:
                z[i] += 1
                start_1 += 1
                start_2 += 1
    return z


def z_func(s):
    z = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


if __name__ == '__main__':
    string = input()
    z = z_func_naive(string)
    z_1 = z_func(string)
    print(*z, sep=' ')
    print(*z_1, sep=' ')
