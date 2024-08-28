import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

a = map(lambda a, b: a == b, first, second)
print(list(a))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8')as file:
            for i in data_set:
                for j in i:
                    file.write(str(j) + '\n')
        with open(file_name, 'r', encoding='utf-8') as file:
            return print(file.read())

    write_everything(write1)
    return write_everything()


write1 = ('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
write = get_advanced_writer('test.txt')


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        rand_word = random.choice(self.words)
        return rand_word


# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

