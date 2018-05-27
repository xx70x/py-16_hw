# Необходимо реализовать классы животных на ферме:

# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:

# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.


class Fauna():
    def __init__(self, name, size):
        self.name = name
        self.size = size

        print(self.name, self.size)


class Birds(Fauna):
    name_bird = ['Утки', 'Куры', 'Гуси']

    def __init__(self, name_bird):
        self.name_bird = name_bird
        Fauna.__init__(self, name_bird, 'small')


class Animal(Fauna):
    name_animal = ['Коровы', 'Козы', 'Овцы', 'Свиньи']

    def __init__(self, name_animal):
        self.name_animal = name_animal
        Fauna.__init__(self, name_animal, 'big')


ducks = Birds('Утки')
chickens = Birds('Куры')
geese = Birds('Гуси')

Cows = Animal('Коровы')
Goats = Animal('Козы')
Sheep = Animal('Овцы')
Pigs = Animal('Свиньи')

# ДЗ пока не готово 

