from importlib import metadata

try:
    __version__ = metadata.version("bambulabs_api")
except Exception:
    __version__ = "0.dev0+unknown"

from .client import Printer  # noqa
from .filament_info import Filament, AMSFilamentSettings, FilamentTray  # noqa
from .states_info import PrintStatus, GcodeState  # noqa
