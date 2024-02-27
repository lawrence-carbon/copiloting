from utils import *

# Take a user name reading as parameter and 
# print a greeting to the user by spelling its name backwards.
def greet_backwards(name):
    backard_name = str_backwards(name)
    print(f"Your name spelled backwards is {backard_name}!")

def compute_average_if_lower_than(range: list, threshold: int):
    """
    Compute and return the average of the numbers in the range that are lower than the threshold.
    Make sure that all values in the range are numbers, otherwise, if it's a string, try to parse it, else, raise a ValueError.
    """
    numbers = []
    for value in range:
        if not isinstance(value, (int, float)):
            try:
                value = float(value)
            except ValueError:
                raise ValueError(f"Value {value} is not a number.")
        if value < threshold:
            numbers.append(value)
    return sum(numbers) / len(numbers)

def print_tree(tree:dict, indent:int=2, depth:int=0):
    """
    tree is a dict of shape:
    {
        "label": "root",
        "children": [
            {
                "label": "child1",
                "children": [
                    {
                        "label": "child1.1",
                        "children": []
                    },
                    {
                        "label": "child1.2",
                        "children": []
    }

    Print the tree with the following format:
    root
      - child1
        - child1.1
        - child1.2
    Where indent is the number of spaces to use for indentation, except for the root.
    """
    print(" " * depth * indent + tree["label"])
    for child in tree["children"]:
        print_tree(child, indent, depth + 1)

def slice_range(range: list, start:int=0, end:int=None):
    """
    Return a new list with the slice of the range.
    """
    result = []
    for idx, value in enumerate(range):
        if idx >= start and (end is None or idx < end):
            result.append(value)
    return result

def print_up_to(range: list, threshold):
    """
    Print the values in the range up to the threshold.
    """
    step=0
    while step < threshold and step < len(range):
        print(range[step])


def main():

    print_up_to([1, 2, 3, 4, 5], "3")

    greet_backwards("John")
    greet_backwards("Alice")
    print(compute_average_if_lower_than([1, 2, 3, 4, 5], 3))
    print(compute_average_if_lower_than([1, 2, 3, "4", 5], 3))

    tree={
        "label": "root",
        "children": [
            {
                "label": "child1",
                "children": [
                    {
                        "label": "child1.1",
                        "children": []
                    },
                    {
                        "label": "child1.2",
                        "children": []
                    }
                ]
            }
        ]
    }
    print_tree(tree)

if __name__ == "__main__":  
    main()