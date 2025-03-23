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
    }
)


def test_get_skipped_objects():
    assert mqtt.get_skipped_objects() == [1, 2, 3]


def test_nozzle_diameter():
    assert mqtt.nozzle_diameter() == 0.4
