import os
import click
from SignalPrint.utils.project_root import get_project_root
from SignalPrint.utils.wifi_utils import get_wifi_details
import qrcode


def generate_qr_code():
    """Generate a QR code from Wi-Fi details."""
    wifi_data = get_wifi_details()

    project_root = get_project_root()
    supporting_files_dir = os.path.join(project_root, "supportingFiles")

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'{supporting_files_dir}/QrCode.png', "PNG")
    click.secho("QR code generated succesfully", fg='cyan')
