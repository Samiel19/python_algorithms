from math import pi, atan2, sqrt


def moscow_travel(A_x, A_y, B_x, B_y):
    a_zero_dist = sqrt(A_x * A_x + A_y * A_y)
    b_zero_dist = sqrt(B_x * B_x + B_y * B_y)
    simple_dist = a_zero_dist + b_zero_dist
    delta = abs(a_zero_dist - b_zero_dist)
    a = atan2(B_y, B_x) * 180 / pi - atan2(A_y, A_x) * 180 / pi
    r = min(a_zero_dist, b_zero_dist)
    circle_dist = abs(2 * pi * r * a / 360)
    if circle_dist == 0:
        circle_dist = delta
    else:
        circle_dist = circle_dist + delta
    print(min(abs(simple_dist), abs(circle_dist)))


if __name__ == '__main__':
    A_x, A_y, B_x, B_y = [int(a) for a in input().split(' ')]
    moscow_travel(A_x, A_y, B_x, B_y)