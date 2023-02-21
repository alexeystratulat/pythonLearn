"""
Програма випадковим чином обирає число від 1 до 10 і пропонує користувачу його вгадати.
Користувач вводить число, а програма перевіряє його і, якщо користувач не вгадав, то програма повідомляє,
що введене число більше або менше від згенерованого.
Після цього знову просить вгадати. І так, поки користувач не вгадає.

Щоб згенерувати випрадкове число, скористайтеся функцією randint з модулю random.

"""
from random import randint


def main():
    random = randint(0, 10)
    while True:
        number = int(input("Input the number :"))

        if number == random:
            print("You win!")
            break
        else:
            print("Try more your number is bigger ?", random < number )


if __name__ == "__main__":
    main()
