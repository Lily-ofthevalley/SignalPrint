import qrcode
from pathlib import Path
import qrcode.constants
from utils import GetWifiDetails


def GenerateQrCode():
    wifi_data = GetWifiDetails()

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
