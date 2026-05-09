from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
import timeit

def simulate_data(end: int, how_many: int) -> np.ndarray:
    return np.linspace(0, end, how_many, endpoint=False)

print(simulate_data(20, 100))

def simulate_3d(num_dimensions: int = 3, last_number: int = 100, points_per_dimension: int = 10) -> list:
    dims = [simulate_data(last_number, points_per_dimension)for _ in range(num_dimensions)]
    return np.meshgrid(*dims)

def plot_3d(data: list) -> bool:
    if  len(data) != 3:
        return False

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter3D(*data)
    plt.show()
    return True

data = simulate_3d()
plot_3d(data)

