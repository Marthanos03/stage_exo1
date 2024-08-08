"""we need these shapes to test them"""
from shapes import Rectangle, Square, Triangle, Circle

try:
    c = Square(10)
    print(c.area)

    t = Triangle(2)
    print(t.perimeter)

    ci = Circle(5)
    print(ci.area)

    r = Rectangle(2.5, 4)
    print(r.lenght)

except ValueError:
    print("ValueError occured")
except TypeError:
    print("TypeError occured")
