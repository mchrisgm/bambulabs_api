import time
import bambulabs_api as bl
import os

IP = '192.168.1.200'
SERIAL = 'AC12309BH109'
ACCESS_CODE = '12347890'

env = os.getenv("env", "debug")


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

    image = printer.get_camera_image()
    image.save("example.png")
