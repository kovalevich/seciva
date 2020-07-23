from typing import overload, List


class Neurone:
    """Класс нейрона"""

    def __init__(self, value: float = 0):
        self.__value = value
        self.__error = 0
        pass

    def value(self, value: float = None) -> float:
        """Реализация сеттера и геттера для поля __value"""
        if value is not None:
            self.__value = value

        return self.__value

    def error(self, value: float = None) -> float:
        """Реализация сеттера и геттера для поля __error"""
        if value is not None:
            self.__error = value

        return self.__error

    def __call__(self, *args, **kwargs) -> float:
        value = kwargs.get('value', None)
        return self.value(value)


class Layer:

    @overload
    def __init__(self, count_neurones: int): pass

    @overload
    def __init__(self, neurones_values: List[float]): pass

    def __init__(self, *args, **kwargs):
        """Конструктор слоя может принимать целое число - количество нейронов в слое,
        либо список значений нейронов. Если парамоетров нет, создается слой без нейронов"""
        neurones = []
        for arg in args:
            if isinstance(arg, int):
                neurones = [Neurone(x) for x in range(arg)]
            if isinstance(arg, List):
                neurones = [Neurone(x) for x in arg]
        self.__neurones = neurones

    def get_list_view(self) -> list:
        """Метод возвращает список значений нейронов сети"""
        return [neurone() for neurone in self.__neurones]


class Seciva:
    """Класс нейросети"""

    def __init__(self, size_in_layer: int, size_out_layer: int):
        self.__in: Layer = Layer(size_in_layer)
        self.__out: Layer = Layer(size_out_layer)

    def solution(self, input_data: list) -> list:
        """Метод возвращает решение нейронной сети для input_data"""
        return self.__out.get_list_view()

    def train(self, input_data, output_data, iterations: int = 1000):
        pass
