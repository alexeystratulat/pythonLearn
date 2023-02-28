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

def get_max_digit_b(number):
    num = 0
    while number >= 1:
        if number % 10 > num:
            num = number % 10
        number = number // 10
    return num


def main():
    number = 123456789012
    print(get_max_digit(number))
    print(get_max_digit(random.randint(100, 999999)))
    print(get_max_digit_b(number))
    print(get_max_digit_b(random.randint(100, 999999)))

if __name__ == '__main__':
    main()
