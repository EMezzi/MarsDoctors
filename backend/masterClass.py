import pandas as pd

from machine_learning.habitatModel import HabitatModel
from machine_learning.heartDiseaseModel import HeartDisease
from machine_learning.radiationExpositionModel import RadiationExpositionModel
from machine_learning.sleepStressModel import SleepStressModel
from machine_learning.waterPotabilityModel import WaterPotabilityModel


class MasterClass:

    habitat = None
    heart = None
    radiation = None
    sleep = None
    water = None

    def __init__(self):
        self.habitat = HabitatModel()
        self.heart = HeartDisease()
        self.radiation = RadiationExpositionModel()
        self.sleep = SleepStressModel()
        self.water = WaterPotabilityModel()

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


