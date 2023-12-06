from car import Car
from abc import abstractmethod

class Engine(Car):
    @abstractmethod
    def needs_service(self):
        pass