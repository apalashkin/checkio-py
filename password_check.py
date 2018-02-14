import string


def checkio(data):
    if len(data) < 10:
        return False
    if not [c for c in data if c.isdigit()]:
        return False
    if not [c for c in data if c.islower()]:
        return False
    if not [c for c in data if not c.islower()]:
        return False
    res = set(data.lower()) - set(string.ascii_lowercase)
    if len(res) and not ''.join(res).isdigit():
        return False

    return True

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
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
