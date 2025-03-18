from qr_generator import generate_qr_code
from model_generator import combine_stl_files, qr_to_stl
file1 = './supportingFiles/qrcode_3d.stl'
file2 = './supportingFiles/signBlank.stl'




def main():
    generate_qr_code()
    qr_to_stl()
    combine_stl_files(file1, file2)


main()