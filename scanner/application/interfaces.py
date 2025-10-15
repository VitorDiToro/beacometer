from abc import ABC, abstractmethod
from scanner.domain.beacon import Beacon

class IBeaconHandler(ABC):
    """
    Interface for handling detected beacons.
    This allows for different implementations (e.g., printing to console,
    saving to a database, sending to an API).
    """
    @abstractmethod
    def handle(self, beacon: Beacon) -> None:
        """Handles a single parsed beacon."""
        pass

class IBeaconScanner(ABC):
    """
    Interface for the BLE scanning functionality.
    This decouples the main application logic from the specific
    scanning library (e.g., Bleak).
    """
    @abstractmethod
    async def start_scan(self, handler: IBeaconHandler) -> None:
        """Starts the scanning process and uses the handler for each detection."""
        pass