"""
Написати функцію, що приймає безліч ітерабельних (не лише списків!) об'єктів, а повертає список з усіх елементів цих об'єктів разом.

def lchain(*iterables):  # returns list
     pass

assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]
"""


def lchain(*iterables):  # returns list
    result = []
    for i in iterables:
        result.extend(i)
    return result


def main():
    print(lchain({'5': 5}, tuple(), (6, 7)))


def test():
    assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]


if __name__ == '__main__':
    main()
    test()
