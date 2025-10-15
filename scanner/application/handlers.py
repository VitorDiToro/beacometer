from scanner.application.interfaces import IBeaconHandler
from scanner.domain.beacon import Beacon

class ConsoleBeaconHandler(IBeaconHandler):
    """
    A concrete implementation of IBeaconHandler that prints
    beacon information to the standard output.
    """
    def handle(self, beacon: Beacon) -> None:
        """Prints the string representation of the beacon to the console."""
        print("-" * 40)
        print(beacon)
        print("-" * 40 + "\n")