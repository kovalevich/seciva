from classes.seciva import Seciva
from numpy import round, set_printoptions

if __name__ == '__main__':

    # создаем экземпляр класс нейронной сети
    # в качестве параметров передам список слоёв сети с количеством нейронов в каждом слое
    s = Seciva([3, 15, 4])

    # входные и выходные данные для обучения
    in_ = [[0, 0, 0],
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 1],
            [1, 1, 1]]
    out_ = [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],]

    # тренировка сети по тренировочным данным на 100000 итераций
    s.train(input_data=in_, output_data=out_, iterations=10000)

    set_printoptions(suppress=True)

    # проверяем результаты тренировки
    print(round(s.solution(in_), 6))