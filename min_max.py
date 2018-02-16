def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    min_value = None
    if len(args) == 1:
        args = args[0]
    for i in args:
        if min_value is None:
            min_value = i
            continue
        if key(min_value) > key(i):
            min_value = i
    return min_value


def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    max_value = None
    if len(args) == 1:
        args = args[0]
    for i in args:
        if max_value is None:
            max_value = i
            continue
        if key(max_value) < key(i):
            max_value = i
    return max_value


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([0]) == 0, "Zero"

    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
