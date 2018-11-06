
import numpy as np

def function_d(array1=np.arange(10)*2, array2=np.arange(10), operation='-'):
    """
    Makes a matrix where the [i,j]th element is array1[i] <operation> array2[j]
    """
    if operation == '+':
        return array1[:, np.newaxis] + array2
    elif operation == '-':
        return array1[:, np.newaxis] - array2
    elif operation == '*':
        return array1[:, np.newaxis] * array2
    elif operation == '/':
        return array1[:, np.newaxis] / array2
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
