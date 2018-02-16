import collections

def checkio(text):
    counter = collections.Counter(text.lower())
    max_count = None
    min_letter = 'z'
    for letter, count in counter.most_common():
        if ord(letter) < 97:
            continue
        if max_count and max_count > count:
            break
        else:
            max_count = count
            if ord(min_letter) > ord(letter):
                min_letter = letter
    print(min_letter)
    return min_letter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
