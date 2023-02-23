"""
Написати функцію, що повертає усі прості числа від 1 до 100 у вигляді списку.

def gen_primes():  # returns list of ints
    pass
"""


def gen_primes():
    list = []
    for i in range(2, 100):
        counter = 0
        for j in range(i - 1, 1, -1):

            if (i % j) == 0:
                counter += 1
        if counter == 0:
            list.append(i)

    return list


def main():
    print(gen_primes())


if __name__ == '__main__':
    main()
