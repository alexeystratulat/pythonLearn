"""
Для зручності проведення вступних іспитів, усіх абітуріентів MIT розбивають на групи з залежності від перших літер їхніх прізвищ.
Групи називаються "A-I", "J-P", "Q-T", "U-Z". Назва групи визначає, в яку групу потрапляє абітуріентка, в залежності від першої літери її прізвища.
Наприклад, Will Smith потрапить в групу "Q-T", т.я. перша літера його прізвища потрапляє в діапазон букв 'Q' та 'T' включно.
Абітуріент Jay Z потрапить в групу "U-Z".

Написати функцію, що приймає параметром список імен студентів виду ['Name1 Surname1', 'Name2 Surname2', 'Name3 Surname3', ...]
і повертає кількість абітуріентів в групах, сформованим за прізвищами описаним вище чином.

def group_by_surname(list_of_enrollees): # returns 4 ints
    pass
"""


def group_by_surname(list_of_enrollees):  # returns 4 ints

    group_1 = 'ABCDEFGHI'
    group_2 = 'JKLMNOP'
    group_3 = 'QRST'
    group_4 = 'UVWXYZ'
    counter_for_group_1 = 0
    counter_for_group_2 = 0
    counter_for_group_3 = 0
    counter_for_group_4 = 0
    for i in list_of_enrollees:

        name = i.split()[1][0]

        if name.upper() in group_1:
            counter_for_group_1 += 1
        if name.upper() in group_2:
            counter_for_group_2 += 1
        if name.upper() in group_3:
            counter_for_group_3 += 1
        if name.upper() in group_4:
            counter_for_group_4 += 1

    return counter_for_group_1, counter_for_group_2, counter_for_group_3, counter_for_group_4


def main():
    list_of_enrollees = ['Blake Antonio', 'Connor Julian', 'Aidan Harold', 'Conner Peter', 'Hunter Eli',
                         'Alberto Carlos', 'Shane Aaron', 'Marlin Paul', 'Ricardo Qector', 'Alexis Udrian']
    print(group_by_surname(list_of_enrollees))


if __name__ == "__main__":
    main()
