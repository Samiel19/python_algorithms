def evclid_gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return evclid_gcd(a-b, b)
    elif a < b:
        return evclid_gcd(a, b-a)


def fraction(a, b, c, d):
    result = [a * d + c * b, b * d]
    gcd = evclid_gcd(result[0], result[1])
    result = [int(result[0]/gcd), int(result[1]/gcd)]
    print(*result)


if __name__ == '__main':
    A = [int(a) for a in input().split(' ')]
    a, b, c, d = A
    fraction(a, b, c, d)