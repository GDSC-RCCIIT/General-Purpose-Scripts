import bluetooth

print("Searching for Bluetooth Device")
searched_device = bluetooth.discover_devices(lookup_names=True)

for physical_address, device_name in searched_device:
    print("Physical Address: ",physical_address)
    print("Device Name: ",device_name)
    