import math


def circle_area(radius):
    """Return the area of a circle with the given radius.

    >>> round(circle_area(1), 2)
    3.14
    >>> circle_area(0)
    0.0
    >>> round(circle_area(2.5), 2)
    19.63
    """
    return math.pi * radius ** 2


if __name__ == "__main__":
    r = float(input("Radius: "))
    print(f"Area: {circle_area(r):.2f}")