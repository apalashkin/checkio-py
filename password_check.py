import string


def checkio(data):
    isdigit, islower, isupper, isascii = None, None, None, None

    if len(data) < 10:
        return False

    for c in data:
        isdigit = isdigit or c.isdigit()
        islower = islower or (not c.isdigit() and c.islower())
        isupper = isupper or (not c.isdigit() and not c.islower())
    res = set(data.lower()) - set(string.ascii_lowercase)
    isascii = not res or ''.join(res).isdigit()

    return all([isdigit, islower, isupper, isascii])

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('erer798rew9rew9r7ew987rw') == False, "7th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
