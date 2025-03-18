import os
import numpy as np
from stl import mesh
from PIL import Image
from math import cos, sin, radians
from utils import get_downloads_folder


def qr_to_stl():
    img = Image.open("./supportingFiles/QrCode.png").convert('L')
    img_array = np.array(img)

    cube_size = 1.0 #Size of each cube
    cube_height = 1.5 #Height og each cube
    scale_factor = 1 #Scaling factor to reduce size

    vertices = []
    faces = []

    for y in range(img_array.shape[0]):
        for x in range(img_array.shape[1]):
            if img_array[y, x] < 128:
                v0 = [x * cube_size * scale_factor, y * cube_size * scale_factor, 0]
                v1 = [x * cube_size * scale_factor, (y + 1) * cube_size * scale_factor, 0]
                v2 = [(x + 1) * cube_size * scale_factor, (y + 1) * cube_size * scale_factor, 0]
                v3 = [(x + 1) * cube_size * scale_factor, y * cube_size * scale_factor, 0]
                v4 = [x * cube_size * scale_factor, y * cube_size * scale_factor, cube_height]
                v5 = [x * cube_size * scale_factor, (y + 1) * cube_size * scale_factor, cube_height]
                v6 = [(x + 1) * cube_size * scale_factor, (y + 1) * cube_size * scale_factor, cube_height]
                v7 = [(x + 1) * cube_size * scale_factor, y * cube_size * scale_factor, cube_height]

                start_index = len(vertices)
                vertices.extend([v0, v1, v2, v3, v4, v5, v6, v7])

                faces.extend([
                    [start_index, start_index + 1, start_index + 2],
                    [start_index, start_index + 2, start_index + 3],
                    [start_index + 4, start_index + 5, start_index + 6],
                    [start_index + 4, start_index + 6, start_index + 7],
                    [start_index, start_index + 1, start_index + 5],
                    [start_index, start_index + 5, start_index + 4],
                    [start_index + 2, start_index + 3, start_index + 7],
                    [start_index + 2, start_index + 7, start_index + 6],
                    [start_index + 1, start_index + 2, start_index + 6],
                    [start_index + 1, start_index + 6, start_index + 5],
                    [start_index + 0, start_index + 3, start_index + 7],
                    [start_index + 0, start_index + 7, start_index + 4],
                ])

    vertices = np.array(vertices)
    faces = np.array(faces)

    qr_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            qr_mesh.vectors[i][j] = vertices[f[j]]

    qr_mesh.save('./supportingFiles/qrcode_3d.stl')

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

def translate_mesh(vertices, translation):
    return vertices + translation

def center_mesh(mesh):
    min_coords = np.min(mesh.vectors, axis=(0, 1))
    max_coords = np.max(mesh.vectors, axis=(0, 1))
    center = (min_coords + max_coords) / 2.0
    
    translation = -center
    return translate_mesh(mesh.vectors, translation)

def combine_stl_files(file1, file2):
    mesh1 = mesh.Mesh.from_file(file1) # The QrCode
    mesh2 = mesh.Mesh.from_file(file2) # The sign

    # Center both meshes at the origin
    mesh1.vectors = center_mesh(mesh1)
    mesh2.vectors = center_mesh(mesh2)


    translation1 = np.array([0, 10, 4.5])  # Move mesh1 10 units along the y-axis and 4.5 units along the z-axis
    rotation_x = (78, 0)  # Rotate mesh1 78 degrees around the x-axis


     # Apply transformations to mesh1
    mesh1.vectors = translate_mesh(mesh1.vectors, translation1)
    angle, axis = rotation_x
    mesh1.vectors = rotate_mesh(mesh1.vectors, angle, axis)

    combined_vertices = np.vstack((mesh1.vectors, mesh2.vectors))
    
    combined_mesh = mesh.Mesh(np.zeros(combined_vertices.shape[0], dtype=mesh.Mesh.dtype))
    combined_mesh.vectors = combined_vertices
    
    downloads_folder = get_downloads_folder()
    stl_file_path = os.path.join(downloads_folder, 'combined.stl')

    combined_mesh.save(stl_file_path)