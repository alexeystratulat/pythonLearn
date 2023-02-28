"""
Написати функцію, що знаходить різницю між максимальним та мінімальним значенням з num_limit випадкових чисел згенерованих в заданому діапазоні lower_bound..upper_bound.
Для генерації чисел використайте модуль random (можна використати будь-яку зі зручних для вас функцій модулю, наприклад randint).
Для визначення мінімального та максимального значення використайте вбудовані функції min(), max().

def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    pass

    Виконайте попереднє завдання, але без використання вбудованих функцій min(), max().
"""

import random


def diff_min_max(num_limit, lower_bound, upper_bound):  # returns int
    numbers = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    return max(numbers) - min(numbers), sorted(numbers)[len(numbers) - 1] - sorted(numbers)[0]


def main():
    lower_bound = int(input("Please input lower_bound "))
    upper_bound = int(input("Please input upper_bound "))
    num_limit = int(input("Please input num_limit "))
    print(diff_min_max(num_limit, lower_bound, upper_bound))


if __name__ == '__main__':
    main()
