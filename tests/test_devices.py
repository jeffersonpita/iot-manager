"""Tests for IoT devices"""

import pytest

from classes.devices import Dimmer, Lock, Switch, Thermostat


def test_switch_on_off():
    """Test the on/off functionality of a switch."""
    sw = Switch("s1", "Test Switch")
    assert sw.info()["is_on"] is False
    sw.modify(is_on=True)
    assert sw.info()["is_on"] is True


def test_dimmer_bounds():
    """Test the bounds of a dimmer's brightness level."""
    dm = Dimmer("d1", "Test Dimmer")
    dm.modify(level=50)
    assert dm.info()["level"] == 50
    with pytest.raises(ValueError):
        dm.modify(level=150)


def test_lock_modify():
    """Test modifying the state of a lock."""
    lk = Lock("l1", "Test Lock")
    assert lk.info()["is_locked"] is True
    lk.modify(is_locked=False)
    assert lk.info()["is_locked"] is False
    lk.modify(is_locked=True, pin_code="1234")
    assert lk.pin_code == "1234"


def test_thermostat():
    """Test modifying the temperature of a thermostat."""
    th = Thermostat("t1", "Test Thermostat")
    th.modify(temperature=22.5)
    assert th.info()["temperature"] == 22.5
