#!/usr/bin/python3

def safe_print_integer(value):
    """Print an int with "{:d}".format().
    Args:
        value (int): The integer to print.
    Returns:
        if a TypeError or ValueError occurs - False
        else - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
