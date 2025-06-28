""" Tests for Dwelling class functionality """

import pytest

from classes.dwelling import Dwelling
from classes.hub import Hub


def test_occupancy_toggle():
    """Test toggling occupancy status of a dwelling."""
    dw = Dwelling("dw1", "123 Main St")
    # Initially vacant
    assert dw.is_occupied is False

    dw.occupy()
    assert dw.is_occupied is True

    dw.vacate()
    assert dw.is_occupied is False


def test_install_and_list_hubs():
    """Test installing and listing hubs in a dwelling."""
    dw = Dwelling("dw2", "456 Elm St")
    hub = Hub("hub1", "Living Room Hub")

    # No hubs at start
    assert not dw.list_hubs()

    dw.install_hub(hub)
    assert dw.list_hubs() == ["hub1"]

    # Install another and verify both present
    hub2 = Hub("hub2", "Kitchen Hub")
    dw.install_hub(hub2)
    hubs = dw.list_hubs()
    assert set(hubs) == {"hub1", "hub2"}


def test_duplicate_install_raises_value_error():
    """Test that installing the same hub twice raises an error."""
    dw = Dwelling("dw3", "789 Oak St")
    hub = Hub("hubX", "Garage Hub")
    dw.install_hub(hub)

    with pytest.raises(ValueError) as exc:
        dw.install_hub(hub)
    assert "already installed" in str(exc.value)
