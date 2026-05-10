import numpy as np


def vector_projection(vectorA, vectorB):

    b_norm_squared = np.dot(vectorB, vectorB)  # element ||b||^2

    if b_norm_squared != 0:
        scalar_part = np.dot(vectorA, vectorB) / b_norm_squared
        projection = scalar_part * vectorB

        return projection

    else:
        return vectorB


A = np.array([3, 4])
B = np.array([1, 0])

print(vector_projection(A, B))