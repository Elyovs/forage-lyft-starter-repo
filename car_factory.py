from car import Car
from engine.Engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.Battery import Battery
from battery.nubbin import NubbinBattery
from battery.splinder import SplinderBattery


class carFactory(Engine, Battery, Car):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

