import sys
import numpy as np
import pytest
sys.path.append('./Functions/')
from my_first_function import my_func_1

def test_one():
    with pytest.raises(TypeError):
        my_func_1("Test")

def test_two():
    assert my_func_1(10) == 20
    assert my_func_1(3.111111111) == pytest.approx(6.222222222)
    
def test_three():
    assert 0.1 + 0.2 == 0.3#pytest.approx(0.3)
    