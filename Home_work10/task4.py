"""
Розширити розв'язок задачі 5 з домашки 7:

Програма випадковим чином обирає число від 1 до 10 і пропонує користувачу його вгадати.
Користувач вводить число, а програма перевіряє його і, якщо користувач не вгадав, то програма повідомляє, що введене число більше або менше від згенерованого.
Після цього знову просить вгадати. І так, поки користувач не вгадає.

Щоб згенерувати випрадкове число, скористайтеся функцією randint з модулю random.

Нові умови до завдання:

Програма пропонує дві гри на вибір: або вгадує користувач, або програма.
При цьому варіанті, коли вгадує програма, то вона пропонує число, а користувач повідомляє чи це правильне число, або чи воно більше чи менше за правильне.
В обох варіантах гри число загадується в проміжку від 1 до 100
Після однієї гри, програма пропонує повторити питаючи про це.
Якщо користувач відповів негативно: завершити роботу.
У варіанті гри, коли вгадує програма, для вгадування, програма може використати звичайні випадкові числа від random.randint (але гра буде довгою).
Але краще застосувати Двійковий пошук: відео з поясненням, вікіпедія
Ввід від користувача оформити функціями get_integer, get_str, що побудовані з врахуванням практик, описаних на лекції.
"""

from random import randint


def main():
    choosing_of_game()


def choosing_of_game():
    print("Who guesses ?")
    print("1-comp 2-you")
    print("or press 3 for exit! ")
    a = input()
    if a == '1':
        game1()

    elif a == '2':
        game2()

    elif a == '3':
        pass


def game1():
    random = randint(0, 10)
    # print(random)
    while True:
        number = int(input("Input the number :"))

        if number == random:
            print("You win!")

        else:
            print("Try more. Your number is bigger ?" if random < number else "Your number is lower")


def game2():
    print("Choose nubmer between 1 and 100 !")
    lower = 0
    upper = 101
    while True:

        random = randint(lower + 1, upper - 1)

        print("You number is", random, "?")
        print("'1' - yes ")
        print("'2' - your number is more than", random, "?")
        print("'3' - your number is less than", random, "?")

        customer_input = input()

        if customer_input == '1':
            print("You WIN !")
            customer_wants_to_play = input("Do you want to continue ? y - yes , n - no ")
            if customer_wants_to_play == 'y':
                choosing_of_game()
            else:
                break

        elif customer_input == '2':
            lower = random

        elif customer_input == '3':
            upper = random


if __name__ == "__main__":
    main()
