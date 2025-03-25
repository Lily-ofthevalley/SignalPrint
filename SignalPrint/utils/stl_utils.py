import os
import click
from SignalPrint.utils.folder_utils import get_downloads_folder
from SignalPrint.utils.mesh_utils import center_mesh, rotate_mesh, translate_mesh
from SignalPrint.utils.project_root import get_project_root
import numpy as np
from stl import mesh
from PIL import Image


def qr_to_stl():
    """Convert the QR code image to an STL file."""
    project_root = get_project_root()
    supporting_files_dir = os.path.join(project_root, "supportingFiles")

    img = Image.open(f'{supporting_files_dir}/QrCode.png').convert('L')
    img_array = np.array(img)

    cube_size = 1.0  # Size of each cube
    cube_height = 1.5  # Height of each cube
    scale_factor = 1  # Scaling factor to reduce size

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

    qr_mesh.save(f'{supporting_files_dir}/qrcode_3d.stl')
    os.remove(f'{supporting_files_dir}/QrCode.png')
    click.secho("QR code converted to STL succesfully", fg='cyan')

def combine_stl_files(file1, file2):
    """Combine two STL files into one."""
    project_root = get_project_root()
    supporting_files_dir = os.path.join(project_root, "supportingFiles")

    mesh1 = mesh.Mesh.from_file(file1)  # The QrCode
    mesh2 = mesh.Mesh.from_file(file2)  # The sign

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
    stl_file_path = os.path.join(downloads_folder, 'SignalPrint_Sign.stl')

    combined_mesh.save(stl_file_path)
    os.remove(f'{supporting_files_dir}/qrcode_3d.stl')
    click.secho("Combined STL file succesfully", fg='cyan')
