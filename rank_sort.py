from itertools import chain
from copy import deepcopy


phase_1 = {
    'Bucket 0': [],
    'Bucket 1': [],
    'Bucket 2': [],
    'Bucket 3': [],
    'Bucket 4': [],
    'Bucket 5': [],
    'Bucket 6': [],
    'Bucket 7': [],
    'Bucket 8': [],
    'Bucket 9': [],
    }


def rank_sort(arr, phase_1):
    counter = 1
    print('Initial array:')
    print(*arr, sep=', ')
    print(f'**********\nPhase {counter}')
    length = len(arr[0])
    for i in arr:
        phase_1[f'Bucket {i[-1]}'] += [i]
    for bucket, numbers in phase_1.items():
        x = numbers
        if numbers == []:
            x = 'empty'
        else:
            x = ', '.join(map(str, numbers))
        print(f'{bucket}: {x}')
    print('**********')
    phase_empty = {
        'Bucket 0': [],
        'Bucket 1': [],
        'Bucket 2': [],
        'Bucket 3': [],
        'Bucket 4': [],
        'Bucket 5': [],
        'Bucket 6': [],
        'Bucket 7': [],
        'Bucket 8': [],
        'Bucket 9': [],
        }
    phase_2 = {
        'Bucket 0': [],
        'Bucket 1': [],
        'Bucket 2': [],
        'Bucket 3': [],
        'Bucket 4': [],
        'Bucket 5': [],
        'Bucket 6': [],
        'Bucket 7': [],
        'Bucket 8': [],
        'Bucket 9': [],
        }
    if length > 1:
        rank = -2
        while rank >= -length:
            for bucket, numbers in phase_1.items():
                if numbers != []:
                    i = 0
                    while i < len(numbers):
                        if numbers[i][rank] == bucket[-1]:
                            phase_2[bucket] += [numbers[i]]
                        elif numbers[i][rank] != bucket[-1]:
                            phase_2[
                                f'Bucket {numbers[i][rank]}'
                                ] += [numbers[i]]
                        i += 1
            rank -= 1
            counter += 1
            print(f'Phase {counter}')
            phase_1 = deepcopy(phase_2)
            for bucket, numbers in phase_2.items():
                x = numbers
                if numbers == []:
                    x = 'empty'
                else:
                    x = ', '.join(map(str, numbers))
                print(f'{bucket}: {x}')
            print('**********')
            phase_2 = deepcopy(phase_empty)

    result = list(chain(*phase_1.values()))
    print('Sorted array:')
    print(*result, sep=', ')
    return result


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    rank_sort(arr, phase_1)


dict = {1: ['11', '12'],
        2: ['13', '13']}

for num in list(chain(*dict.values())):
    print(num)