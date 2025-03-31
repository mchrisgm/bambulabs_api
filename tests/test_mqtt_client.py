"""
Test the Client class
"""

import pytest  # noqa: F401, F403

import bambulabs_api as bl  # noqa: F401, F403

mqtt = bl.PrinterMQTTClient(hostname="", access="", printer_serial="")
mqtt.manual_update(
    {
        "print": {
            "s_obj": [1, 2, 3],
            "nozzle_diameter": "0.4",
        },
        "info": {
            "command": "get_version",
            "sequence_id": "",
            "module": [
                {
                    "name": "ota",
                    "sw_ver": "01.07.00.00",
                },
            ]
        }
    }
)


def test_get_skipped_objects():
    assert mqtt.get_skipped_objects() == [1, 2, 3]


def test_nozzle_diameter():
    assert mqtt.nozzle_diameter() == 0.4


def test_get_firmware():
    assert mqtt.firmware_version() == "01.07.00.00"
    assert mqtt.printer_info.firmware_version == "01.07.00.00"
