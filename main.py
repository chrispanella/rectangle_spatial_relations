from rectangle import Rectangle

def main():
    print("Running rectangle-spatial-relations...")

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

    # Compare all rectangles to each other:
    print("Comparing all rectangles to each other:")
    Rectangle.compare_rectangles(rectangles)

    # Intersects rectangles:
    print(Rectangle.intersects(rectA, rectB)) # false
    print(Rectangle.intersects(rectA, rectC)) # false
    print(Rectangle.intersects(rectB, rectD)) # false
    print(Rectangle.intersects(rectB, rectC)) # false
    print(Rectangle.intersects(rectA, rectD)) # false
    print(Rectangle.intersects(rectE, rectF)) # true
    print(Rectangle.intersects(rectE, rectG)) # true

    # Adjacent rectangles:
    print(Rectangle.is_adjacent(rectA, rectB)) # true
    print(Rectangle.is_adjacent(rectA, rectC)) # false
    print(Rectangle.is_adjacent(rectB, rectD)) # true
    print(Rectangle.is_adjacent(rectB, rectC)) # true
    print(Rectangle.is_adjacent(rectA, rectD)) # false
    print(Rectangle.is_adjacent(rectE, rectF)) # false
    print(Rectangle.is_adjacent(rectE, rectG)) # false
    print(Rectangle.is_adjacent(rectH, rectJ)) # true
    print(Rectangle.is_adjacent(rectJ, rectK)) # true
    print(Rectangle.is_adjacent(rectI, rectH)) # true Sub-line adjacent
    print(Rectangle.is_adjacent(rectK, rectL)) # false

    # Contained rectangles:
    print(Rectangle.is_contained(rectA, rectB)) # false
    print(Rectangle.is_contained(rectB, rectD)) # false
    print(Rectangle.is_contained(rectE, rectF)) # false
    print(Rectangle.is_contained(rectF, rectE)) # false
    print(Rectangle.is_contained(rectJ, rectK)) # false
    print(Rectangle.is_contained(rectK, rectL)) # true
    print(Rectangle.is_contained(rectL, rectK)) # true

if __name__ == "__main__":
    main()
