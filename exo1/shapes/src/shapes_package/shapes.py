"""abc is for abstract class"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for all shapes"""

    @abstractmethod
    def __init__(self):
        pass


class Sharp(Shape):
    """Parent class for all sharps class, child of Shape class"""

    def __init__(self, lenght: int):
        """Init for Sharp class with lenght"""
        if lenght < 0:
            raise ValueError
        if not isinstance(lenght, int):
            raise TypeError
        self._lenght = lenght

    @property
    def lenght(self) -> int:
        """Lenght property getter"""
        return self._lenght

    @lenght.setter
    def lenght(self, lenght: int):
        """Lenght property setter"""
        if lenght < 0:
            raise ValueError
        if not isinstance(lenght, int):
            raise TypeError
        self._lenght = lenght


class Rectangle(Sharp):
    """Class for rectangles, child of Sharp class"""
    def __init__(self, lenght: int, width: int):
        """Init for Rectangle class with lenght and width"""
        if width < 0:
            raise ValueError
        if not isinstance(width, int):
            raise TypeError
        self._width = width
        super().__init__(lenght)

    @property
    def width(self) -> int:
        """Width property getter"""
        return self._width

    @width.setter
    def width(self, width: int):
        """Width property setter"""
        if width < 0:
            raise ValueError
        if not isinstance(width, int):
            raise TypeError
        self._width = width

    @property
    def perimeter(self) -> int:
        """Perimeter property getter"""
        return 2*self._width + 2*self._lenght

    @property
    def area(self) -> int:
        """Area property getter"""
        return self._lenght * self._width


class Square(Rectangle):
    """Class for squares, child of Rectangle class"""
    def __init__(self, lenght: int):
        """Init for Square class with lenght"""
        super().__init__(lenght, lenght)

# autres triangles


class Triangle(Sharp):
    """Class for triangles, child of Sharp class"""
    @property
    def perimeter(self) -> int:
        """Perimeter property getter"""
        return 3*self._lenght

    @property
    def area(self) -> float:
        """Area property getter"""
        return (self._lenght**2) / 2


class Circle(Shape):
    """Class for circles, child of Shape class"""
    def __init__(self, ray: int):
        """Init for Circle class with ray"""
        if ray < 0:
            raise ValueError
        if not isinstance(ray, int):
            raise TypeError
        self._ray = ray

    @property
    def ray(self) -> int:
        """Ray property getter"""
        return self._ray

    @ray.setter
    def ray(self, ray: int):
        """Ray property setter"""
        if ray < 0:
            raise ValueError
        if not isinstance(ray, int):
            raise TypeError
        self._ray = ray

    @property
    def perimeter(self) -> float:
        """Perimeter property getter"""
        return 2*math.pi*self._ray

    @property
    def area(self) -> float:
        """Area property getter"""
        return math.pi*(self._ray**2)
