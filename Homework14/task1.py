"""
Завдання 1.
Створити клас "Транспортний засіб" та його нащадків:
класи Поїзд та Літак (можна більше за бажанням).
В батьківському класі має бути визначено мінімум 1 конструктор, 3 атрибути та 1 метод.
В класах-нащадках мають бути додані мінімум по 1му новому методу та мінімум по 1му новому атрибуту.
Щонайменше по-одному методу має бути перевизначено в класах-нащадках.
Оформлення програми має максимально враховувати усі кращі практики, що обговорювалися на попередніх лекціях.
"""



class Vehicle:
    def __init__(self, name, max_speed=None, altitude=None, weight=None, current_speed=None):
        self.name = name
        self.max_speed = max_speed
        self.altitude = altitude
        self.weight = weight
        self.current_speed = current_speed

    def extra_stop(self):
        self.current_speed = 0
        f" exstra stop {self.name} completed"


class Train(Vehicle):
    pass


class Plain(Vehicle):
    def __init__(self, name, max_speed, altitude, weight, current_speed, max_altitude, max_distance):
        super().__init__(name, max_speed, altitude, weight, current_speed)
        self.max_altitude = max_altitude
        self.max_distance = max_distance

    def extra_stop(self):
        self.altitude = 0
        self.current_speed = 0
        print(f"plane {self.name} lended")


def main():
    plain1 = Plain("plain1", max_speed=800, altitude=8000, weight=50000, current_speed=500, max_altitude=10000,
                   max_distance=5000)

    plain1.extra_stop()

    tr1 = Train("train1", 300, weight=9999999, current_speed=100)
    tr1.extra_stop()


if __name__ == '__main__':
    main()
