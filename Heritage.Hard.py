class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__color = color
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)


class Circle(Figure):
    sides_count = 1
    PI = 3.14159

    def __init__(self, color, radius):
        super().__init__(color,radius * 2 * Circle.PI)
        self.__radius = radius

    def get_square(self):
        return Circle.PI * (self.__radius ** 2)


def __len__(self):
    return int(self.__radius * 2 * Circle.PI)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2
        self.__height = (2 / a) * ((s * (s - a) * (s - b) * (s - c)) ** 0.5)

    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, *[side_length] * self.sides_count)
        self.__side_length = side_length

    def get_volume(self):
        return self.__side_length ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
