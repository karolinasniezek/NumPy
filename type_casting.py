import numpy as np


def was_type_changed(func, array1, array2):

    dtype1_before = array1.dtype
    dtype2_before = array2.dtype

    result = func(array1, array2)
    dtype_result = result.dtype

    type_change = dtype1_before != dtype_result or dtype2_before != dtype_result

    return  type_change, dtype1_before, dtype2_before, dtype_result

tab1, tab2, tab3 = np.array(1), np.array(3), np.array(2.5)
print(was_type_changed(np.add, tab1, tab3))

