def prefix(string):
    p = [0]*len(string)
    for i in range(1, len(string)):
        k = p[i-1]
        while k > 0 and string[k] != string[i]:
            k = p[k-1]
        if string[k] == string[i]:
            k = k + 1
            p[i] = k
    return p


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


def z_func(string):
    z = [0] * len(string)
    left, right = 0, 0
    for i in range(1, len(string)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(string) and string[z[i]] == string[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def z_from_prefix(prefix):
    z = [0] * len(prefix)
    for i in range(1, len(prefix)):
        if prefix[i] > 0:
            z[i - prefix[i] + 1] = prefix[i]
    z[0] = 0
    i = 1
    while i < len(prefix):
        t = i
        if z[i] > 0:
            for j in range(1, z[i]):
                if z[i + j] > z[j]:
                    break
                z[i + j] = min(z[j], z[i] - j)
                t = i + j
        i = t + 1
    return z


if __name__ == '__main__':
    string = 'affdassdsafs'
    z = z_func_naive(string)
    z_1 = z_func(string)
    print(*z, sep=' ')
    z_2 = z_from_prefix(prefix(string))
    print(*z_1, sep=' ')
    print(*z_2, sep=' ')
