# from abc import ABC, abstractmethod


# class Car(ABC):
#     def __init__(self, last_service_date):
#         self.last_service_date = last_service_date

#     @abstractmethod
#     def needs_service(self):
#         pass

from Servicable import Servicable
from abc import abstractmethod

class Car(Servicable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    @abstractmethod
    def needs_service(self):
        pass