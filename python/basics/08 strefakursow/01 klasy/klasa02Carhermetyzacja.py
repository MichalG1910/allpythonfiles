class Car:
    def __init__(self, luquid = 0):
        self.tank = luquid

    def setTank(self, liquid, unit = "L"):
        if unit.upper() == "L":
            self.tank = liquid
        elif unit.upper() == "G":
            self.tank = liquid / 0.26417
        else:
            self.tank = liquid

    def getTank(self, unit = "L"):
        if unit.upper() == "L":
            return self.tank
        elif unit.upper() == "G":
            return self.tank * 0.26417
        else:
            return self.tank

       
