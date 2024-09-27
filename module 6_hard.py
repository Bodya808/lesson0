class Figure:
    sides_count = 0
    valid_sides = 0
    is_cube = False

    def __init__(self, color, *sides, filled=False):
        self.__sides = []
        self.__color = list(color)
        self.filled = filled
        if self.is_cube:
            if len(sides) == 1:
                for i in range(self.sides_count):
                    self.__sides.append(*sides)
            else:
                for i in range(self.sides_count):
                    self.__sides.append(1)
        else:
            if len(sides) == self.sides_count:
                self.__sides = list(sides)
            else:
                for i in range(self.sides_count):
                    self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, new_color):
        for i in new_color:
            if i < 0 or i > 255 or not isinstance(i, int):
                return False
        return True

    def set_color(self, r, g, b):
        new_color = [r, g, b]
        validation = self.__is_valid_color(new_color)
        if validation:
            self.__color = new_color

    def __is_valid_sides(self, new_sides):
        for i in new_sides:
            if i <= 0:
                return False

        if len(new_sides) != self.valid_sides:
            return False
        else:
            return True

    def set_sides(self, *sides):
        new_sides = sides
        validation = self.__is_valid_sides(new_sides)
        if validation:
            if self.is_cube:
                self.__sides = []
                for i in range(self.sides_count):
                    self.__sides.append(*new_sides)
            else:
                self.__sides = list(sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        res = sum(self.__sides)
        return res


class Circle(Figure):
    sides_count = 1
    valid_sides = sides_count

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = len(self) / 6.28

    def get_square(self):
        s = 3.14 * (self.__radius ** 2)
        return s


class Triangle(Figure):
    sides_count = 3
    valid_sides = sides_count

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        p = len(self) / 2
        sides = self.get_sides()
        self.side_a = sides[0]
        self.__height = (2 * (p * (p - sides[0]) * (p - sides[1]) *
                              (p - sides[2])) ** 0.5) / sides[0]

    def get_square(self):
        s = 0.5 * self.side_a * self.__height
        return s


class Cube(Figure):
    sides_count = 12
    is_cube = True
    valid_sides = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        cube_side = self.get_sides()[0]
        res = cube_side ** 3
        return res


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())