"""
За реузлтьаатми длосдіжнеь ооднго аглнісйкього уінвсрееитут, не має зчнаннея, в якмоу пояркду рзтооашвнаі лтіери у совлі.
Гоолвен, щоб пшреа та оастння ліетри блуи на сєвому мсіці.
Ретша летір мжоуть сділаувти в абосюлтно впиакдомову поярдук, все ондо ткест чатиитмтьеся без пброемл.
Прчиниою цгоьо є те, що ми чтаимєо не кножу бкуву окером, а усе совло раозм.



Напишіть функцію, яка прийматиме рядок тексту та перетворюватиме його способом, cхожим до описаного вище.
В якості алгоритму перемішування букв обов'язково використовуйте наступні кроки для кожного слова в тексті (треба дотриматися цих вимог та алгоритму,
а також запропонованої сигнатури функції):

Для простоти вважати, що пунктуація є "буквами" і частинами слів, до яких вона торкається.
Але, за бажанням, можна обробити лише слова, а пунктуацію лишити на правильних місцях.
Залишаєте на місці перший та останні символи слова
З тих символів, що лишилися, беремо перші три символа та перемішуємо в довільному порядку
Якщо отримана перемішана трійка не дорівнює оригінальній, то додаємо її до результату
Повторюємо з пункту 2 допоки не закінчаться неперемішані символи
def pemrtuate(text):  # returns permuted text
    pass
"""


def pemrtuate(text):  # returns permuted text
    text = text.split()
    text_to_change = text
    text_to_print = []
    for i in text_to_change:
        text_to_print.append(change(i))

    return " ".join(text_to_print)


def change(word):
    if len(word) > 3:
        word_for_return = [None] * len(word)
        word_for_return[0] = word[0]
        word_for_return[len(word) - 1] = word[len(word) - 1]

        for i in range((len(word)) // 3):
            word_for_return[i + 1] = word[len(word) - 2 - i]
            word_for_return[len(word) - 2 - i] = word[i + 1]

        if word_for_return[(len(word)) // 2] is None:
            word_for_return[(len(word)) // 2] = word[(len(word)) // 2]

        return "".join(word_for_return)
    else:
        return word


def main() -> None:
    text = "The list methods make it very easy to use a list as a stack where the last element added is the first element retrieved"
    print (pemrtuate(text))


if __name__ == "__main__":
    main()
