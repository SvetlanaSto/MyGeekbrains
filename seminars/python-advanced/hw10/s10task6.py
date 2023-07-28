# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def show_spec(self):
        pass


class Fish(Animal):
    LITTLE = 10
    HIGHT = 100

    def __init__(self, name: str, long: int):
        super().__init__(name)
        self.long = long

    def show_spec(self):
        if self.long < self.LITTLE:
            return "Мелководная рыба"
        elif self.long > self.HIGHT:
            return "Глубоководная рыба"
        else:
            return "Средне-глубоководная рыба"


class Bird(Animal):
    def __init__(self, name: str, length: int):
        super().__init__(name)
        self.lenght = length

    def show_spec(self):
        return self.lenght * 2


fish1 = Fish('акула', 50)
bird1 = Bird('орел', 15)
animal_list = [fish1, bird1]
for animal in animal_list:
    print(animal.show_spec())
