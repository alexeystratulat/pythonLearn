"""
Створити клас Годзіла.
При створенні Годзіли вказується об'єм шлунку (параметром конструктора).
Для даного класу написати метод для поїдання людей eat. В даний метод параметром має передаватися об'єм людини для поїдання;
відповідно має зменшитися доступне місце в шлунку.
Коли шлунок заповнюється більше, ніж на 90%, то Годзіла, замість нормальної роботи методу має друкувати повідомлення,
що він вже наївся і зараз не може з'їсти більше людей.
"""


class Godzilla:

    def __init__(self, volume):
        self.volume = volume
        self.free_volume = volume

    def get_free_volume(self):
        return self.free_volume

    def set_free_volume(self, vol_of_people):
        self.free_volume -= vol_of_people
        return self.get_free_volume

    def get_volume(self):
        return self.volume

    def eat(self, vol_of_people):
        if vol_of_people > self.volume * 0.9:
            print("It's too big for me")
        elif vol_of_people > self.get_free_volume():
            print("No more space !")
        else:
            if self.get_free_volume() / self.get_volume() <= 0.1:
                print("I can't eat any more ! ")
            else:
                self.set_free_volume(vol_of_people)


def main():
    dino1 = Godzilla(50)
    dino1.eat(45)
    dino1.eat(5)


if __name__ == "__main__":
    main()
