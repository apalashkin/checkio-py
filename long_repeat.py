import collections


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if not line:
        return 0
    max_v = 1
    tmp = 1
    p = None
    for c in line:
        if p == c:
            tmp += 1
        else:
            tmp = 1
        if tmp > max_v:
            max_v = tmp
        p = c
    return max_v


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
