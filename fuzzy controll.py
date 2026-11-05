import numpy as np


def triangle(x, a, b, c):
    """Membership in a triangular fuzzy set."""
    return np.maximum(
        np.minimum((x - a) / (b - a), (c - x) / (c - b)),
        0
    )


def trapezoid(x, a, b, c, d):
    """Membership in a trapezoidal fuzzy set."""
    if a == b:
        rising = 1
    else:
        rising = (x - a) / (b - a)

    if c == d:
        falling = 1
    else:
        falling = (d - x) / (d - c)

    return max(0, min(rising, 1, falling))


def green_time(density, waiting):
    # Membership values for density: low, medium, high
    low_density = trapezoid(density, 0, 0, 10, 15)
    medium_density = triangle(density, 10, 20, 30)
    high_density = trapezoid(density, 25, 50, 50, 50)

    # Membership values for waiting time: short, moderate, long
    short_wait = trapezoid(waiting, 0, 0, 20, 30)
    moderate_wait = triangle(waiting, 20, 50, 80)
    long_wait = trapezoid(waiting, 70, 120, 120, 120)

    # Green output values from 10 to 90 seconds
    green = np.arange(10, 91)
    output = np.zeros(len(green))

    # Each rule has a strength and a green-time category.
    rules = [
        (min(low_density, short_wait), "short"),
        (min(low_density, moderate_wait), "short"),
        (min(low_density, long_wait), "medium"),
        (min(medium_density, short_wait), "short"),
        (min(medium_density, moderate_wait), "medium"),
        (min(medium_density, long_wait), "long"),
        (min(high_density, short_wait), "medium"),
        (min(high_density, moderate_wait), "long"),
        (min(high_density, long_wait), "long"),
    ]

    for strength, category in rules:
        if category == "short":
            shape = np.array([trapezoid(x, 10, 10, 20, 30) for x in green])
        elif category == "medium":
            shape = np.array([triangle(x, 30, 45, 60) for x in green])
        else:
            shape = np.array([trapezoid(x, 60, 75, 90, 90) for x in green])

        # Clip each rule's output, then combine rules.
        output = np.maximum(output, np.minimum(strength, shape))

    # Find the center (weighted average) of the output.
    return np.sum(green * output) / np.sum(output)


# Try four examples
for density, waiting in [(5, 10), (20, 50), (45, 110), (35, 100)]:
    print(f"density={density}, waiting={waiting} -> green={green_time(density, waiting):.1f} s")


