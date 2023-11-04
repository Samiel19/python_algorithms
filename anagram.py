def anagram(a, b):
    if len(a) != len(b):
        return 'NO'
    a_dict = {}
    b_dict = {}
    for x in a:
        if x in a_dict.keys():
            a_dict[x] += 1
        else:
            a_dict[x] = 1
    for y in b:
        if y in b_dict.keys():
            b_dict[y] += 1
        else:
            b_dict[y] = 1
    return 'YES' if a_dict == b_dict else 'NO'


if __name__ == '__main__':
    a = str(input())
    b = str(input())
    print(anagram(a, b))