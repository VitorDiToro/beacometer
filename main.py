import asyncio
import sys
import argparse
from typing import Optional

from scanner.application.scanner import BleakBeaconScanner
from scanner.application.handlers import ConsoleBeaconHandler
from scanner.application.parser import BeaconParser
from scanner.application.filter import BeaconFilter
from scanner.application.filtered_handler import FilteredBeaconHandler


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="BLE Beacon Scanner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan all beacons
  python main.py

  # Scan only beacons listed in filter.txt
  python main.py -f filter.txt
        """,
    )

    parser.add_argument(
        "-f",
        "--filter",
        type=str,
        metavar="FILE",
        help="Path to filter file containing allowed beacon addresses (one per line)",
    )

    return parser.parse_args()


async def main():
    """
    The main function that sets up and runs the beacon scanner.
    This is the composition root of the application.
    """
    # Parse command line arguments
    args = parse_arguments()

    # 1. Create dependencies (the "leaf" objects first)
    parser = BeaconParser()
    base_handler = ConsoleBeaconHandler()

    # 2. Setup filter if provided
    handler = base_handler
    filtered_handler: Optional[FilteredBeaconHandler] = None

    if args.filter:
        try:
            beacon_filter = BeaconFilter(args.filter)
            filtered_handler = FilteredBeaconHandler(base_handler, beacon_filter)
            handler = filtered_handler
            print(f"Filter active: {args.filter}")
        except Exception as e:
            print(f"Error setting up filter: {e}", file=sys.stderr)
            sys.exit(1)

    # 3. Inject dependencies into the main object
    scanner = BleakBeaconScanner(parser)

    # 4. Start the application
    try:
        print("Starting BLE scan... Press Ctrl+C to stop.")
        await scanner.start_scan(handler)
    except KeyboardInterrupt:
        if filtered_handler:
            filtered_handler.print_stats()
        print("\nScanner stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
