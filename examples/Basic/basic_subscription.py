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

    try:
        while True:
            time.sleep(5)

            # Get the printer status
            status = printer.get_state()
            bed_temperature = printer.get_bed_temperature()
            nozzle_temperature = printer.get_nozzle_temperature()
            print(
                f'Printer status: {status}, Bed temp: {bed_temperature}, '
                f'Nozzle temp: {nozzle_temperature}')

            if env == "debug":
                print("=" * 100)
                print("Printer MQTT Dump")
                print(printer.mqtt_dump())
                print("=" * 100)
    finally:
        # Disconnect from the Bambulabs 3D printer
        printer.disconnect()
