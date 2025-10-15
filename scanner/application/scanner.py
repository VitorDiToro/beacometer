import asyncio
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

from scanner.application.interfaces import IBeaconScanner, IBeaconHandler
from scanner.application.parser import BeaconParser


class BleakBeaconScanner(IBeaconScanner):
    """
    An implementation of IBeaconScanner using the Bleak library.
    It encapsulates the logic for scanning and delegation.
    """

    def __init__(self, parser: BeaconParser):
        self._parser = parser
        # Using a set to keep track of discovered devices by address
        # helps in reducing redundant processing if desired,
        # though for beaconing we often want every advertisement.
        self._discovered_devices = set()

    async def start_scan(self, handler: IBeaconHandler) -> None:
        """
        Starts the Bleak scanner and uses a callback to process
        advertisements.
        """

        # The detection callback is a closure, capturing 'handler' and 'self'
        def detection_callback(device: BLEDevice, ad_data: AdvertisementData):
            beacon = self._parser.parse(device, ad_data)
            if beacon:
                # We can add logic here to only handle new beacons
                # or beacons with updated data if needed.
                # For this example, we handle every valid advertisement.
                handler.handle(beacon)

        async with BleakScanner(detection_callback=detection_callback) as scanner:
            # Keep the scanner running indefinitely
            await asyncio.Event().wait()
