import math

def vector_between_points(p1, p2):
    """
    Find the vector from p1 -> p2.
    """
    return (p2[0] - p1[0], p2[1] - p1[1])

def dot_product(v1, v2):
    """
    Find the dot product of two 2d vectors.
    """
    return v1[0] * v2[0] + v1[1] * v2[1]

def magnitude(v):
    """
    Find the magnitude of a vector.
    """
    return math.sqrt(v[0] ** 2 + v[1] ** 2)

def angle_between(v1, v2):
    """
    Find the angle between two vectors.
    """
    dot = dot_product(v1, v2)
    mag_v1 = magnitude(v1)
    mag_v2 = magnitude(v2)
    if mag_v1 == 0 or mag_v2 == 0:
        # print("magnitue is 0")
        return 0
    cosine_angle = dot / (mag_v1 * mag_v2)
    cosine_angle = max(min(cosine_angle, 1), -1)
    radians = math.acos(cosine_angle)
    return math.degrees(radians)