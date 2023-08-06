import usb.core
import time

VENDOR_ID = 0x0483
PRODUCT_ID = 0x3748

devices = usb.core.find(find_all=True)
_dev = None

for dev in devices:
    if dev.idVendor == VENDOR_ID and dev.idProduct == PRODUCT_ID:
        _dev = dev

print(_dev)
        
cmd = [0xf7]
cmd += [0] * (16 - len(cmd))
_dev.write(0x02, cmd, 200)
data = _dev.read(0x81, 0x40).tolist()
print(data)

