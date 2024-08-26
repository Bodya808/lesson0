"""first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as f:
            for item in data_set:
                if isinstance(item, str):
                    f.write(item + '\n')
                else:
                    f.write(str(item) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])"""

import random


class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


# Ваш класс здесь
first_ball = MysticBall(['Да', 'Нет', 'Наверное'])
print(first_ball())
print(first_ball())
print(first_ball())
