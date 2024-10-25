import time
import bambulabs_api as bl


EMAIL = 'myemail@gmail.com'
PASSWORD = 'mypassword'
REGION = 'Global'

IP_ADDRESS = '192.168.1.100'
SERIAL = '12309KJBOASF09'
ACCESS_CODE = '123456789'


if __name__ == '__main__':
    print('Starting bambulabs_api example')

    cloud = bl.Cloud(EMAIL, REGION)
    cloud.login(PASSWORD)

    username = cloud.get_username()
    print(f'Username: {username}')

    token = cloud.get_token()
    print(f'Token: {token}')

    devices = cloud.get_devices()
    print(f'Devices: {devices}')

    # Create a new instance of the API
    printer = bl.Printer(IP_ADDRESS, ACCESS_CODE, SERIAL,
                         REGION, username, token)

    # Connect to the Bambulabs 3D printer
    printer.connect()

    # Necessary to wait for the printer to respond
    time.sleep(2)

    # Get the printer status
    status = printer.get_state()
    print(f'Printer status: {status}')

    # Turn the light off
    printer.turn_light_off()

    # Wait for 2 seconds
    time.sleep(2)

    # Turn the light on
    printer.turn_light_on()

    # Disconnect from the Bambulabs 3D printer
    printer.disconnect()

