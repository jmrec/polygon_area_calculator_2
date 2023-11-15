from math import pi, sqrt

def square(side):
    """
    Number = Int | Float\n
    :: Number -> Float
    """
    return pow(side, 2)

def rectangle(length, width):
    """
    Number = Int | Float\n
    :: Number -> Number -> Float
    """
    return length * width

def triangle(height, base):
    """
    Number = Int | Float\n
    :: Number -> Float
    """
    return (height * base) / 2

def trapezoid(base1, base2, height):
    """
    Number = Int | Float\n
    :: Number -> Number -> Number -> Float
    """
    return ((base1 + base2) * height) / 2

def hexagon(side):
    """
    Number = Int | Float\n
    :: Number -> Float
    """
    return ((3 * sqrt(3)) * pow(side, 2)) / 2

def octagon(side):
    """
    Number = Int | Float\n
    :: Number -> Float
    """
    return ((1 + sqrt(2)) * pow(side, 2)) * 2

def circle(radius):
    """
    Number = Int | Float\n
    :: Number -> Float
    """
    return pi * pow(radius, 2)

def line_break(char="-", length=80):
    """:: Char -> Int -> String"""
    return char * length

def is_too_small(num, limit=0.005):
    """
    Number = Int | Float\n
    :: Number -> Number -> Bool
    """
    return num < limit

def is_too_large(num, limit=10000000):
    """
    Number = Int | Float\n
    :: Number -> Number -> Bool
    """
    return num > limit

def is_a_positive_number(*args):
    """
    Returns False if any argument is invalid, otherwise it will return True\n
    :: a1 -> .. -> an -> Bool
    """
    for argument in args:
        try:
            argument = float(argument)
        except:
            return False
        
        if not argument > 0:
            return False
        
    return True

def is_valid_selection(selection, shape):
    """:: [a] -> a -> Bool"""
    return shape in selection

def selection_as_string(shapes):
    """
    Makes a single-line string showing the selectable shapes\n
    :: [String] -> String
    """
    string = ""
    for each in shapes:
        string += each.capitalize()

        if each != shapes[-1]:
            string += " | "

    return string

def calculation_header(shape):
    """:: String -> String"""
    if shape[0] == "o":
        return f"[You are calculating for the area of an {shape}]"
    else:
        return f"[You are calculating for the area of a {shape}]"

def get_area(mapping, shape, **kwargs):
    """Returns a function based on the shape, then apply the needed parameters using **kwargs"""
    return mapping[shape](**kwargs)