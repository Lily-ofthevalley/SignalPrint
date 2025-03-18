import numpy as np
from SignalPrint.utils import translate_mesh


def center_mesh(mesh):
    min_coords = np.min(mesh.vectors, axis=(0, 1))
    max_coords = np.max(mesh.vectors, axis=(0, 1))
    center = (min_coords + max_coords) / 2.0
    
    translation = -center
    return translate_mesh(mesh.vectors, translation)