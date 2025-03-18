from math import cos, radians, sin
import numpy as np


def rotate_mesh(vertices, angle_degrees, axis):
    angle_radians = radians(angle_degrees)
    if axis == 0:  # Rotate around x-axis
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, cos(angle_radians), -sin(angle_radians)],
            [0, sin(angle_radians), cos(angle_radians)]
        ])
    elif axis == 1:  # Rotate around y-axis
        rotation_matrix = np.array([
            [cos(angle_radians), 0, sin(angle_radians)],
            [0, 1, 0],
            [-sin(angle_radians), 0, cos(angle_radians)]
        ])
    elif axis == 2:  # Rotate around z-axis
        rotation_matrix = np.array([
            [cos(angle_radians), -sin(angle_radians), 0],
            [sin(angle_radians), cos(angle_radians), 0],
            [0, 0, 1]
        ])
    return np.dot(vertices, rotation_matrix.T)
