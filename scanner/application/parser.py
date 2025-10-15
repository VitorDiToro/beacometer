from typing import Optional
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from scanner.domain.beacon import Beacon
import time

class BeaconParser:
    """
    A utility class responsible for parsing raw BLE device data
    into a structured Beacon object.
    It follows the Single Responsibility Principle.
    """
    @staticmethod
    def parse(device: BLEDevice, ad_data: AdvertisementData) -> Optional[Beacon]:
        """
        Parses raw data from Bleak into a Beacon object.
        
        Returns a Beacon object if essential data is present, otherwise None.
        """
        # We consider manufacturer data essential for most beacon types.
        if not ad_data.manufacturer_data:
            return None

        return Beacon(
            address=device.address,
            name=device.name or ad_data.local_name,
            rssi=ad_data.rssi,
            manufacturer_data=next(iter(ad_data.manufacturer_data.values()), None),
            timestamp=time.time()
        )