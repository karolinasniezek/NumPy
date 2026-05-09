from typing import Tuple
import numpy as np
import timeit

def simulate_data(end: int, how_many: int) -> np.ndarray:
    return np.linspace(0, end, how_many, endpoint=False)


print(simulate_data(20, 100))
