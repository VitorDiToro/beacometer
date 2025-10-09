from bleak import BleakScanner
from typing import Dict


class BluetoothScanner:
    def __init__(self, timeout: float = 5.0):
        self.timeout = timeout
    
    async def scan(self) -> Dict:
        devices = await BleakScanner.discover(
            timeout=self.timeout,
            return_adv=True
        )
        return devices