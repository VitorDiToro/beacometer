
from datetime import datetime
from typing import List

from .models import BluetoothDevice
from .scanner import BluetoothScanner
from .distance_calculator import DistanceCalculator


class SignalMonitor:
    def __init__(
        self,
        scanner: BluetoothScanner,
        distance_calculator: DistanceCalculator
    ):
        self.scanner = scanner
        self.distance_calculator = distance_calculator
        self.devices: List[BluetoothDevice] = []
    
    async def scan_devices(self) -> List[BluetoothDevice]:
        print(f"Scanning for Bluetooth devices...\n")
        
        discovered = await self.scanner.scan()
        self.devices = []
        
        for device, adv_data in discovered.values():
            rssi = adv_data.rssi
            distance = self.distance_calculator.calculate(rssi)
            
            bt_device = BluetoothDevice(
                address=device.address,
                name=device.name or "Unknown",
                rssi_dbm=rssi,
                distance_meters=distance,
                timestamp=datetime.now()
            )
            self.devices.append(bt_device)
        
        return self.devices
    
    def display_results(self) -> None:
        if not self.devices:
            print("No devices found.")
            return
        
        sorted_devices = sorted(
            self.devices,
            key=lambda d: d.rssi_dbm,
            reverse=True
        )
        
        print(f"{'Device Name':<30} {'Address':<20} {'Signal':<12} {'Distance'}")
        print("-" * 75)
        
        for device in sorted_devices:
            print(device)
        
        print(f"\nTotal devices found: {len(self.devices)}")