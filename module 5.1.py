class House:
    def __init__(self, name, number_floor):
        self.name = name
        self.number_floor = number_floor
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_floor:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
                


h1 = House('ЖК Эльбрус', 18)
h2 = House('ЖК Мелодия леса', 2)
print(h1.name, h1.number_floor)
print(h2.name, h2.number_floor)
print((h1.go_to(5)))
print(h2.go_to(10))
