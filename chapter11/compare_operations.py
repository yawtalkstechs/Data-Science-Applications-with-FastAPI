import numpy as np
np.random.seed(0)
m = np.random.randint(10, size=1000000)

def standard_double(array):
    output = np.empty(array.size)
    for i in range(array.size):
        output[i] = array[i] * 2
    return output

def numpy_double(array):
    return array * 2