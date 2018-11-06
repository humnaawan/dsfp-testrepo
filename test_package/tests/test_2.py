
import test_package

def test_subfunction_b():
    assert test_package.subfunction_b(inp=0) == 1.0
    assert test_package.subfunction_b(inp=1) == 10.0
    
def test_func_b():
    assert test_package.function_b(value=0) == 10.0
    assert test_package.function_b(value=-10) == -11
