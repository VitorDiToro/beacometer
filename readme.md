# BLE Beacon Scanner

A Bluetooth Low Energy (BLE) beacon scanner built with Python using clean architecture and SOLID principles.

## 📋 Prerequisites

- Python 3.8 or higher
- Operating system with Bluetooth support:
  - **Windows**: Windows 10 build 19041 or higher
  - **macOS**: 10.15 (Catalina) or higher
  - **Linux**: BlueZ 5.43 or higher

## 🔧 Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd BLE
```

### 2. Setup environment

#### Linux (Debian/Ubuntu/Mint based distributions)

Use the automated setup script:

```bash
chmod +x setup.sh
./setup.sh
```

The script will:
- Install pyenv if not present
- Install Python 3.14.0
- Create a virtual environment named `ble`
- Install all dependencies

After running the script, activate the virtual environment:
```bash
source ble/bin/activate
```

#### Windows/macOS/Other Linux distributions

Create and activate a virtual environment manually:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Then install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Permissions (Linux only)

On Linux, you may need to run with sudo or add your user to the bluetooth group:

```bash
sudo usermod -a -G bluetooth $USER
# Log out and log in again to apply changes
```

## 🚀 Usage

### Basic usage - Scan all beacons

```bash
python main.py
```

This command will start the scanner and display all detected BLE beacons.

### Using address filter

```bash
python main.py -f filter.txt
```

This command will only show beacons whose MAC addresses are listed in the `filter.txt` file.

### Command line options

```bash
python main.py -h
```

Available options:
- `-f, --filter FILE`: Specify a file containing allowed MAC addresses

### Stopping the scanner

Press `Ctrl+C` to stop scanning. If using a filter, filtering statistics will be displayed.

## 📁 Project structure

```
BLE
├── main.py                    # Application entry point with CLI argument parsing
├── requirements.txt           # Project dependencies (bleak, etc.)
├── filter.txt                 # Example file with allowed MAC addresses
├── setup.sh                   # Automated setup script for Debian-based Linux
├── scanner                    # Main BLE scanner package
│   ├── application           # Application layer - business logic and use cases
│   │   ├── handlers.py       # Handler implementations for processing detected beacons
│   │   ├── __init__.py       # Exports public classes from application module
│   │   ├── interfaces.py    # Interfaces (contracts) for handlers and scanners
│   │   ├── parser.py        # Parser to convert raw BLE data into Beacon objects
│   │   ├── scanner.py       # Scanner implementation using Bleak library
│   │   ├── filter.py        # MAC address filter management
│   │   └── filtered_handler.py  # Decorator that adds filtering to any handler
│   └── domain               # Domain layer - entities and business rules
│       ├── beacon.py        # Beacon class - represents a detected BLE beacon
│       └── __init__.py      # Exports domain entities
└── README.md                # This file
```

## 📝 Filter file format

The filter file should contain one MAC address per line. Example (`filter.txt`):

```
# Comments are allowed (lines starting with #)
# MAC addresses of allowed beacons

82:00:00:00:02:BA
82:00:00:00:02:BC
82:00:00:00:02:88
AA:BB:CC:DD:EE:FF

# Empty lines are ignored
# Lowercase addresses are automatically normalized
```

## 💻 Output examples

### Without filter:

```
Starting BLE scan... Press Ctrl+C to stop.
----------------------------------------
[Mon Oct 15 10:30:45 2025] Beacon Found:
  -> Address: 82:00:00:00:02:BA
  -> Name: MyBeacon
  -> RSSI: -65 dBm
  -> Manufacturer Data: 4c:00:02:15
----------------------------------------

----------------------------------------
[Mon Oct 15 10:30:46 2025] Beacon Found:
  -> Address: AA:BB:CC:DD:EE:FF
  -> Name: Unknown
  -> RSSI: -72 dBm
  -> Manufacturer Data: N/A
----------------------------------------
```

### With filter:

```
Filter active: filter.txt
Loaded 3 addresses from filter file
Starting BLE scan... Press Ctrl+C to stop.
----------------------------------------
[Mon Oct 15 10:30:45 2025] Beacon Found:
  -> Address: 82:00:00:00:02:BA
  -> Name: MyBeacon
  -> RSSI: -65 dBm
  -> Manufacturer Data: 4c:00:02:15
----------------------------------------

^C
Filtering Statistics:
  Total beacons detected: 15
  Beacons filtered out: 12
  Beacons passed through: 3

Scanner stopped by user.
```

## 🛠️ Troubleshooting

### Error: "No module named 'bleak'"

Make sure you have installed the dependencies:
```bash
pip install -r requirements.txt
```

### Error: "Permission denied" (Linux)

Run with sudo or add your user to the bluetooth group:
```bash
sudo python main.py
```

### Error: "Bluetooth adapter not found"

- Check if Bluetooth is enabled on your system
- Windows: Check in Windows Settings
- macOS: Check in System Preferences
- Linux: Use `bluetoothctl power on`

### No beacons detected

- Verify there are active BLE beacons nearby
- Some beacons may have long intervals between transmissions
- Try without filter first to check if any beacon is being detected

## 📚 Dependencies

- **[Bleak](https://github.com/hbldh/bleak)**: Cross-platform Python library for BLE communication
- **asyncio**: Support for asynchronous programming (Python standard library)
- **argparse**: Command-line argument parser (Python standard library)

## 📄 License

This project is licensed under the MIT License:
