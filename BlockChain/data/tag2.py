class Storage:
    def __init__(self, storage_volume, temperature, ph):
        self.storage_volume = storage_volume
        self.temperature = temperature
        self.ph = ph

    def get_storage_volume(self):
        return self.storage_volume

    def get_temperature(self):
        return self.temperature

    def get_ph(self):
        return self.ph

    def __str__(self):
        return str(self.storage_volume) + " - " + str(self.temperature) + " - " + str(self.ph)
