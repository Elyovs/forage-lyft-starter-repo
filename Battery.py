from car import Car
from abc import abstractmethod

class Battery(Car):
    @abstractmethod
    def needs_service(self):
        pass