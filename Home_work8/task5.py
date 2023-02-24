"""

Написати функцію, що повертає найбільшу цифру випадкового 12-ти-значного натурального числа
а) з використанням рядків
б) без використання рядків. Число для тестування можна отримати або від користувача, або згенерувати за допомогою функції randint з модулю random.

	def get_max_digit(number): # returns int
             pass
"""

import random


def get_max_digit(number):  # returns int
    res = list(map(int, str(number)))

    return max(res)


def main():
    number = 123456789012
    print(get_max_digit(number))
    print(get_max_digit(random.randint(100, 999999)))


if __name__ == '__main__':
    main()
