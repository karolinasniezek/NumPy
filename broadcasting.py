import numpy as np

def chec_broadcasting(tab1, tab2):

    shape1 = tab1.shape
    shape2 = tab2.shape

    #Rule 1: if arrays differ in dimensions, add leading 1s to the smaller array shape.
    if len(shape1) < len(shape2):
        shape1 = (1,) * (len(shape2) - len(shape1)) + shape1
    elif len(shape2) < len(shape1):
        shape2 = (1,) * (len(shape1) - len(shape2)) + shape2

    # Rule 2: if array shapes do not match in a dimension, the array with size 1 in that dimension is stretched to match the other array.

    result_shape = []
    for dim1, dim2 in zip(shape1, shape2):
        if dim1 == dim2:
            result_shape.append(dim1)
        elif dim1 == 1:
            result_shape.append(dim2)
        elif dim2 == 1:
            result_shape.append(dim1)
        else: # Rule 3: if array sizes differ in a dimension and neither array has size 1, a broadcasting error occurs.
            return False
    return True

tab1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

tab2 = np.array([
    [1, 2],
    [3, 4]
])

print(chec_broadcasting(tab1, tab2))