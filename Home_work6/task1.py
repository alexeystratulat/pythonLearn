"""
Написати функцію, що визначає чи введене число є парним:

def is_even(number): # returns boolean value
    pass
"""


def is_even(number):
    return number % 2 == 0



def tests():
    assert is_even(2) == True
    assert is_even(3) == False


def main():
    number = int(input("input number "))
    print(is_even(number))


if __name__ == "__main__":
    tests()
    main()