from functions import *

# paste "pytest -v main_test.py" to terminal

class TestAreaCalculator:
    class TestInteger:
        def test_square(self):
            assert round(square(5), 2) == 25

        def test_rectangle(self):
            assert round(rectangle(length=5, width=10), 2) == 50

        def test_triangle(self):
            assert round(triangle(height=5, base=10), 2) == 25

        def test_trapezoid(self):
            assert round(trapezoid(base1=5, base2=10, height=15), 2) == 112.5

        def test_hexagon(self):
            assert round(hexagon(side=5), 2) == 64.95

        def test_octagon(self):
            assert round(octagon(side=5), 2) == 120.71

        def test_circle(self):
            assert round(circle(radius=5), 2) == 78.54

    class TestFloat:
        def test_square(self):
            assert round(square(5.69), 2) == 32.38

        def test_rectangle(self):
            assert round(rectangle(length=5.69, width=10.69), 2) == 60.83

        def test_triangle(self):
            assert round(triangle(height=5.69, base=10.69), 2) == 30.41

        def test_trapezoid(self):
            assert round(trapezoid(base1=5.69, base2=10.69, height=15.69), 2) == 128.5

        def test_hexagon(self):
            assert round(hexagon(side=5.69), 2) == 84.12

        def test_octagon(self):
            assert round(octagon(side=5.69), 2) == 156.33

        def test_circle(self):
            assert round(circle(radius=5.69), 2) == 101.71

class TestArgumentValidator:
    class TestValid:
        def test_integer(self):
            assert is_a_positive_number(5) == True

        def test_float(self):
            assert is_a_positive_number(5.69) == True

    class TestInvalid:
        def test_integer(self):
            assert is_a_positive_number(-5) == False

        def test_float(self):
            assert is_a_positive_number(-5.69) == False

        def test_string(self):
            assert is_a_positive_number("5.69y") == False

        def test_zero(self):
            assert is_a_positive_number(0) == False

class TestShapeValidator:
    def test_valid_shape(self):
        assert is_valid_selection(["Star", "Sphere", "Cylinder"], "Sphere") == True

    def test_invalid_shape(self):
        assert is_valid_selection(["Star", "Sphere", "Cylinder"], "Twogon") == False

class TestFormatter:
    class TestNumTooSmall:
        def test_below_limit(self):
            assert is_too_small(0.0049) == True

        def test_above_limit(self):
            assert is_too_small(0.0051) == False

    class TestNumTooLarge:
        def test_below_limit(self):
            assert is_too_large(9999999.99) == False

        def test_above_limit(self):
            assert is_too_large(10000000.01) == True