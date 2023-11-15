from functions import *

RED = "\033[1;31m"
GREEN =  "\033[1;32m"
YELLOW = "\033[1;33m"
NOCOLOR = "\033[0m"

INPUT = f"{YELLOW}[INPUT]{NOCOLOR}"
OUTPUT = f"{GREEN}[OUTPUT]{NOCOLOR}"
ERROR = f"{RED}[ERROR]{NOCOLOR}"

mapping = {
    "square": square,
    "rectangle": rectangle,
    "triangle": triangle,
    "trapezoid": trapezoid,
    "hexagon": hexagon,
    "octagon": octagon,
    "circle": circle,
}

# Makes a list of shapes derived from the "mapping" dictionary
shape_selection = list(mapping.keys())

user_wants_to_use_app = True
while user_wants_to_use_app:
    print(line_break())
    print("Welcome To My Area Calculator!".center(80, " "))
    print("First, enter the shape. Then, enter the parameters needed to calculate its area.")
    print(line_break())

    print(selection_as_string(shape_selection).center(80, " "), "\n")
    shape = input(f"{INPUT} Enter shape: ").lower()

    if is_valid_selection(shape_selection, shape):
        print(f"\n{calculation_header(shape).center(80, '~')}")
    else:
        print(f"{ERROR} Please enter a valid shape.\n")
        continue
    
    yet_to_enter_correct_parameter = True
    while yet_to_enter_correct_parameter:
        arguments = {}

        match shape:
            case "square":
                arguments["side"] = input(f"{INPUT} Enter length of side: ")

            case "rectangle":
                arguments["length"] = input(f"{INPUT} Enter length: ")
                arguments["width"] = input(f"{INPUT} Enter width: ")

            case "triangle":
                arguments["base"] = input(f"{INPUT} Enter base: ")
                
            case "trapezoid":
                arguments["base1"] = input(f"{INPUT} Enter base 1: ")
                arguments["base2"] = input(f"{INPUT} Enter base 2: ")
                arguments["height"] = input(f"{INPUT} Enter height: ")
                
            case "hexagon":
                arguments["side"] = input(f"{INPUT} Enter length of side: ")

            case "octagon":
                arguments["side"] = input(f"{INPUT} Enter length of side: ")

            case "circle":
                arguments["radius"] = input(f"{INPUT} Enter radius: ")

        if is_a_positive_number(*arguments.values()):
            yet_to_enter_correct_parameter = False
            values_to_float = {key: float(value) for key, value in arguments.items()}
        else:
            print(f"{ERROR} Inputs must be a positive number.\n")
            continue
        
        area = get_area(mapping, shape, **values_to_float)

        if is_too_small(area) or is_too_large(area):
            print(f"{OUTPUT} The area of the {shape} is", "{:.1e}".format(area))
        else:
            print(f"{OUTPUT} The area of the {shape} is {round(area, 2)}")

        print(line_break(char="~"), "\n")

        invalid_choice = True
        while invalid_choice:
            choice = input(f"{INPUT} Do you want to calculate the area of another shape? [Y/N]: ")
            match choice.upper():
                case "Y":
                    invalid_choice = False
                    print()
                case "N":
                    invalid_choice = False
                    user_wants_to_use_app = False
                case _:
                    print(f"{ERROR} Inputs must be either 'Y' or 'N'.\n")

print(f"{OUTPUT} You have now exited the application. Have a nice day ahead!")