from importlib import metadata

try:
    __version__ = metadata.version("bambulabs_api")
except Exception:
    __version__ = "0.dev0+unknown"

from .client import *  # noqa
from .filament_info import Filament, AMSFilamentSettings, FilamentTray  # noqa
from .states_info import PrintStatus, GcodeState  # noqa
from .mqtt_client import *  # noqa
from .ams import *  # noqa


__all__ = []
__all__.extend(client.__all__)
__all__.extend(mqtt_client.__all__)
__all__.extend(ams.__all__)
