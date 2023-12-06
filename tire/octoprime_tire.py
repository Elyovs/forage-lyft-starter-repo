from Tire import Tire

class Octoprime(Tire):
    def __init__(self, wear_sensor):
        self.wear1 = wear_sensor[0]
        self.wear2 = wear_sensor[1]
        self.wear3 = wear_sensor[2]
        self.wear4 = wear_sensor[3]
    
    def needs_service(self):
        return (self.wear1 + self.wear2 + self.wear3 + self.wear4) >= 3