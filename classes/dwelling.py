"""Module for managing dwellings and their associated hubs."""

from typing import Dict, List

from .hub import Hub


class Dwelling:
    """Represents a dwelling with its own IoT hubs and devices."""

    def __init__(self, dwelling_id: str, address: str):
        """Initialize a Dwelling instance."""
        self.dwelling_id = dwelling_id
        self.address = address
        self.is_occupied: bool = False
        self.hubs: Dict[str, Hub] = {}

    def occupy(self):
        """Mark the dwelling as occupied."""
        self.is_occupied = True

    def vacate(self):
        """Mark the dwelling as unoccupied."""
        self.is_occupied = False

    def install_hub(self, hub: Hub):
        """Install a hub in the dwelling."""
        if hub.hub_id in self.hubs:
            raise ValueError(f"Hub {hub.hub_id} already installed")
        self.hubs[hub.hub_id] = hub

    def list_hubs(self) -> List[str]:
        """List all installed hubs in the dwelling."""
        return list(self.hubs.keys())
