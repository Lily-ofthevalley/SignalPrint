import qrcode
import qrcode.constants
from utils import get_wifi_details


def generate_qr_code():
    """This function generates a qr code image with the wifi data"""
    wifi_data = get_wifi_details()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=1
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("./Qrcode/QrCode.png", "PNG")
