import os
import numpy as np
from stl import mesh
from PIL import Image
from utils import get_downloads_folder


def qr_to_stl():
    img = Image.open("./supportingFiles/QrCode.png").convert('L')
    img_array = np.array(img)

    cube_size = 1.0 #Size of each cube
    cube_height = 2.5 #Height og each cube
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

def combine_stl_files(file1, file2):
    mesh1 = mesh.Mesh.from_file(file1)
    mesh2 = mesh.Mesh.from_file(file2)
    combined_vertices = np.vstack((mesh1.vectors, mesh2.vectors))
    
    combined_mesh = mesh.Mesh(np.zeros(combined_vertices.shape[0], dtype=mesh.Mesh.dtype))
    combined_mesh.vectors = combined_vertices
    
    downloads_folder = get_downloads_folder()
    stl_file_path = os.path.join(downloads_folder, 'combined.stl')

    combined_mesh.save(stl_file_path)