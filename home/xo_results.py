class Winner(Exception):
    def __init__(self, winner):
        self.sign = winner


def check(seq):
    unique = set(seq)
    if len(unique) == 1 and unique != set('.'):
        raise Winner(unique.pop())


def checkio(game_result):
    try:
        # check lines
        for line in game_result:
            check(line)

        # check rows
        rows = [l[i] for i in range(3) for l in game_result]
        for i in range(0, 9, 3):
            check(rows[i: i + 3])

        # check diagonals
        diag1 = []
        diag2 = []
        i = 1
        for l in game_result:
            diag1.append(l[i - 1])
            diag2.append(l[i * -1])
            i += 1

        for diag in (diag1, diag2):
            check(diag)

    except Winner as win:
        return win.sign
    else:
        return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    assert checkio([
        "...",
        "XX.",
        "XOO"]) == "D", "Draw"
    assert checkio([
        "O.X.X",
        "XX.X.",
        "XXX..",
        "XX...",
        "XOO.."]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
