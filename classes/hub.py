""" Hub class for managing IoT devices """

from typing import Dict, List

from .devices import Device


class Hub:
    """Represents a hub that manages IoT devices."""

    def __init__(self, hub_id: str, name: str):
        """Initialize a Hub instance."""
        self.hub_id = hub_id
        self.name = name
        self.paired_devices: Dict[str, Device] = {}

    def pair_device(self, device: Device):
        """Pair a device with the hub."""
        if device.device_id in self.paired_devices:
            raise ValueError(f"Device {device.device_id} already paired")
        self.paired_devices[device.device_id] = device

    def remove_device(self, device_id: str):
        """Remove a paired device from the hub."""
        if device_id not in self.paired_devices:
            raise KeyError(f"Device {device_id} not paired")
        del self.paired_devices[device_id]

    def list_devices(self) -> List[dict]:
        """List all paired devices with their current state."""
        return [d.info() for d in self.paired_devices.values()]

    def get_device_state(self, device_id: str) -> dict:
        """Get the current state of a specific device."""
        if device_id not in self.paired_devices:
            raise KeyError(f"Device {device_id} not paired")
        return self.paired_devices[device_id].info()
