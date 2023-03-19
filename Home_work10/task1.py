"""
Розширити функцію copydeep() з попереднього домашнього завдання, щоб вона також коректно працювала на рекурсивних структурах данних.

Не можна використовувати deepcopy з модулю copy
УВАГА: Вважати, що кортежі, тобто tuple ніколи не будуть присутні в данних! Їх не треба обробляти -- інакше це безкінечно збільшить складність вашої функції
Вважати, що можливі лише ці типи об'єктів та іхніх можливих вкладених елементів, які можуть бути передані у функцію: str, int, float, bool, list, dict
Якщо редагується будь-яка частина чи вкладений на довільній глибині елемент оригінального списку, то в копії не має нічого змінюватися.
Алгоритм може бути такий:
Потрібно завести об'єкт memory, як на лекції
На початку функції перевірити чи об'єкт obj вже присутній в memory за його id. Якщо так -- повернути його з memory, не копіювати
Перед копіюванням списку/словника, створити порожній список/словник, додати його в memory за ключем, що є id оригінального списку/словника
Далі в відповідному циклі for копіювати і давати елементи в копію спика/словника, що створена на попередньому кроці
Повернути копію списка/словника
УВАГА: не намагайтеся для рішення використати list-comprehension, dict-comprehension чи generator expression: рішення не вийде, а ви себе заведете в тупик
Перевіряйте на такому прикладі:

test_data = [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658]}, 2.0, {'e': 0}]
test_data[3]['d'] = test_data
test_data[-1]['f'] = test_data[-1]
copy = copydeep(test_data)
print(test_data)
# [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
print(copy)
# [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
print(copy[3]['c'] is not test_data[3]['c'])  # True
print(copy[3]['d'] is not test_data[3]['d'])  # True
print(copy[3]['d'] is copy)  # True
print(copy[-1] is not test_data[-1])  # True
print(copy[-1] is copy[-1]['f'])  # True
"""

from typing import Union


def copydeep(
    obj: Union[str, int, float, bool, list, dict], memory=None
) -> Union[str, int, float, bool, list, dict]:
    if memory is None:
        memory = {}

    if id(obj) in memory:
        return memory[id(obj)]

    elif isinstance(obj, (int, float, str, bool)):
        memory[id(obj)] = obj
        return obj

    elif isinstance(obj, list):
        copy_list = []
        memory[id(obj)] = copy_list
        for el in obj:
            copy_list.append(copydeep(el, memory))
        return copy_list

    elif isinstance(obj, dict):
        copy_dict = {}
        memory[id(obj)] = copy_dict
        for key, value in obj.items():
            copy_dict[copydeep(key, memory)] = copydeep(value, memory)
        return copy_dict


def test_deep_copy():
    test_data = [1, 2, [4, 5, 6], {"A": "B", "c": [3658]}, 2.0, {"e": 0}]
    test_data[3]["d"] = test_data
    copy = copydeep(test_data)

    assert copy[3]["d"] is not test_data[3]["d"], "true"


if __name__ == "__main__":
    test_deep_copy()