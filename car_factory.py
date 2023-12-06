from car import Car
from Engine import Engine
from Battery import Battery
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class carFactory(Engine, Battery, Car):
    def __init__(self, current_date, last_service_data, current_mileage, last_service_mileage):
        super.__init__(Car)
        self.current_date = current_date
        self.last_service_data = last_service_data
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage =current_mileage
        self.last_service_mileage = last_service_mileage
        return Calliope()
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage =current_mileage
        self.last_service_mileage = last_service_mileage
        return Glissade()
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.warning_light_on - warning_light_on
        return Palindrome()
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage =current_mileage
        self.last_service_mileage = last_service_mileage
        return Rorschach()
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage =current_mileage
        self.last_service_mileage = last_service_mileage
        return Thovex()

