"""
Шаховий кінь ходить буквою "Г" - на дві клітинки по вертикалі в будь-якому напрямку і на одну клітинку по горизонталі, чи навпаки.
Дані дві різні клітини шахівниці, визначте, чи може кінь потрапити з першої клітини на другу одним ходом.
Клітина шахівниці задається одним рядком, що складається з символу a-h та цифри 1-8: a2, e2, e4, h7, d1, і т.і.
"""


def logic(start, finish):
    diff_letters = ord(finish[0]) - ord(start[0])
    diff2 = int(finish[1]) - int(start[1])
    return abs(diff_letters) * abs(diff2) == 2


def main():
    start = input("start ")
    finish = input("finish ")
    print("You can do it" if logic(start, finish) else "No way")


if __name__ == '__main__':
    main()
