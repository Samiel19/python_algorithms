def bracket_seq(seq):
    bracket_dict = '{([])}'
    close_brackets = ')]}'
    start_brackets = '{[('
    pairs = ['()', '[]', '{}']
    start = []
    for bracket in seq:
        if bracket not in bracket_dict:
            continue
        elif bracket in close_brackets and len(start) == 0:
            return 'no'
        elif bracket in start_brackets:
            start.append(bracket)
            continue
        pair = start.pop()
        if (pair + bracket) not in pairs:
            return 'no'
    return 'yes' if len(start) == 0 else 'no'


if __name__ == '__main__':
    seq = input()
    print(bracket_seq(seq))