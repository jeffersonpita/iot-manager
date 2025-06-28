""" Device classes for IoT management"""

from abc import ABC, abstractmethod
from typing import Optional


class Device(ABC):
    """Abstract base class for IoT devices."""

    def __init__(self, device_id: str, name: str):
        """Initialize a device with an ID and name."""
        self.device_id = device_id
        self.name = name

    @abstractmethod
    def info(self) -> dict:
        """Return current state of the device."""
        raise NotImplementedError

    @abstractmethod
    def modify(self, **kwargs):
        """Modify the state of the device with validation."""
        raise NotImplementedError


class Switch(Device):
    """Represents a simple on/off switch device."""

    def __init__(self, device_id: str, name: str):
        """Initialize a switch with an ID and name."""
        super().__init__(device_id, name)
        self.is_on: bool = False

    def info(self) -> dict:
        """Return the current state of the switch."""
        return {
            "id": self.device_id,
            "name": self.name,
            "type": "Switch",
            "is_on": self.is_on,
        }

    def modify(self, is_on: bool):  # pylint: disable=arguments-differ
        """Modify the state of the switch."""
        self.is_on = is_on


class Dimmer(Device):
    """Represents a dimmer device with adjustable brightness."""

    def __init__(self, device_id: str, name: str):
        """Initialize a dimmer with an ID and name."""
        super().__init__(device_id, name)
        self.level: int = 0  # 0-100

    def info(self) -> dict:
        """Return the current state of the dimmer."""
        return {
            "id": self.device_id,
            "name": self.name,
            "type": "Dimmer",
            "level": self.level,
        }

    def modify(self, level: int):  # pylint: disable=arguments-differ
        """Modify the brightness level of the dimmer."""
        if 0 <= level <= 100:
            self.level = level
        else:
            raise ValueError("Level must be between 0 and 100")


class Lock(Device):
    """Represents a lock device that can be locked or unlocked."""

    def __init__(self, device_id: str, name: str):
        """Initialize a lock with an ID and name."""
        super().__init__(device_id, name)
        self.is_locked: bool = True
        self.pin_code: Optional[str] = None

    def info(self) -> dict:
        """Return the current state of the lock."""
        return {
            "id": self.device_id,
            "name": self.name,
            "type": "Lock",
            "is_locked": self.is_locked,
        }

    def modify(
        self, is_locked: bool, pin_code: Optional[str] = None
    ):  # pylint: disable=arguments-differ
        """Modify the state of the lock."""
        self.is_locked = is_locked
        if pin_code is not None:
            self.pin_code = pin_code


class Thermostat(Device):
    """Represents a thermostat device for temperature control."""

    def __init__(self, device_id: str, name: str):
        """Initialize a thermostat with an ID and name."""
        super().__init__(device_id, name)
        self.temperature: float = 20.0

    def info(self) -> dict:
        """Return the current state of the thermostat."""
        return {
            "id": self.device_id,
            "name": self.name,
            "type": "Thermostat",
            "temperature": self.temperature,
        }

    def modify(self, temperature: float):  # pylint: disable=arguments-differ
        """Modify the temperature setting of the thermostat."""
        self.temperature = temperature
