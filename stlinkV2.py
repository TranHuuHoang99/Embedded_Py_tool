import stlinkV2usb


class stlinkV2:
    STLINK_GET_VERSION = 0xf1


    def __init__(self) -> None:
        ...

    def read_device_version(self):
        ...
