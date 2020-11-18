class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small

    def addCar(self, carType: int) -> bool:
        if carType==1:
            if self.big:
                self.big-=1
                return True
            else:
                return False
        if carType == 2:

            if self.medium:
                self.medium-=1
                return True
            else:
                return False
        if carType == 3:

            if self.small:
                self.small-=1
                return True
            else:
                return False