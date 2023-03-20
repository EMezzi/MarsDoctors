import pandas as pd

from machine_learning.habitatModel import HabitatModel
from machine_learning.heartDiseaseModel import HeartDisease
from machine_learning.radiationExpositionModel import RadiationExpositionModel
from machine_learning.sleepStressModel import SleepStressModel
from machine_learning.waterPotabilityModel import WaterPotabilityModel

from models import Notification

class MasterClass:

    habitat = None
    heart = None
    radiation = None
    sleep = None
    water = None
    notifications = []

    def __init__(self):
        self.habitat = HabitatModel()
        self.heart = HeartDisease()
        self.radiation = RadiationExpositionModel()
        self.sleep = SleepStressModel()
        self.water = WaterPotabilityModel()
        notification1 = Notification(key=1, name="Health check ❤", date="10-01-2045", description="No action needed.",
                                     explanation="Longer explanation Longer explanationLonger", tags=['good'])
        notification2 = Notification(key=2, name="Habitat check 🏠", date="11-01-2045", description="No action needed.",
                                     explanation="", tags=["good"])
        notification3 = Notification(key=3, name="Health check ❤", date="12-01-2045", description="No action needed.",
                                     explanation="Detected increasing stress level!", tags=['warning'])
        self.notifications.append(notification1)
        self.notifications.append(notification2)
        self.notifications.append(notification3)


    def habitat_decide(self, habitat_data: pd.DataFrame):
        return self.habitat.decide(habitat_data)

    def heart_decide(self, heart_data: pd.DataFrame):
        return self.heart.decide(heart_data)

    def radiation_decide(self, radiation_data: pd.DataFrame):
        return self.radiation.decide(radiation_data)

    def sleep_decide(self, sleep_data: pd.DataFrame):
        return self.sleep.decide(sleep_data)

    def water_decide(self, water_data: pd.DataFrame):
        return self.water.decide(water_data)


