import pandas as pd

from machine_learning.habitatModel import HabitatModel
from machine_learning.heartDiseaseModel import HeartDisease
from machine_learning.radiationExpositionModel import RadiationExpositionModel
from machine_learning.sleepStressModel import SleepStressModel
from machine_learning.waterPotabilityModel import WaterPotabilityModel

from datetime import date

from models import Notification


class MasterClass:
    habitat = None
    heart = None
    radiation = None
    sleep = None
    water = None
    notifications = []
    check_notifications = {"health": {"heart": [-1, None], "radiation": [-1, None], "sleep": [-1, None]},
                           "habitat": {"stress": [-1, None], "water": [-1, None]}}

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
        stress_level, message = self.habitat.decide(habitat_data)

        description = None
        tag = None

        if stress_level == 0:
            tag = 'good'
            description = 'no action needed'
        elif stress_level == 1:
            tag = 'warning'
            description = 'you could try to visit a doctor'
        elif stress_level == 2:
            tag = 'hard warning'
            description = 'there has to be a problem with environmental machines'

        notification = Notification(key=1, name="Habitat Check", date=date.today().strftime("%d/%m/%Y"),
                                    description=description, explanation=message, tags=[tag])
        self.notifications.append(notification)

        self.check_notifications["habitat"]["stress"][0] = 1
        self.check_notifications["habitat"]["stress"][1] = notification

        return stress_level  # self.habitat.decide(habitat_data)

    def heart_decide(self, heart_data: pd.DataFrame):
        heart_level, message = self.heart.decide(heart_data)

        description = None
        tag = None

        if heart_level == 0:
            tag = 'good'
            description = 'no action needed'
        elif heart_level == 1:
            tag = 'warning'
            description = 'you might risk an heart attack'
        elif heart_level == 2:
            tag = 'hard warning'
            description = 'you have to visit a doctor now'

        notification = Notification(key=1, name="Heart Check", date=date.today().strftime("%d/%m/%Y"),
                                    description=description, explanation=message, tags=[tag])
        self.notifications.append(notification)

        self.check_notifications["health"]["heart"][0] = 1
        self.check_notifications["health"]["heart"][1] = notification

        return heart_level

    def radiation_decide(self, radiation_data: pd.DataFrame):

        radiation_level, message = self.radiation.decide(radiation_data)

        description = None
        tag = None

        if radiation_level == 0:
            tag = 'good'
            description = 'no action needed'
        elif radiation_level == 1:
            tag = 'warning'
            description = 'you have to visit a biologist immediately'

        notification = Notification(key=1, name="Radiations Check", date=date.today().strftime("%d/%m/%Y"),
                                    description=description, explanation=message, tags=[tag])
        self.notifications.append(notification)

        self.check_notifications["health"]["radiation"][0] = 1
        self.check_notifications["health"]["radiation"][1] = notification

        return radiation_level

    def sleep_decide(self, sleep_data: pd.DataFrame):
        prediction = self.sleep.decide(sleep_data)

        sleep_level = prediction[0]

        description = None
        tag = None
        message = None

        print("Level of the sleep: ", sleep_level)

        if sleep_level == 0:
            tag = 'good'
            description = 'no action needed'
            message = "Your sleep is not affected by stress"
        elif sleep_level == 1:
            tag = 'warning'
            description = 'maybe you could visit a psychologist'
            message = "Your sleep is affected by stress"
        elif sleep_level == 2:
            tag = 'hard warning'
            description = 'you have to visiti a psychologyst'
            message = 'your sleep is not good at all'
        elif sleep_level == 3:
            tag = 'WARNING'
            description = 'you must visit a psychologist and stop the mission'
            message = 'you haven''t slept for the last 3 weeks'

        notification = Notification(key=1, name="Sleep Check", date=date.today().strftime("%d/%m/%Y"),
                                    description=description, explanation=message, tags=[tag])

        self.notifications.append(notification)
        self.check_notifications["health"]["sleep"][0] = 1
        self.check_notifications["health"]["sleep"][1] = notification

        return prediction

    def water_decide(self, water_data: pd.DataFrame):
        prediction = self.water.decide(water_data)
        water_level = prediction[0]

        description = None
        tag = None
        message = None

        if water_level == 0:
            tag = 'good'
            description = 'no action needed'
            message = "the quality of water is absolutely good"
        elif water_level == 1:
            tag = 'warning'
            description = 'there has to be a problem with water quality'
            message = "pay attention to water quality. Pollution on Mars often happens"

        notification = Notification(key=1, name="Water Check", date=date.today().strftime("%d/%m/%Y"),
                                    description=description, explanation=message, tags=[tag])

        self.notifications.append(notification)
        self.check_notifications["habitat"]["water"][0] = 1
        self.check_notifications["habitat"]["water"][1] = notification

        return prediction
