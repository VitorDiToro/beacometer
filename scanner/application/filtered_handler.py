# scanner/application/filtered_handler.py

from scanner.application.interfaces import IBeaconHandler
from scanner.application.filter import BeaconFilter
from scanner.domain.beacon import Beacon


class FilteredBeaconHandler(IBeaconHandler):
    """
    A decorator that adds filtering capability to any IBeaconHandler.
    Only beacons with addresses in the filter list will be processed.
    """

    def __init__(self, handler: IBeaconHandler, beacon_filter: BeaconFilter):
        self._handler = handler
        self._filter = beacon_filter
        self._filtered_count = 0
        self._total_count = 0

    def handle(self, beacon: Beacon) -> None:
        """
        Handles a beacon only if it passes the filter.
        """
        self._total_count += 1

        if self._filter.is_allowed(beacon.address):
            self._handler.handle(beacon)
        else:
            self._filtered_count += 1
            # Optionally, you can add debug logging here
            # print(f"Filtered out beacon: {beacon.address}")

    def print_stats(self) -> None:
        """Prints filtering statistics."""
        if self._filter.is_active:
            print(f"\nFiltering Statistics:")
            print(f"  Total beacons detected: {self._total_count}")
            print(f"  Beacons filtered out: {self._filtered_count}")
            print(
                f"  Beacons passed through: {self._total_count - self._filtered_count}"
            )
