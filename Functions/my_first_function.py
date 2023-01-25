"""
Doubles a single numeric value
"""


def my_func_1(my_val):
    """Takes x and doubles it
    """
    if type(my_val) not in [int, float]:
        raise TypeError("Input my_val must be numeric.")

    return 2 * my_val
