# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Fish:
    LITTLE = 10
    HIGHT = 100

    def __init__(self, name: str, long: int):
        self.name = name
        self.long = long

    def get_info_fish(self):
        if self.long < self.LITTLE:
            return "Мелководная рыба"
        elif self.long > self.HIGHT:
            return "Глубоководная рыба"
        else:
            return "Средне-глубоководная рыба"


class Bird:
    def __init__(self, name: str, length: int):
        self.name = name
        self.lenght = length

    def wing_span(self):
        return self.lenght * 2


if __name__ == '__main__':
    fish1 = Fish('акула', 50)
    print(fish1.get_info_fish())
    bird1 = Bird('орел', 15)
    print(bird1.wing_span())
