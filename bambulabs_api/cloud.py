# Thanks to d0c-stranGE for the initial implementation

from base64 import b64decode
import json
import requests


class Cloud:
    """
    Class to interact with the Bambulabs Cloud API
    """
    def __init__(self, email, region, username=None, token=None):
        self._email = email
        self._region = region
        self._username = username
        self._token = token
        tld = "cn" if self._region == "China" else "com"
        self._api_url = f'https://api.bambulab.{tld}/v1'

    def login(self, password):
        """
        Login to the Bambulabs Cloud API

        Args:
            password (str): The password of the account

        Raises:
            ValueError: If the login fails
        """
        credentials = {'account': self._email, 'password': password}
        res = requests.post(f'{self._api_url}/user-service/user/login',
                            json=credentials, timeout=10)
        if not res.ok:
            raise ValueError(res.status_code)
        self._token = res.json()['accessToken']

        # Extract username from tokens 2nd part
        payload = self._token.split('.')[1]
        # Fix base64 padding
        payload += '=' * ((4 - len(payload) % 4) % 4)
        # Decode string, convert to json and return username
        self._username = json.loads(b64decode(payload))['username']

    def get_token(self) -> str:
        """
        Get the token of the user

        Returns:
            str: The token of the user
        """
        return self._token

    def get_username(self) -> str:
        """
        Get the username of the user

        Returns:
            str: The username of the user
        """
        return self._username

    def get_devices(self) -> list[dict]:
        """
        Get the devices of the user

        Raises:
            ValueError: If the request fails

        Returns:
            list[dict]: The devices of the user as a list of dictionaries
        """
        headers = {'Authorization': 'Bearer ' + self._token}
        res = requests.get(f'{self._api_url}/iot-service/api/user/bind',
                           headers=headers, timeout=10)
        if not res.ok:
            raise ValueError(res.status_code)
        return res.json()['devices']
