import re

CYMBOLS = {
    '{': '}',
    '(': ')',
    '[': ']'
}

def checkio(expression):
    check_cymbols(expression)

def check_cymbols(expression):
    for c in CYMBOLS:
        i = c in expression and expression.index(c) or -1
        if i == -1:
            continue
        while 
        check_cymbols(expression[i: expression.index(CYMBOLS[c])])

    try:
        while expression:
            expressions = [g for g in re.search('\{(.+)\}|\((.+)\)|\[(.+)\]', expression).groups() if g]
            import pdb; pdb.set_trace()
    except Exception as err:
        import pdb; pdb.set_trace()
        return all(map(lambda x: x not in expression, '{}()[]'))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("((5+3)*2+1)") == True, "Simple"
    # assert checkio("{[(3+1)+2]+}") == True, "Different types"
    # assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    # assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    # assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    # assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("[(3)+(-1)]*{3}") == True, "test"
