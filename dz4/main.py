
"""
class proccesor:
    def __init__(self):
        super().__init__()
        self.name = "AMD Ryzen 5 5500"
        self.MHz = 3600

class videocard:
    def __init__(self):
        super().__init__()
        self.name1 = "Rtx 3060"
        self.type = "GDDR6"
        self.MB = 12288
        self.MHzz = 1777

class motherboard:
    def __init__(self):
        super().__init__()
        self.name2 = "ASUS ROG STRIX B550-F GAMING"
        self.socket = "AM4 socket"

class Computer(proccesor, videocard, motherboard):
    def printInfo(self):
        print(f"Computer info:")
        print(f"Proccesor: {self.name}")
        print(f"Mhz: {self.MHz}")
        print(f"Videocard: {self.name1}")
        print(f"Type: {self.type}")
        print(f"Memory: {self.MB}")
        print(f"Mhz: {self.MHzz}")
        print(f"Motherboard {self.name2}")
        print(f"Socket: {self.socket}")

Pc = Computer()
print(Pc.printInfo())
"""

