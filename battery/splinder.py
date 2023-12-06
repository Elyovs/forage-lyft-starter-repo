from Battery import Battery

class SplinderBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_data = last_service_date
        self.current_service_data = current_date

    def needs_service(self):
        return (self.current_service_data - self.last_service_data) >= 2
