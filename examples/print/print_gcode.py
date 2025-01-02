from io import BytesIO
import time
import zipfile
import bambulabs_api as bl
import os

IP = '192.168.1.200'
SERIAL = 'AC12309BH109'
ACCESS_CODE = '12347890'

# ============================================================
INPUT_FILE_PATH = 'bambulab_api_example.gcode'
UPLOAD_FILE_NAME = 'bambulab_api_example.3mf'
# ============================================================

env = os.getenv("env", "debug")


def create_zip_archive_in_memory(
        text_content: str,
        text_file_name: str = 'file.txt') -> BytesIO:
    """
    Create a zip archive in memory

    Args:
        text_content (str): content of the text file
        text_file_name (str, optional): location of the text file.
            Defaults to 'file.txt'.

    Returns:
        io.BytesIO: zip archive in memory
    """
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr(text_file_name, text_content)
    zip_buffer.seek(0)
    return zip_buffer


if __name__ == '__main__':
    print('Starting bambulabs_api example')
    print('Connecting to Bambulabs 3D printer')
    print(f'IP: {IP}')
    print(f'Serial: {SERIAL}')
    print(f'Access Code: {ACCESS_CODE}')

    # Create a new instance of the API
    printer = bl.Printer(IP, ACCESS_CODE, SERIAL)

    # Connect to the Bambulabs 3D printer
    printer.connect()

    time.sleep(5)

    with open(INPUT_FILE_PATH, "r") as file:
        gcode = file.read()

    gcode_location = "Metadata/plate_1.gcode"
    io_file = create_zip_archive_in_memory(gcode, gcode_location)
    if file:
        result = printer.upload_file(io_file, UPLOAD_FILE_NAME)
        if "226" not in result:
            print("Error Uploading File to Printer")

        else:
            print("Done Uploading/Sending Start Print Command")
            printer.start_print(UPLOAD_FILE_NAME, 1)
            print("Start Print Command Sent")
