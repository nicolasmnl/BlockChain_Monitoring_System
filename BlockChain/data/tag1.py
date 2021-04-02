from datetime import datetime


class WithdrawalRecord:
    def __init__(self, animal_record, volume,date, withdrawal_time):
        self.animalRecord = animal_record
        self.volume = volume
        self.date = date
        self.withdrawal_time = withdrawal_time

    def get_date(self):
        return self.date

    def get_volume(self):
        return self.volume

    def get_animal_record(self):
        return self.animalRecord

    def get_withdrawal_time(self):
        return self.withdrawal_time

    def __str__(self):
        return self.animalRecord + " - " + str(self.volume) + " - " + self.date + " - " + self.withdrawal_time
