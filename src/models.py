from dataclasses import dataclass
from datetime import datetime


@dataclass
class BluetoothDevice:
    address: str
    name: str
    rssi_dbm: int
    distance_meters: float
    timestamp: datetime
    
    def __str__(self) -> str:
        return (f"{self.name:<30} {self.address:<20} "
                f"{self.rssi_dbm:>6} dBm  {self.distance_meters:>6.2f} m")