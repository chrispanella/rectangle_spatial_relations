from dataclasses import dataclass

@dataclass(frozen=True)
class Rectangle:
    x1: float
    y1: float
    x2: float
    y2: float
    name: str

    def __post_init__(self):
        if self.x1 >= self.x2 or self.y1 >= self.y2:
            raise ValueError("INVALID RECTANGLE: x1 must be less than x2 and y1 must be less than y2. Rectangles start at the bottom left and end at the top right.")
            
    
    def test_y(a: "Rectangle", b: "Rectangle"):
        """
        Classifies vertical-edge adjacency between two rectangles that share a
        vertical boundary (i.e. a.x1 == b.x2 or a.x2 == b.x1).

        Prints one of:
        - "sub-line adjacent" if one rectangle's y-span is strictly contained
          within the other's.
        - "partially adjacent" otherwise (y-spans overlap but neither contains
          the other).

        Args:
            a: First rectangle.
            b: Second rectangle.
        """
        if a.y1 < b.y1 and a.y2 > b.y2:
            print(f"Rectangle {b.name} is sub-line adjacent to {a.name}.")
        elif a.y1 > b.y1 and a.y2 < b.y2:
            print(f"Rectangle {a.name} is sub-line adjacent to {b.name}.")
        else:
            print(f"Rectangles {a.name} and {b.name} are partially adjacent.")

    def test_x(a: "Rectangle", b: "Rectangle"):
        """
        Classifies horizontal-edge adjacency between two rectangles that share a
        horizontal boundary (i.e. a.y1 == b.y2 or a.y2 == b.y1).

        Prints one of:
        - "sub-line adjacent" if one rectangle's x-span is strictly contained
          within the other's.
        - "partially adjacent" otherwise (x-spans overlap but neither contains
          the other).

        Args:
            a: First rectangle.
            b: Second rectangle.
        """
        if a.x1 < b.x1 and a.x2 > b.x2:
            print(f"Rectangle {b.name} is sub-line adjacent to {a.name}.")
        elif a.x1 > b.x1 and a.x2 < b.x2:
            print(f"Rectangle {a.name} is sub-line adjacent to {b.name}.")
        else:
            print(f"Rectangles {a.name} and {b.name} are partially adjacent.")
    
    def rectangle_edges(a: "Rectangle"):
        """
        Returns the four edges of the rectangle as line segments.

        Each edge is a tuple of two (x, y) endpoint tuples. The order is
        bottom, right, top, left (counter-clockwise starting from the
        bottom edge).

        Args:
            a: The rectangle whose edges are produced.

        Returns:
            list[tuple[tuple[float, float], tuple[float, float]]]:
                Four edge segments.
        """
        return [
            ((a.x1, a.y1), (a.x2, a.y1)), # bottom
            ((a.x2, a.y1), (a.x2, a.y2)), # right
            ((a.x1, a.y2), (a.x2, a.y2)), # top
            ((a.x1, a.y1), (a.x1, a.y2)), # left
            ]

    def segment_intersection(seg1, seg2):
        """
        Computes the intersection of two axis-aligned line segments.

        Handles all combinations of vertical and horizontal segments:
        perpendicular crossings yield a point, collinear overlaps yield a
        point (if they meet at exactly one endpoint) or a segment.

        Args:
            seg1: First segment as ((x1, y1), (x2, y2)).
            seg2: Second segment as ((x3, y3), (x4, y4)).

        Returns:
            list[tuple[str, tuple]]: A list of intersection results, each
                being either ("point", (x, y)) or
                ("segment", ((x1, y1), (x2, y2))).
                Empty list if the segments do not intersect.
        """
        (x1, y1), (x2, y2) = seg1
        (x3, y3), (x4, y4) = seg2

        seg1_vertical = (x1 == x2)
        seg1_horizontal = (y1 == y2)
        seg2_vertical = (x3 == x4)
        seg2_horizontal = (y3 == y4)

        if seg1_vertical and seg2_horizontal:
            ix = x1
            iy = y3
            if min(y1, y2) <= iy <= max(y1, y2) and min(x3, x4) <= ix <= max(x3, x4):
                return [("point", (ix, iy))]
            return []

        if seg1_horizontal and seg2_vertical:
            ix = x3
            iy = y1
            if min(x1, x2) <= ix <= max(x1, x2) and min(y3, y4) <= iy <= max(y3, y4):
                return [("point", (ix, iy))]
            return []

        if seg1_vertical and seg2_vertical:
            if x1 != x3:
                return []

            overlap_start = max(min(y1, y2), min(y3, y4))
            overlap_end = min(max(y1, y2), max(y3, y4))

            if overlap_start > overlap_end:
                return []
            elif overlap_start == overlap_end:
                return [("point", (x1, overlap_start))]
            else:
                return [("segment", ((x1, overlap_start), (x1, overlap_end)))]

        if seg1_horizontal and seg2_horizontal:
            if y1 != y3:
                return []

            overlap_start = max(min(x1, x2), min(x3, x4))
            overlap_end = min(max(x1, x2), max(x3, x4))

            if overlap_start > overlap_end:
                return []
            elif overlap_start == overlap_end:
                return [("point", (overlap_start, y1))]
            else:
                return [("segment", ((overlap_start, y1), (overlap_end, y1)))]
        return []

    
    def produce_points_of_intersection(a: "Rectangle", b: "Rectangle"):
        """
        Finds all intersection geometry between two rectangles by testing
        every pair of edges (4 x 4 = 16 pairs).

        Results are printed as a dict with three keys:
        - "has_intersection": bool indicating any intersection exists.
        - "points_of_intersection": sorted list of (x, y) intersection points.
        - "segments_of_intersection": sorted list of shared edge segments.

        Args:
            a: First rectangle.
            b: Second rectangle.
        """
        edges1 = Rectangle.rectangle_edges(a)
        edges2 = Rectangle.rectangle_edges(b)

        points_of_intersection = set()
        segments_of_intersection = set()

        for edge1 in edges1:
            for edge2 in edges2:
                intersections = Rectangle.segment_intersection(edge1, edge2)

                for kind, value in intersections:
                    if kind == "point":
                        points_of_intersection.add(value)
                    elif kind == "segment":
                        p1, p2 = value
                        if p2 < p1:
                            p1, p2 = p2, p1
                        segments_of_intersection.add((p1, p2))
        results = {
            "has_intersection": bool(points_of_intersection or segments_of_intersection),
            "points_of_intersection": sorted(points_of_intersection),
            "segments_of_intersection": sorted(segments_of_intersection)
        }

        print(results)

        
    def intersects(a: "Rectangle", b: "Rectangle") -> bool:
        """
        Determines whether two rectangles have overlapping interiors.

        Adjacency (shared edge only) and containment (one fully inside the
        other) are excluded — this returns True only when the interiors
        genuinely cross. When True, also prints the intersection points and
        segments via ``produce_points_of_intersection``.

        Args:
            a: First rectangle.
            b: Second rectangle.

        Returns:
            bool: True if the rectangles' interiors overlap.
        """
        if not (a.x2 <= b.x1 or a.x1 >= b.x2 or a.y2 <= b.y1 or a.y1 >= b.y2) and not (b.x1 >= a.x1 and b.x2 <= a.x2 and b.y1 >= a.y1 and b.y2 <= a.y2):
            Rectangle.produce_points_of_intersection(a, b)
            return True
        else:
            return False

    def is_adjacent(a: "Rectangle", b: "Rectangle") -> bool:
        """
        Determines whether two rectangles share an edge segment.

        Corner-only contact (a single shared point) does not count. When
        adjacency is detected, the kind is printed:
        - *proper* — one shared edge is identical (full side match).
        - *sub-line* — one shared edge is strictly contained within the other's
          (delegated to ``test_x`` / ``test_y``).
        - *partial* — the edges overlap but neither contains the other's
          (also delegated to ``test_x`` / ``test_y``).

        Args:
            a: First rectangle.
            b: Second rectangle.

        Returns:
            bool: True if the rectangles are adjacent along an edge.
        """
        if (a.x1 == b.x1 and a.x2 == b.x2) or (a.y1 == b.y1 and a.y2 == b.y2):
            print(f"Rectangles {a.name} and {b.name} are adjacent proper, they share a side.")
            return True
        elif a.x1 == b.x2 or a.x2 == b.x1:
            Rectangle.test_y(a, b)
            return True
        elif a.y1 == b.y2 or a.y2 == b.y1:
            Rectangle.test_x(a, b)
            return True
        else:
            print(f"Rectangles {a.name} and {b.name} are not adjacent.")
            return False

    def is_contained(a: "Rectangle", b: "Rectangle") -> bool:
        """
        Checks whether rectangle ``a`` lies entirely within rectangle ``b``.

        The check is inclusive: edges of ``a`` may coincide with edges of
        ``b`` and the result is still True.

        Args:
            a: The potentially contained rectangle.
            b: The potentially containing rectangle.

        Returns:
            bool: True if every point of ``a`` is within or on the boundary
                of ``b``.
        """
        return (a.x1 >= b.x1 and a.x2 <= b.x2 and a.y1 >= b.y1 and a.y2 <= b.y2)

    def compare_rectangles(rectangles: list["Rectangle"]):
        """
        Performs a pairwise comparison of all rectangles and prints the
        spatial relationship for every unique pair.

        Each pair is classified (in priority order) as: intersecting,
        adjacent, contained, or apart.

        Args:
            rectangles: List of Rectangle instances to compare.
        """
        n = len(rectangles)
        for i in range(n):
            for j in range(i + 1, n):
                a = rectangles[i]
                b = rectangles[j]
                if Rectangle.intersects(a, b):
                    print(f"Rectangles {a.name} and {b.name} intersect.")
                elif Rectangle.is_adjacent(a, b):
                    print(f"Rectangles {a.name} and {b.name} are adjacent.")
                elif Rectangle.is_contained(a, b):
                    print(f"Rectangle {a.name} is contained within {b.name}.")
                elif Rectangle.is_contained(b, a):
                    print(f"Rectangle {b.name} is contained within {a.name}.")
                else:
                    print(f"Rectangles {a.name} and {b.name} are apart.")