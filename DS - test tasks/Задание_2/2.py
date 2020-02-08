from random import randint
class SearchPoint():
        '''Класс искомой точки'''
        def __init__(self, w, h):
                '''инициализация случайных координат искомой точки'''
                self.__x = randint(0, w)
                self.__y = randint(0, h)
                print(self.__x, self.__y)
        def where_is_point(self, x, y):
                '''Описывает положение искомой точки относительно текущей.
                Возможные варианты: "R", "RU", "RD", "L", "LU", "LD", "U", "D" , ""
                '''
                pos_x = pos_y = ''
                if x > self.__x:
                        pos_x = 'L'
                elif x < self.__x:
                        pos_x = 'R'
                if y > self.__y:
                        pos_y = 'D'
                elif y < self.__y:
                        pos_y = 'U'
                return pos_x+pos_y          
# Создание точки:
w, h = (int(i) for i in input("w h ").split())
x, y = (int(i) for i in input("x0 y0 ").split())
SP = SearchPoint(w, h)
# сравнение текущей точки(x,y) с искомой
position = SP.where_is_point(x,y)
while True:
    if position == '':
        print('Искомая точка: ({0}, {1})'.format(x, y))
        break
    else:
        for i in range(len(position)):
            if position[i] == 'R':
                x += 1
            elif position[i] == 'L':
                x -= 1
            elif position[i] == 'U':
                y += 1
            elif position[i] == 'D':
                y -= 1
    position = SP.where_is_point(x,y)
    print(x,y)