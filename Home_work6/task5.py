"""
Користувач вводить натуральне число. Потрібно визначити, чи є рік із цим числом високосним.
Якщо рік є високосним, то виведіть `YES`, інакше виведіть `NO`.

Примітка: відповідно до григоріанського календаря, рік є високосним, якщо його номер кратний 4, але не кратний 100, а також якщо він кратний 400.
"""


def main():
    year = int(input("year ? "))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('YES')
    else:
        print('No')


if __name__ == '__main__':
    main()