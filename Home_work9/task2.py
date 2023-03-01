"""
Написати функцію, що знаходить різницю між сумою усіх парних чисел та сумою усіх непарних чисел серед
num_limit випадкових чисел згенерованих в заданому діапазоні lower_bound..upper_bound.
Для генерації чисел використайте модуль random (можна використати будь-яку зі зручних для вас функцій модулю, наприклад randint).

def diff_odd_even(num_limit, lower_bound, upper_bound): # returns int
    pass
"""

import random


def diff_odd_even(num_limit, lower_bound, upper_bound):  # returns int
    numbers = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    sum_of_even_numbers = 0
    sum_of_non_even_numbers = 0
    for i in numbers:

        if i % 2 == 0:
            sum_of_even_numbers += i
        else:
            sum_of_non_even_numbers += i

    return sum_of_even_numbers, sum_of_non_even_numbers


def main():
    lower_bound = int(input("Please input lower_bound "))
    upper_bound = int(input("Please input upper_bound "))
    num_limit = int(input("Please input num_limit "))
    print(diff_odd_even(num_limit, lower_bound, upper_bound))


if __name__ == '__main__':
    main()
