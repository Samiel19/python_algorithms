def contest_result(a, b, n):
    st_a_max = a
    st_b_min = b // n
    if b % n > 0:
        st_b_min += 1
    print('Yes' if st_a_max > st_b_min else 'No')


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    n = int(input())
    contest_result(a, b, n)