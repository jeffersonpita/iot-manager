"""" IoTManager class for managing dwellings and their IoT hubs and devices."""

from typing import Dict, List

from .dwelling import Dwelling


class IoTManager:
    """Manager for multiple dwellings, each with its own IoT hubs and devices."""

    def __init__(self):
        """Initialize the IoT Manager with an empty dwellings dictionary."""
        self.dwellings: Dict[str, Dwelling] = {}

    def create_dwelling(self, dwelling_id: str, address: str):
        """Create a new dwelling with the given ID and address."""
        if dwelling_id in self.dwellings:
            raise ValueError("Dwelling already exists")
        self.dwellings[dwelling_id] = Dwelling(dwelling_id, address)

    def get_dwelling(self, dwelling_id: str) -> Dwelling:
        """Retrieve a dwelling by its ID."""
        return self.dwellings[dwelling_id]

    def list_dwellings(self) -> List[dict]:
        """List all dwellings with their basic information."""
        return [
            {
                "id": d.dwelling_id,
                "address": d.address,
                "occupied": d.is_occupied,
                "hubs": d.list_hubs(),
            }
            for d in self.dwellings.values()
        ]
