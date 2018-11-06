
import test_package
import math 
import numpy as np

inf = float('inf') 

def test_func_a():
    assert test_package.function_a() == inf
    assert test_package.function_a(angle=180.0) == inf
    assert test_package.function_a(angle=90.0) == 1/np.sqrt(2)
    assert test_package.function_a(angle=-90.0) == 1/np.sqrt(2)
