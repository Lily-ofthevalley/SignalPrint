import click
import os
from SignalPrint.utils.qr_utils import generate_qr_code
from SignalPrint.utils.stl_utils import combine_stl_files, qr_to_stl
from SignalPrint.utils.project_root import get_project_root

@click.group()
def generate_custom_file():
    pass


@generate_custom_file.command()
def generate_custom():
    """Run all steps sequentially: generate QR code, convert to STL, and combine with sign."""
    project_root = get_project_root()
    supporting_files_dir = os.path.join(project_root, "supportingFiles")

    click.secho("\nStarting the generation process...", fg='magenta', bold=True)
    
    # Step 1: Generate QR code
    click.secho("\nGenerating QR code...", fg='blue', bold=True)
    generate_qr_code()
    
    # Step 2: Convert QR code to STL
    click.secho("\nConverting QR code to STL...", fg='blue', bold=True)
    qr_to_stl()
    
    # Step 3: Combine STL files
    click.secho("\nCombining STL files...", fg='blue', bold=True)
    combine_stl_files(f'{supporting_files_dir}/qrcode_3d.stl', f'{supporting_files_dir}/signBlank.stl')
    
    click.secho("\n🎉 Generation process completed successfully! 🎉", fg='magenta', bold=True)

if __name__ == "__main__":
    generate_custom()