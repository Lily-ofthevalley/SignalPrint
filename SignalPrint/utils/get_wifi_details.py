import subprocess


def get_wifi_details():
    # Get general WiFi details
    data = subprocess.check_output(
        (['netsh', 'WLAN', 'show', 'interfaces'])).decode("utf-8")

    ssid, encryption = None, None

    for line in data.splitlines():
        if "SSID" in line and "BSSID" not in line:
            ssid = line.split(":")[1].strip()
        if "Authentication" in line:
            raw_encryption = line.split(":")[1].strip()
            encryption = raw_encryption.split(
                "-", 1)[0] if "-" in raw_encryption else raw_encryption

    if not ssid or not encryption:
        print("Unable to retrieve WiFi details.")
        return None

    # Get the profile and password
    profile_data = subprocess.check_output(
        'netsh wlan show profile "' + ssid + '" key=clear', shell=True).decode('utf-8').splitlines()

    password = None
    for line in profile_data:
        line = line.strip()
        if "Key Content" in line:
            password = line.split(":")[1].strip()
            break

    if not password:
        print("Password not found.")
        return None

    # Create WiFi QR Code text
    qr_code_text = f"WIFI:S:{ssid};T:{encryption};P:{password};;"
    return qr_code_text