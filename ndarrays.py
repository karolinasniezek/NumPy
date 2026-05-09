from typing import Tuple
import numpy as np
import timeit

def compare_operations(N: int, iters: int) -> Tuple[float, float, float]:
    listOfItems = list(range(N))
    tableOfItems = np.array(N)

    addition_list_of_time = timeit.timeit(lambda: [el + 1 for el in listOfItems], number=iters)
    addition_nparray_of_time = timeit.timeit(lambda: tableOfItems + 1, globals=globals(), number=iters)

    multiplication_list = timeit.timeit(lambda:[el * 1 for el in listOfItems], globals=globals(), number=iters)
    multiplication_ndarray = timeit.timeit(lambda:tableOfItems * 2, globals=globals(), number=iters)

    raising_to_power_list = timeit.timeit(lambda:[el ** 1 for el in listOfItems], globals=globals(), number=iters)
    raising_to_power_nparray = timeit.timeit(lambda:tableOfItems ** 2, globals=globals(), number=iters)

    addition_ratio = addition_list_of_time / addition_nparray_of_time
    multiplication_ratio = multiplication_list / multiplication_ndarray
    raising_to_power_ratio = raising_to_power_list / raising_to_power_nparray

    return round(addition_ratio, 2), round(multiplication_ratio, 2), round(raising_to_power_ratio, 2),


print(compare_operations(10,10))