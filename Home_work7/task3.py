"""
Згідно з древньою індійською легендою творець гри в шахи за свій винахід попросив у раджі незначну на перший погляд винагороду:
стільки пшеничних зерен, скільки опиниться на шаховій дошці, якщо на першу клітинку покласти одне зерно, на другу -- два зерна, на третю -- чотири, і т.д..
Виявилося, що такої кількості зерна немає на усій планеті (2**64-1 зерен).
Напишіть програму, що вираховує починаючи з якої клітинки дошки раджі треба було віддати Nкг зерна,
де N -- вводить користувач. Прийняти вагу однієї зернинки за 35мг. Номер клітинки виводити в букво-циферних традиційних шахових координатах.
Наприклад:

kilograms = 0.03584  # 35mg per seed, 1024 seeds
calculate_wheat_chess_position(kilograms)  # prints 'b3'

"""
from math import log2


def calculate_wheat_chess_position(kilograms):
    gram = (kilograms * 1000000) / 35
    chess = int(log2(gram) + 1)
    return "abcdefgh"[chess // 8] + str(chess % 8)


def main():
    kilograms = float(input("How many kilograms ?"))
    print(calculate_wheat_chess_position(kilograms))


def test():
    assert calculate_wheat_chess_position(0.03584) == 'b3'


if __name__ == '__main__':
    main()
    test()
