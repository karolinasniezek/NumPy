import numpy as np

def calculate_normal_vector(posA, posB, posC):
    """
       Calculate the normal vector to a plane defined by three points in 3D space.

        Returns:
            A tuple of length 2:
            - normal vector
            - normalized normal vector
        """

    vector1 = posC - posA
    vector2 = posB - posA

    vectorNormal = np.cross(vector1, vector2)

    norm = np.linalg.norm(vectorNormal)
    normalized = vectorNormal / norm if norm != 0 else vectorNormal

    return vectorNormal, normalized


a,b,c = np.array([-1,0,7]), np.array([0,0,7]), np.array([0, -1, 7])

print(calculate_normal_vector(a,b,c))


