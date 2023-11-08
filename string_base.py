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


if __name__ == '__main__':
    string = input()
    pref = prefix(string)
    print(pref)
    print(len(pref) - pref[-1])
