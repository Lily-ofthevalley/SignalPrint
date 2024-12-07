import numpy as np
from stl import mesh
from PIL import Image


def qr_to_stl():
    img = Image.open("./Qrcode/QrCode.png").convert('L')
    img_array = np.array(img)

    cube_size = 1.0
    cube_height = 20.0

    vertices = []
    faces = []

    for y in range(img_array.shape[0]):
        for x in range(img_array.shape[1]):
            if img_array[y, x] < 128:
                v0 = [x * cube_size, y * cube_size, 0]
                v1 = [x * cube_size, (y + 1) * cube_size, 0]
                v2 = [(x + 1) * cube_size, (y + 1) * cube_size, 0]
                v3 = [(x + 1) * cube_size, y * cube_size, 0]
                v4 = [x * cube_size, y * cube_size, cube_height]
                v5 = [x * cube_size, (y + 1) * cube_size, cube_height]
                v6 = [(x + 1) * cube_size, (y + 1) * cube_size, cube_height]
                v7 = [(x + 1) * cube_size, y * cube_size, cube_height]

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

    qr_mesh.save('./Qrcode/qrcode_3d.stl')
