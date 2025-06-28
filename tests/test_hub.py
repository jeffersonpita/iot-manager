"""Tests for Hub"""

import pytest

from classes.devices import Dimmer, Switch
from classes.hub import Hub


def test_hub_pair_and_remove():
    """Test pairing and removing devices from a hub."""
    hub = Hub("h1", "Test Hub")
    sw = Switch("s2", "Hub Switch")
    hub.pair_device(sw)
    assert len(hub.list_devices()) == 1
    hub.remove_device("s2")
    assert hub.list_devices() == []
    with pytest.raises(KeyError):
        hub.remove_device("s2")


def test_pairing_duplicate_device_raises():
    """Pairing the same device twice should error."""
    hub = Hub("h2", "Dup Hub")
    sw = Switch("s3", "Switch 3")
    hub.pair_device(sw)
    with pytest.raises(ValueError) as exc:
        hub.pair_device(sw)
    assert "already paired" in str(exc.value)


def test_get_device_state_success():
    """get_device_state returns the correct info dict."""
    hub = Hub("h3", "State Hub")
    dim = Dimmer("d1", "Dimmer 1")
    hub.pair_device(dim)
    # state should match info()
    expected = dim.info()
    result = hub.get_device_state("d1")
    assert result == expected
    assert result["type"] == "Dimmer"
    assert isinstance(result["level"], int)


def test_get_device_state_missing_raises():
    """Requesting state for an unpaired device should error."""
    hub = Hub("h4", "Empty Hub")
    with pytest.raises(KeyError) as exc:
        hub.get_device_state("nope")
    assert "not paired" in str(exc.value)


def test_list_devices_contains_multiple():
    """list_devices should return a list of info dicts for all paired devices."""
    hub = Hub("h5", "Multi Hub")
    sw = Switch("s5", "Switch 5")
    dim = Dimmer("d6", "Dimmer 6")
    hub.pair_device(sw)
    hub.pair_device(dim)
    infos = hub.list_devices()
    # must contain exactly two entries
    assert isinstance(infos, list) and len(infos) == 2
    ids = {info["id"] for info in infos}
    assert ids == {"s5", "d6"}
