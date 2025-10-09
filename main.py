import asyncio
from src.scanner import BluetoothScanner
from src.distance_calculator import DistanceCalculator
from src.monitor import SignalMonitor


async def main():
    scanner = BluetoothScanner(timeout=5.0)
    distance_calc = DistanceCalculator(tx_power=-59, path_loss_exponent=2.0)
    monitor = SignalMonitor(scanner, distance_calc)
    
    try:
        await monitor.scan_devices()
        monitor.display_results()
    except PermissionError:
        print("Error: Bluetooth permissions required.")
        print("Try: sudo usermod -aG bluetooth $USER")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())