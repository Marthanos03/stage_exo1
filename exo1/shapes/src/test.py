from shapes import Rectangle, Square, Triangle, Circle

r = Rectangle(2, 6)
s = Square(3)
t = Triangle(8)
c = Circle(5)


def test_good_1():
    """r.area"""
    assert r.area == 12


def test_good_2():
    """s.area"""
    assert s.area == 9


def test_good_3():
    """t.area"""
    assert t.area == 32


def test_good_4():
    """c.area"""
    assert c.area > 78.5 and c.area < 78.6


def test_good_5():
    """r.perimeter"""
    assert r.perimeter == 16


def test_good_6():
    """s.perimeter"""
    assert s.perimeter == 12


def test_good_7():
    """t.perimeter"""
    assert t.perimeter == 24


def test_good_8():
    """c.perimeter"""
    assert c.perimeter > 31.4 and c.perimeter < 31.5


def test_good_9():
    """rectangle setter"""
    r.width = 4
    r.lenght = 8
    assert r.perimeter == 24


def test_good_10():
    """c.area type"""
    assert isinstance(c.area, float)


def test_bad_1():
    """rectangle lenght negative value"""
    try:
        Rectangle(-2, 2)
    except ValueError:
        assert True
    else:
        assert False


def test_bad_2():
    """rectangle width negative value"""
    try:
        Rectangle(2, -2)
    except ValueError:
        assert True
    else:
        assert False


def test_bad_3():
    """rectangle all negative value"""
    try:
        Rectangle(-2, -2)
    except ValueError:
        assert True
    else:
        assert False


def test_bad_4():
    """square negative value"""
    try:
        Square(-2)
    except ValueError:
        assert True
    else:
        assert False


def test_bad_5():
    """triangle negative value"""
    try:
        Triangle(-2)
    except ValueError:
        assert True
    else:
        assert False


def test_bad_6():
    """circle negative value"""
    try:
        Circle(-2)
    except ValueError:
        assert True
    else:
        assert False


def test_bad_7():
    """rectangle lenght type"""
    try:
        Rectangle(2.5, 2)
    except TypeError:
        assert True
    else:
        assert False


def test_bad_8():
    """square ray type"""
    try:
        Square("coucou")
    except TypeError:
        assert True
    else:
        assert False


def test_bad_9():
    """triangle lenght type"""
    try:
        Triangle((-2, 2))
    except TypeError:
        assert True
    else:
        assert False


def test_bad_10():
    """square lenght type"""
    try:
        Square([2, 15, 48])
    except TypeError:
        assert True
    else:
        assert False
