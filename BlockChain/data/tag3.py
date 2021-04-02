class Transportation:
    def __init__(self, vehicle_license, vehicle_temperature, transportation_time):
        self.vehicle_license = vehicle_license
        self.vehicle_temperature = vehicle_temperature
        self.transportation_time = transportation_time


    def __str__(self):
        return self.vehicle_license + " - " + str(self.vehicle_temperature) + " - " + self.transportation_time