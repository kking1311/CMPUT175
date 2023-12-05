
from importlib import invalidate_caches
from importlib import import_module

def load_function(name):
 """
 load_function - imports a module recently created by name
 and returns the function of the same name from inside of it
 name - a string name of the module (not including .py at the end)
 """
 # invalidate_caches is necessary to import any files created after this file started!
 invalidate_caches()
 print(f" Attempting to import {name}...")
 module = import_module(name)
 print(f" Imported!")
 assert hasattr(module, name), f"{name} is missing from {name}.py"
 function = getattr(module, name)
 assert callable(function), f"{name} in {name}.py isn't a function"
 assert type(function) is type(load_function), f"{name} in {name}.py isn't a function"
 return function

def fixed_bubble(size):
    # Generate the function string based on the specified size
    function_str = f"def bubble{size}(a_list):\n"

    # Generate the bubble sort code for the given size
    for bubble in range(size - 1, 0, -1):
        for index in range(bubble):
            function_str += f"    if a_list[{index}] > a_list[{index + 1}]:\n"
            function_str += f"        a_list[{index}], a_list[{index + 1}] = a_list[{index + 1}], a_list[{index}]\n"

    # Add the return statement
    function_str += "    return a_list\n"

    # Write the function to a file
    with open(f"bubble{size}.py", "w") as file:
        file.write(function_str)

def write_py(name, parameters, statements):
    # Form the function string
    assert name!="a3"
    function_str = f"def {name}({', '.join(parameters)}):\n"
    function_str += '\n'.join([f"    {statement}" for statement in statements])
    # Write the function to a file
    with open(f"{name}.py", "w") as file:
        file.write(function_str)

def flip(direction):
    if direction == "<":
        return ">"
    elif direction == ">":
        return "<"
    else:
        return None
    
def greatest_power_of_two_less_than(num):
    power = 1
    while power * 2 < num:
        power *= 2
    return power

def bitonic_merge(a_list, start, end, direction):
    if end - start <= 1:
        return

    distance = (end - start) // 2
    middle = end - distance

    for i in range(start, middle):
        if (direction == "<" and a_list[i] > a_list[i + distance]) or (direction == ">" and a_list[i] < a_list[i + distance]):
            a_list[i], a_list[i + distance] = a_list[i + distance], a_list[i]

    bitonic_merge(a_list, start, middle, direction)
    bitonic_merge(a_list, middle, end, direction)

def fixed_bitonic(size):
    function_str = f"def bitonic{size}(a_list):\n"

    # Generate the bubble sort code for the given size
    for bubble in range(size - 1, 0, -1):
        for index in range(bubble):
            function_str += f"    if a_list[{index}] > a_list[{index + 1}]:\n"
            function_str += f"        a_list[{index}], a_list[{index + 1}] = a_list[{index + 1}], a_list[{index}]\n"

    # Add the return statement
    function_str += "    return a_list\n"

    # Write the function to a file
    with open(f"bitonic{size}.py", "w") as file:
        file.write(function_str)

def bitonic(a_list):
    def bitonic(start, end, direction):
        if end - start <= 1:
            return

        middle = (start + end) // 2
        bitonic(start, middle, "<")
        bitonic(middle, end, ">")
        bitonic_merge(a_list, start, end, direction)

    bitonic(0, len(a_list), ">")

def main():
 write_py("add", ["a", "b"], ["r = a + b", "return r"])
 add = load_function("add")
 assert add(1, 2) == 3
 fixed_bubble(9)

if __name__=="__main__":
   main()