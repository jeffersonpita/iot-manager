"""Tests for IoTManager"""

import pytest

from classes.devices import Switch
from classes.dwelling import Dwelling
from classes.hub import Hub
from classes.iot_manager import IoTManager


def test_create_and_get_dwelling():
    """Basic create/get functionality."""
    mgr = IoTManager()
    mgr.create_dwelling("dw1", "123 Main St")
    dw = mgr.get_dwelling("dw1")
    assert isinstance(dw, Dwelling)
    assert dw.address == "123 Main St"
    # get non-existent should raise KeyError
    with pytest.raises(KeyError):
        mgr.get_dwelling("nope")


def test_duplicate_dwelling_raises():
    """Creating a dwelling with the same ID twice errors."""
    mgr = IoTManager()
    mgr.create_dwelling("dw2", "Addr")
    with pytest.raises(ValueError) as exc:
        mgr.create_dwelling("dw2", "Other Addr")
    assert "already exists" in str(exc.value)


def test_list_dwellings_empty_and_populated():
    """list_dwellings returns correct summaries."""
    mgr = IoTManager()
    # initially empty
    assert mgr.list_dwellings() == []

    # add two dwellings
    mgr.create_dwelling("a", "A St")
    mgr.create_dwelling("b", "B Ave")
    summaries = mgr.list_dwellings()
    # must be a list of two dicts
    assert isinstance(summaries, list) and len(summaries) == 2

    # verify each dict has required keys
    for s in summaries:
        assert set(s.keys()) == {"id", "address", "occupied", "hubs"}
        assert s["occupied"] is False
        assert s["hubs"] == []


def test_dwelling_hub_integration_visible_in_list():
    """After installing a hub, list_dwellings shows it under 'hubs'."""
    mgr = IoTManager()
    mgr.create_dwelling("dw3", "789 Oak St")
    dw = mgr.get_dwelling("dw3")
    hub = Hub("hubX", "Garage Hub")
    dw.install_hub(hub)

    summaries = mgr.list_dwellings()
    target = next(s for s in summaries if s["id"] == "dw3")
    assert target["hubs"] == ["hubX"]


def test_full_flow_modify_and_query():
    """End-to-end: occupy, install hub, pair device, then inspect."""

    mgr = IoTManager()
    mgr.create_dwelling("home", "1 Home Rd")
    dw = mgr.get_dwelling("home")
    dw.occupy()

    hub = Hub("hub1", "Main Hub")
    dw.install_hub(hub)

    sw = Switch("sw1", "Light")
    hub.pair_device(sw)
    sw.modify(is_on=True)

    # confirm dwelling summary
    summary = mgr.list_dwellings()[0]
    assert summary["occupied"] is True
    assert summary["hubs"] == ["hub1"]

    # confirm device state via hub
    state = hub.get_device_state("sw1")
    assert state["is_on"] is True
