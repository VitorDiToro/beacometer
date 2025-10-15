import asyncio
import sys

from scanner.application.scanner import BleakBeaconScanner
from scanner.application.handlers import ConsoleBeaconHandler
from scanner.application.parser import BeaconParser

async def main():
    """
    The main function that sets up and runs the beacon scanner.
    This is the composition root of the application.
    """
    # 1. Create dependencies (the "leaf" objects first)
    parser = BeaconParser()
    handler = ConsoleBeaconHandler()
    
    # 2. Inject dependencies into the main object
    scanner = BleakBeaconScanner(parser)
    
    # 3. Start the application
    try:
        await scanner.start_scan(handler)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScanner stopped by user.")
        sys.exit(0)