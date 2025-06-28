from classes.devices import Switch
from classes.hub import Hub
from classes.iot_manager import IoTManager


def main():
    mgr = IoTManager()
    # Create and use a dwelling
    mgr.create_dwelling("home1", "123 Main St")
    dw = mgr.get_dwelling("home1")

    # Install a hub and pair a switch
    hub = Hub("hub1", "Living Room Hub")
    dw.install_hub(hub)
    sw = Switch("dev1", "Porch Light")
    hub.pair_device(sw)

    # Toggle state and print
    sw.modify(is_on=True)
    print("Hub State:", hub.list_devices())


if __name__ == "__main__":
    main()
