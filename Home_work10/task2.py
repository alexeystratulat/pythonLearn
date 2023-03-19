"""
Створити функцію "генератор паролів", що повертає згенеровані паролі сумісні з наступними вимогами.
Можна використовувати лише криптостійкі функції для генерації паролю.
Вимоги:
Пароль складається мінімум з 8 символів, потрібну довжину приймати параметром, але не менше 8
В паролі допускаються лише великі та маленькі латинські літери, цифри та символ підкреслення "_".
Використайте змінні з модулю string (UKR)
Пароль обов'язково має містити щонайменше одну велику літеру, одну маленьку літеру та одну цифру
Не повинно бути більше 2 однакових символів підряд
"""
import random


def password_generator(pass_lenght: int):
    password = [None] * pass_lenght
    word_of_password_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    word_of_password_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    word_of_password_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    all_word = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']

    password[random.randint(0, pass_lenght - 1)] = random.choice(word_of_password_numbers)

    while True:
        i = random.randint(0, pass_lenght - 1)
        if password[i] is None:
            password[i] = random.choice(word_of_password_upper)
            break

    while True:
        i = random.randint(0, pass_lenght - 1)
        if password[i] is None:
            password[i] = random.choice(word_of_password_lower)
            break

    for i in range(pass_lenght):
        if password[i] is None:
            password[i] = random.choice(all_word)

    return "".join(password)


def main() -> None:
    while True:
        try:
            pass_lenght = input("enter password length: ")

            if int(pass_lenght) >= 8:
                print("Your password is:", password_generator(int(pass_lenght)))

                break
            else:
                print("Length should be more than 8")

        except ValueError:
            print("Invalid input!")


if __name__ == "__main__":
    main()
