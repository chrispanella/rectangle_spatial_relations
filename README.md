# Rectangle Spatial Relations

A Python library for analyzing spatial relationships between rectangles. Given a set of rectangles defined by their bottom-left and top-right corners, it determines whether any two rectangles **intersect**, are **adjacent**, are **contained** within one another, or are **apart**.

## Spatial Relations

| Relation | Description |
|---|---|
| **Intersection** | The interiors of two rectangles overlap, producing intersection points and/or shared edge segments. |
| **Adjacency** | Two rectangles share part or all of an edge without their interiors overlapping. Adjacency is further classified as *proper* (entire side shared), *sub-line* (one side is a subset of the other), or *partial* (sides overlap but neither contains the other). |
| **Containment** | One rectangle lies entirely within the bounds of another. |
| **Apart** | No geometric relationship — the rectangles neither touch nor overlap. |

## Rectangle Model

Each rectangle is an immutable dataclass defined by five fields:

| Field | Type | Meaning |
|---|---|---|
| `x1` | `float` | Left edge (min x) |
| `y1` | `float` | Bottom edge (min y) |
| `x2` | `float` | Right edge (max x) |
| `y2` | `float` | Top edge (max y) |
| `name` | `str` | Label used in output |

Coordinates follow the convention `x1 < x2` and `y1 < y2` (bottom-left to top-right). Invalid rectangles raise a `ValueError`.

## Usage

```python
from rectangle import Rectangle

a = Rectangle(3, 2, 6, 3, "A")
b = Rectangle(4, 3, 8, 5, "B")

Rectangle.intersects(a, b)      # False
Rectangle.is_adjacent(a, b)     # True — sub-line adjacent
Rectangle.is_contained(a, b)    # False
```

To compare every pair in a list at once:

```python
rectangles = [a, b]
Rectangle.compare_rectangles(rectangles)
```

## Project Structure

```
rectangle_spatial_relations/
├── rectangle.py          # Rectangle dataclass and all spatial relation methods
├── main.py               # Demo script exercising the API
├── test_rectangle.py     # Unit tests (pytest)
├── pyproject.toml        # Project metadata and dependencies
└── README.md
```

## Requirements

- Python >= 3.12

### Dependencies

Managed via [uv](https://docs.astral.sh/uv/) (see `pyproject.toml`):

- **pytest** — test runner
- **black** — code formatter
- **isort** — import sorter

## Running

```bash
# Run the demo
python main.py

# Run tests
pytest test_rectangle.py
```
