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
        # notification1 = Notification(key=0, name="Stress check❤", date="10-01-2045", description="Check for details!",
        #                              explanation="Mars habitat might be responsible for your raised stress level. You "
        #                                          "should visit a doctor or a psychologist. For now no need to "
        #                                          "stop the mission.", tags=['warning'])
        # notification2 = Notification(key=1, name="Water check 🏠", date="11-01-2045", description="No action needed.",
        #                              explanation="You can drink the purified Mars water, without any problem. No sign "
        #                                          "of pollution has been detected.", tags=["good"])
        # notification3 = Notification(key=2, name="Radiation Check ❤", date="12-01-2045", description="Abnormal "
        #                                                                                              "activity "
        #                                                                                              "detected!",
        #                              explanation="Radiations levels have been increasing, take caution!",
        #                              tags=['warning'])
        # self.notifications.append(notification1)
        # self.notifications.append(notification2)
        # self.notifications.append(notification3)

    def habitat_decide(self, habitat_data: pd.DataFrame):
        stress_level, description = self.habitat.decide(habitat_data)

        explanation = None
        tag = None

        if stress_level == 0:
            tag = 'good'
            explanation = 'The habitat environment on Mars is currently stable and there are no factors that are' \
                          ' significantly affecting your stress level. The system is monitoring for any potential' \
                          ' environmental changes that may impact your physical/ mental wellbeing, and will alert' \
                          ' you if any changes are detected.'
        elif stress_level == 1:
            tag = 'warning'
            explanation = 'Mars habitat might be responsible for your raised stress level. You should visit a doctor ' \
                          'or a psychologist. For now no need to stop the mission.'
        elif stress_level == 2:
            tag = 'hard warning'
            explanation = 'The system has noticed that your stress level is very high, due to the new planet' \
                          'environment. You have to check yourself, you are not in condition to work.'

        notification = Notification(key=len(self.notifications), name="Habitat Check 🏠", date=date.today().strftime("%d/%m/%Y"),
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
            explanation = 'Based on your current physiological indicators, our system has detected that you are at' \
                          ' high risk of experiencing a heart attack. It is important that you remain calm and take' \
                          ' deep breaths to help regulate your heart rate. Medical assistance will be dispatched' \
                          ' immediately to provide you with the necessary treatment and care. For now, take an' \
                          ' aspirin and/or nitroglycerin if possible. '

        notification = Notification(key=len(self.notifications), name="Heart Check ❤", date=date.today().strftime("%d/%m/%Y"),
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
                          'not been exposed to ionizing radiation.'
        elif radiation_level == 1:
            tag = 'hard warning'
            explanation = 'Mars is subject to higher levels of ionizing radiation than what we experience on Earth,' \
                          ' which can have significant health consequences. Our system has detected that you have' \
                          ' been exposed to ionizing radiation, which has resulted in changes to your genes' \
                          ' transcription levels. It is important that you seek immediate treatment to help manage' \
                          ' and mitigate these changes before they lead to further health complications. Either' \
                          ' Thyroshield, Radiogardase, and/or DTPA will be prescribed to reduce radiation damage.' \
                          ' Further monitoring of health is necessary.'

        notification = Notification(key=len(self.notifications), name="Radiations Check ❤", date=date.today().strftime("%d/%m/%Y"),
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
            explanation = 'The stressors of living on Mars can have a significant impact on your sleep quality,' \
                          ' resulting in a range of physical and mental health issues. Our system has detected that' \
                          ' your sleep is being impacted by stress, and we recommend that you schedule an appointment' \
                          ' with a Mars psychologist to help manage and alleviate these symptoms.'
        elif sleep_level == 3:
            tag = 'DANGER WARNING'
            description = 'Stress is heavily affecting your sleep'
            explanation = 'All the indicators show that you are absolutely stressed and are not integrating in the new ' \
                          'environment. Stop the mission and visit a Mars psychiatrist'

        notification = Notification(key=len(self.notifications), name="Sleep Check ❤", date=date.today().strftime("%d/%m/%Y"),
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
            explanation = "The purified Mars water has been tested and found to be potable. The water purification" \
                          "system is designed to remove any contaminants that may be present in the Martian" \
                          " environment, ensuring that the water is of a high quality and free from any harmful" \
                          " pathogens or toxins. The concentrations of impurities, salts, and pH are all tested" \
                          " and reported to be within acceptable ranges."
        elif water_level == 1:
            tag = 'warning'
            description = 'Water is not potable'
            explanation = "There is evidence that water is not potable. You will have to drink from the water " \
                          "supplies until the problem will be solved"

        notification = Notification(key=len(self.notifications), name="Water Check 🏠", date=date.today().strftime("%d/%m/%Y"),
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
