from dataclasses import dataclass
from typing import Optional
import time

@dataclass(frozen=True)
class Beacon:
    """
    Represents the core data of a detected BLE beacon.
    This is a pure data class (entity) with no logic.
    'frozen=True' makes instances of this class immutable.
    """
    address: str
    name: Optional[str]
    rssi: int
    manufacturer_data: Optional[bytes]
    timestamp: float

    def __str__(self) -> str:
        """
        Provides a user-friendly string representation of the beacon.
        """
        # Format manufacturer data for better readability
        mfg_data_hex = self.manufacturer_data.hex(':') if self.manufacturer_data else 'N/A'
        
        return (
            f"[{time.ctime(self.timestamp)}] Beacon Found:\n"
            f"  -> Address: {self.address}\n"
            f"  -> Name: {self.name or 'Unknown'}\n"
            f"  -> RSSI: {self.rssi} dBm\n"
            f"  -> Manufacturer Data: {mfg_data_hex}"
        )