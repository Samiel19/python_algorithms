def elevator(floors, capacity):
    start_capacity = capacity
    time = 0
    while len(floors) > 0:
        while len(floors) and floors[-1] <= 0:
            if floors[-1] == 0:
                floors.pop(-1)
            else:
                delta = floors.pop(-1)
                if len(floors):
                    floors[-1] += delta
        if len(floors) <= 0:
            print(time)
            return
        if floors[-1] // capacity > 1:
            multiplier = floors[-1] // capacity
        else:
            multiplier = 1
        time += 2 * len(floors) * multiplier
        floors[-1] -= capacity * multiplier
        capacity = start_capacity
    print(time)


if __name__ == '__main__':
    floors_num = 3
    floors = [3, 0, 1, 0, 2]
    capacity = 2
    elevator(floors, capacity)
