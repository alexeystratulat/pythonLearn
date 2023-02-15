"""
У математиці функцію `sign(x)` (знак числа) визначено так:

  sign(x) = 1, якщо x > 0,

  sign(x) = -1, якщо x < 0,

  sign(x) = 0 якщо x = 0.
Напишіть функцію sign() та для введеного користувачем числа x виведіть значення sign(x).
Це завдання бажано вирішити за допомогою каскадних інструкцій if... elif... else.

"""


def sign(x):
    if x > 0:

        return 1
    elif x < 0:

        return -1
    elif x == 0:

        return 0


def main():
    x = int(input('input x: '))
    print(sign(x))


if __name__ == '__main__':
    main()
