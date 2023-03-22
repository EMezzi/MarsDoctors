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
    check_notifications = {"health": {"heart": False, "radiation": False, "sleep": False},
                           "habitat": {"stress": False, "water": False}}

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
        stress_level, description = self.habitat.decide(habitat_data)

        explanation = None
        tag = None

        if stress_level == 0:
            tag = 'good'
            explanation = 'The stress level is absolutely normal. The system is affirming that Mars'' habitat is not ' \
                          'affecting your stress level'
        elif stress_level == 1:
            tag = 'warning'
            explanation = 'Mars habitat might be responsible for your raised stress level. You should visit a doctor ' \
                          'or a psychologist. For now no need to stop the mission.'
        elif stress_level == 2:
            tag = 'hard warning'
            explanation = 'The system has noticed that your stress level is very high, due to the new planet' \
                          'environment. You have to check yourself, you are not in condition to work.'

        notification = Notification(key=1, name="Habitat Check", date=date.today().strftime("%d/%m/%Y"),
                                    description=description, explanation=explanation, tags=[tag])

        self.check_notifications["habitat"]["stress"] = True
        self.notifications.append(notification)

        return stress_level  # self.habitat.decide(habitat_data)

    def heart_decide(self, heart_data: pd.DataFrame):
        heart_level, description = self.heart.decide(heart_data)

        explanation = None
        tag = None

        if heart_level == 0:
            tag = 'good'
            explanation = 'The system has not found any evidence of a possible heart attack. You are in good shape.'
        elif heart_level == 1:
            tag = 'warning'
            explanation = 'The system has found mild evidence of a possible heart problem. ' \
                          'Go to your Mars cardiologist to have your heart checked'
        elif heart_level == 2:
            tag = 'hard warning'
            explanation = 'You are about to have an heart attack. The doctors will come as soon as possible. Stay ' \
                          'calm and breath deeply, otherwise you''ll only worsen the situation'

        notification = Notification(key=1, name="Heart Check", date=date.today().strftime("%d/%m/%Y"),
                                    description=description, explanation=explanation, tags=[tag])

        self.check_notifications["health"]["heart"] = True
        self.notifications.append(notification)

        return heart_level

    def radiation_decide(self, radiation_data: pd.DataFrame):

        radiation_level, description = self.radiation.decide(radiation_data)

        explanation = None
        tag = None

        if radiation_level == 0:
            tag = 'good'
            explanation = 'Your genes do not show any change in their transcription level. This means that you have ' \
                          'not been exposed to ionizing radiation'
        elif radiation_level == 1:
            tag = 'hard warning'
            explanation = 'Your genes show a change in their transcription level which is above 1%. You have to ' \
                          'immediately visit a biotechnologist to act with CRISPR'

        notification = Notification(key=1, name="Radiations Check", date=date.today().strftime("%d/%m/%Y"),
                                    description=description, explanation=explanation, tags=[tag])

        self.check_notifications["health"]["radiation"] = True
        self.notifications.append(notification)

        return radiation_level

    def sleep_decide(self, sleep_data: pd.DataFrame):
        prediction = self.sleep.decide(sleep_data)

        sleep_level = prediction[0]

        description = None
        tag = None
        explanation = None

        print("Level of the sleep: ", sleep_level)

        if sleep_level == 0:
            tag = 'good'
            description = 'Stress is not affecting your sleep'
            explanation = "All the indicators show that stress is not affecting your sleep. You are integrating well " \
                          "in the new planet environment"
        elif sleep_level == 1:
            tag = 'warning'
            description = 'Stress might be affecting your sleep'
            explanation = "It might be possible that the new environment is causing stress which is affecting your " \
                          "You should visit a psychologist but the situation seems under control"
        elif sleep_level == 2:
            tag = 'hard warning'
            description = 'Stress is affecting your sleep'
            explanation = 'The new environment is causing you a lot of stress. Visit your Mars psychologist to deal ' \
                          'with it'
        elif sleep_level == 3:
            tag = 'DANGER WARNING'
            description = 'Stress is heavily affecting your sleep'
            explanation = 'All the indicators show that you are absolutely stressed and are not integrating in the new ' \
                          'environment. Stop the mission and visit a Mars psychiatrist'

        notification = Notification(key=1, name="Sleep Check", date=date.today().strftime("%d/%m/%Y"),
                                    description=description, explanation=explanation, tags=[tag])

        self.check_notifications["health"]["sleep"] = True
        self.notifications.append(notification)

        return prediction

    def water_decide(self, water_data: pd.DataFrame):
        prediction = self.water.decide(water_data)
        water_level = prediction[0]

        description = None
        tag = None
        explanation = None

        if water_level == 0:
            tag = 'good'
            description = 'The water is potable'
            explanation = "You can drink the purified Mars water, without any problem. No sign of pollution has been " \
                          "detected"
        elif water_level == 1:
            tag = 'warning'
            description = 'Water is not potable'
            explanation = "There is evidence that water is not potable. You will have to drink from the water " \
                          "supplies until the problem will be solved"

        notification = Notification(key=1, name="Water Check", date=date.today().strftime("%d/%m/%Y"),
                                    description=description, explanation=explanation, tags=[tag])

        self.check_notifications["habitat"]["water"] = True
        self.notifications.append(notification)

        return prediction

    def set_habitat_to_false(self):
        for key in self.check_notifications["habitat"].keys():
            self.check_notifications["habitat"][key] = False

    def set_health_to_false(self):
        for key in self.check_notifications["health"].keys():
            self.check_notifications["health"][key] = False
