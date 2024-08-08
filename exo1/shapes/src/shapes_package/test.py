"""pytest is for testing exception"""
from pytest import raises
from shapes import Rectangle, Square, Triangle, Circle


def test_good_area_rectangle():
    """r.area"""
    r = Rectangle(2, 6)
    assert r.area == 12


def test_good_area_square():
    """s.area"""
    s = Square(3)
    assert s.area == 9


def test_good_area_triangle():
    """t.area"""
    t = Triangle(8)
    assert t.area == 32


def test_good_area_circle():
    """c.area"""
    c = Circle(5)
    assert c.area > 78.5 and c.area < 78.6


def test_good_perimeter_rectangle():
    """r.perimeter"""
    r = Rectangle(2, 6)
    assert r.perimeter == 16


def test_good_perimeter_square():
    """s.perimeter"""
    s = Square(3)
    assert s.perimeter == 12


def test_good_perimeter_triangle():
    """t.perimeter"""
    t = Triangle(8)
    assert t.perimeter == 24


def test_good_perimeter_circle():
    """c.perimeter"""
    c = Circle(5)
    assert c.perimeter > 31.4 and c.perimeter < 31.5


def test_good_settter_rectangle():
    """rectangle setter"""
    r = Rectangle(2, 6)
    r.width = 4
    r.lenght = 8
    assert r.perimeter == 24


def test_good_type_circle_area():
    """c.area type"""
    c = Circle(5)
    assert isinstance(c.area, float)


def test_bad_rectangle_lenght():
    """rectangle lenght negative value"""
    with raises(ValueError):
        Rectangle(-2, 2)


def test_bad_rectangle_width():
    """rectangle width negative value"""
    with raises(ValueError):
        Rectangle(2, -2)


def test_bad_rectangle_all():
    """rectangle all negative value"""
    with raises(ValueError):
        Rectangle(-2, -2)


def test_bad_square_lenght():
    """square negative value"""
    with raises(ValueError):
        Square(-2)


def test_bad_triangle_lenght():
    """triangle negative value"""
    with raises(ValueError):
        Triangle(-2)


def test_bad_circle_lenght():
    """circle negative value"""
    with raises(ValueError):
        Circle(-2)


def test_bad_rectangle_lenght_type():
    """rectangle lenght type"""
    with raises(TypeError):
        Rectangle(2.5, 2)


def test_bad_square_ray_type():
    """square ray type"""
    with raises(TypeError):
        Square("coucou")


def test_bad_triangle_lenght_type():
    """triangle lenght type"""
    with raises(TypeError):
        Triangle((-2, 2))


def test_bad_square_lenght_type():
    """square lenght type"""
    with raises(TypeError):
        Square([2, 15, 48])
