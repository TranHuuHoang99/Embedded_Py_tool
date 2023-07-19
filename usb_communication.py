import usb

VENDOR_ID = 0x0483
PRODUCT_ID = 0x3748

reader = None
buses = usb.busses()
for bus in buses:
    for device in bus.devices:
        if device.idVendor == VENDOR_ID and device.idProduct == PRODUCT_ID:
            reader = device

if not reader:
    print("Device not found.")
    exit(0)

print("Device connected.")

readerHandler = reader.open()
readerHandler.bulkRead(0x81, 0x40, timeout=100)

exit(1)