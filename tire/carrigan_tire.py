from Tire import Tire

class Carrigan(Tire):
    def __init__(self, wear_sensor):
        self.wear1 = wear_sensor[0]
        self.wear2 = wear_sensor[1]
        self.wear3 = wear_sensor[2]
        self.wear4 = wear_sensor[3]
    
    def needs_service(self):
        return self.wear1 >= 0.9 or self.wear2 >= 0.9 or self.wear3 >= 0.9 or self.wear4 >= 0.9