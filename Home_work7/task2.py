"""
Створити програму, що виводить на екран числа від 1 до 100 при цьому заміняючи:

числа, що діляться на 3, на рядок Fizz
числа, що діляться на 5, на рядок Buzz
числа, що діляться і на 3, і на 5, на рядок FizzBuzz
"""


def main():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


if __name__ == '__main__':
    main()
