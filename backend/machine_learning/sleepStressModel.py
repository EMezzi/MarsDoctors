"""
This class manages the prediction about the stress during the sleep.
"""

import joblib
import pandas as pd


class SleepStressModel:
    version = None
    classifier = None
    dataset: pd.DataFrame = None

    def __init__(self, version: str = "latest"):
        self.version = version
        if version == "latest":
            try:
                # Load latest model and data
                self.classifier = joblib.load('machine_learning/model_data/sleep_random_forest_model.joblib')
                self.dataset = pd.read_csv("../datasets/habitat/Sleep_Stress.csv")
            except Exception as e:
                print("Error when loading data and model: ", e)
        else:
            raise Exception("No other models saved for this task!")

    def __predict(self, sleep_stress_data: pd.DataFrame):
        """
        :param sleep_stress_data: data from the sleep
        :return: predict if the sleep is stressed or not
        """
        return self.classifier.predict(sleep_stress_data)

    def decide(self, sleep_stress_data: pd.DataFrame):
        prediction = self.__predict(sleep_stress_data)

        return prediction

    def get_accuracy_metrics(self):
        pass

    def get_sleep_data(self, limit: int = 10, offset: int = 0):
        return self.dataset.iloc[::-1].iloc[offset:limit]
