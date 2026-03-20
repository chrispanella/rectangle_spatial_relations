#test_rectangle.py
from rectangle import Rectangle

"""
Unit tests for the Rectangle class.
"""
rectA = Rectangle(3, 2, 6, 3, "A")
rectB = Rectangle(4, 3, 8, 5, "B")
rectC = Rectangle(8, 2, 9, 4, "C")
rectD = Rectangle(7, 5, 10, 6, "D")
rectE = Rectangle(2, 8, 4, 11, "E")
rectF = Rectangle(3, 8, 6, 9, "F")
rectG = Rectangle(1, 10, 5, 11, "G")
rectH = Rectangle(13, 4, 15, 7, "H")
rectI = Rectangle(15, 5, 18, 6, "I")
rectJ = Rectangle(13, 7, 15, 10, "J")
rectK = Rectangle(15, 7, 20, 10, "K")
rectL = Rectangle(16, 8, 19, 9, "L")

rectangles = [rectA, rectB, rectC, rectD, rectE, rectF, rectG, rectH, rectI, rectJ, rectK, rectL]

def test_intersects():
    """
    Tests the intersects method.
    """
    assert Rectangle.intersects(rectA, rectB) == False
    assert Rectangle.intersects(rectA, rectC) == False
    assert Rectangle.intersects(rectB, rectD) == False
    assert Rectangle.intersects(rectB, rectC) == False
    assert Rectangle.intersects(rectA, rectD) == False
    assert Rectangle.intersects(rectE, rectF) == True
    assert Rectangle.intersects(rectE, rectG) == True
    assert Rectangle.intersects(rectH, rectJ) == False
    assert Rectangle.intersects(rectH, rectK) == False # corner test

def test_is_adjacent():
    """
    Tests the is_adjacent method.
    """
    assert Rectangle.is_adjacent(rectA, rectB) == True
    assert Rectangle.is_adjacent(rectA, rectC) == False
    assert Rectangle.is_adjacent(rectB, rectD) == True
    assert Rectangle.is_adjacent(rectB, rectC) == True
    assert Rectangle.is_adjacent(rectA, rectD) == False
    assert Rectangle.is_adjacent(rectE, rectF) == False
    assert Rectangle.is_adjacent(rectE, rectG) == False
    assert Rectangle.is_adjacent(rectH, rectJ) == True
    assert Rectangle.is_adjacent(rectJ, rectK) == True
    assert Rectangle.is_adjacent(rectI, rectH) == True # Sub-line adjacent
    assert Rectangle.is_adjacent(rectK, rectL) == False

def test_is_contained():
    """
    Tests the is_contained method.
    """
    assert Rectangle.is_contained(rectA, rectB) == False
    assert Rectangle.is_contained(rectB, rectD) == False
    assert Rectangle.is_contained(rectE, rectF) == False
    assert Rectangle.is_contained(rectF, rectE) == False
    assert Rectangle.is_contained(rectJ, rectK) == False
    assert Rectangle.is_contained(rectK, rectL) == False # K is not contained in L
    assert Rectangle.is_contained(rectL, rectK) == True # L is contained in K

def test_all():
    """
    Runs all the tests.
    """
    test_intersects()
    test_is_adjacent()
    test_is_contained()