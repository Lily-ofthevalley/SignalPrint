import qrcode
import qrcode.constants
from utils import get_wifi_details


def generate_qr_code():
    wifi_data = get_wifi_details()

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("./supportingFiles/QrCode.png", "PNG")
