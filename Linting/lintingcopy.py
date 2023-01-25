"""
This module provides a function that multiplies a variable by another variable
"""

import numpy as np


def my_function(correctionvariable):
    """Function to calculate a product"""
    get_the_var = correctionvariable
    return np.cos(2.0 * np.pi * get_the_var)
