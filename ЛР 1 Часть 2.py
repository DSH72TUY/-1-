# TODO Написать 3 класса с документацией и аннотацией типов
from abc import ABC, abstractmethod

class Chair(ABC):
    def __init__(self, material: str, height: float, width: float):
        """
        "Кресло"

        :param material: Материал, из которого изготовлено кресло
        :param height: Высота кресла в сантиметрах
        :param width: Ширина кресла в сантиметрах

        Примеры:
        >>> chair = Chair("Дерево", 90, 80)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой.")
        if height <= 0:
            raise ValueError("Высота кресла должна быть положительным числом.")
        if width <= 0:
            raise ValueError("Ширина кресла должна быть положительным числом.")

        self.material = material
        self.height = height
        self.width = width

    @abstractmethod
    def recline(self) -> None:
        """
        Откидывание кресла назад.
        Raises:
            NotImplementedError: Если метод не реализован.
        """
        ...

    @abstractmethod
    def adjust_height(self, new_height: float) -> None:
        """
        Настройка высоты кресла.
        :param new_height: Новая высота кресла
        :raise ValueError: Если новая высота не положительное число.
        Примеры:
        >>> chair = Chair("Дерево", 90, 80)
        >>> chair.adjust_height(95)
        """
        ...


class Sofa(ABC):
    def __init__(self, capacity: int, color: str, is_reclinable: bool):
        """
        Объект "Диван"
        :param capacity: Вместимость дивана (количество человек)
        :param color: Цвет дивана
        :param is_reclinable: Может ли диван откидываться

        Примеры:
        >>> sofa = Sofa(3, "Красный", True)  # инициализация экземпляра класса
        """
        if capacity <= 0:
            raise ValueError("Вместимость дивана должна быть положительным числом.")
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой.")

        self.capacity = capacity
        self.color = color
        self.is_reclinable = is_reclinable

    @abstractmethod
    def fold(self) -> None:
        """
        Складывание дивана.
        Raises:
            NotImplementedError: Если метод не реализован.
        """
        ...

    @abstractmethod
    def adjust_capacity(self, new_capacity: int) -> None:
        """
        Настройка вместимости дивана.

        :param new_capacity: Новая вместимость дивана

        :raise ValueError: Если новая вместимость не положительное число.

        Примеры:
        >>> sofa = Sofa(3, "Красный", True)
        >>> sofa.adjust_capacity(4)
        """
        ...


class Bed(ABC):
    def __init__(self, size: str, has_storage: bool, mattress_thickness: float):
        """
        Объект "Кровать"
        :param size: Размер кровати (например, "одиночная", "двуспальная")
        :param has_storage: Наличие места для хранения под кроватью
        :param mattress_thickness: Толщина матраса в сантиметрах

        Примеры:
        >>> bed = Bed("двуспальная", True, 20)  # инициализация экземпляра класса
        """
        if size not in ["одиночная", "двуспальная", "королевская"]:
            raise ValueError("Размер должен быть 'одиночная', 'двуспальная' или 'королевская'.")
        if mattress_thickness <= 0:
            raise ValueError("Толщина матраса должна быть положительным числом.")

        self.size = size
        self.has_storage = has_storage
        self.mattress_thickness = mattress_thickness

    @abstractmethod
    def make_bed(self) -> None:
        """
        Уборка кровати.
        Raises:
            NotImplementedError: Если метод не реализован.
        """
        ...

    @abstractmethod
    def change_mattress(self, new_thickness: float) -> None:
        """
        Замена матраса.

        :param new_thickness: Новая толщина матраса

        :raise ValueError: Если новая толщина не положительное число.

        Примеры:
        >>> bed = Bed("двуспальная", True, 20)
        >>> bed.change_mattress(25)
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации