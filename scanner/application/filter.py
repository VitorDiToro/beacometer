# scanner/application/filter.py

from typing import Set, Optional
from pathlib import Path


class BeaconFilter:
    """
    Manages a list of allowed beacon addresses.
    Follows Single Responsibility Principle - only responsible for loading
    and checking if addresses are in the filter list.
    """

    def __init__(self, filter_file: Optional[str] = None):
        self._allowed_addresses: Set[str] = set()
        if filter_file:
            self._load_filter(filter_file)

    def _load_filter(self, filter_file: str) -> None:
        """
        Loads beacon addresses from a file.
        Each line should contain one address.
        Lines starting with # are treated as comments.
        """
        try:
            path = Path(filter_file)
            if not path.exists():
                raise FileNotFoundError(f"Filter file not found: {filter_file}")

            with path.open("r") as f:
                for line_num, line in enumerate(f, 1):
                    # Strip whitespace
                    line = line.strip()

                    # Skip empty lines and comments
                    if not line or line.startswith("#"):
                        continue

                    # Convert to uppercase for consistency
                    address = line.upper()

                    # Basic validation for MAC address format
                    if ":" in address or "-" in address:
                        self._allowed_addresses.add(address)
                    else:
                        print(
                            f"Warning: Invalid address format at line {line_num}: {line}"
                        )

            print(f"Loaded {len(self._allowed_addresses)} addresses from filter file")

        except Exception as e:
            raise RuntimeError(f"Error loading filter file: {e}")

    def is_allowed(self, address: str) -> bool:
        """
        Checks if an address is in the allowed list.
        If no filter is loaded, all addresses are allowed.
        """
        if not self._allowed_addresses:
            return True

        # Normalize address for comparison
        return address.upper() in self._allowed_addresses

    @property
    def is_active(self) -> bool:
        """Returns True if a filter is active (has allowed addresses)."""
        return bool(self._allowed_addresses)
