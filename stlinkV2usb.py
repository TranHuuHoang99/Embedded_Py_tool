import usb.core
import time

class StlinkV2usb:
    # device information
    VENDOR_ID = 0x0483
    PRODUCT_ID = 0x3748

    def __init__(self) -> None:
        self.device = None
        devices = usb.core.find(find_all=True)
        for dev in devices:
            if dev.idVendor == StlinkV2usb.VENDOR_ID and dev.idProduct == StlinkV2usb.PRODUCT_ID:
                self.device = dev

    def getDeviceInfo(self):
        print(self.device)

    def _write(self, data, tout = 200):
        self.device.write(0x02, data=data, timeout=tout)
    
    def _read(self, size, tout = 200):
        read_size = size
        if read_size < 64:
            read_size = 64
        elif read_size % 4:
            read_size += 3
            read_size &= 0xffc
        data = self.device.read(0x81, read_size, timeout=tout).tolist()
        return data

    def bulkTransfer(self, cmd, data = None, rx_len = None, retry = 0, tout = 200):
        while True:
            try:
                cmd += [0] * (16 - len(cmd))
                self._write(cmd, tout=tout)
                if rx_len:
                    return self._read(rx_len, tout=tout)
            except:
                if retry:
                    retry -= 1
                    continue
                print("ERROR!!")
            return None
                

if __name__ == "__main__":
    stlink = StlinkV2usb()
    # stlink.getDeviceInfo()
    print(stlink.bulkTransfer([0xf1, 0x80], rx_len=6, retry=2, tout=200))
    print(stlink.bulkTransfer([0xf5], rx_len=2, retry=2, tout=200))
    stlink.bulkTransfer([0xf3, 0x07])
    data = stlink.bulkTransfer([0xf7], rx_len=8, tout=200)
    a0 = int.from_bytes(data[:4], byteorder='little')
    a1 = int.from_bytes(data[4:8], byteorder='little')
    print(a0)
    print(a1)