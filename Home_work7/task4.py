"""
Написати функцію, що розраховує суму Unicode кодів усіх символів, що знаходяться між двома заданими символами включно.
Наприклад, в функцію передаються символи 'a' та 'd', отже треба порахувати суму кодів символів 'a', 'b', 'c' та 'd', а це 97+98+99+100=394.

def sum_symbol_codes(first, last): # returns int
    pass
"""


def sum_symbol_codes(first, last):  # returns int
    sum = 0
    for i in range(ord(first), ord(last) + 1):
        sum += i
    return sum


def main():
    first = input('1st :')
    last = input('2nd :')
    print(sum_symbol_codes(first, last))


def tests():
    assert sum_symbol_codes("a", "d") == 394


if __name__ == '__main__':
    main()
    tests()
