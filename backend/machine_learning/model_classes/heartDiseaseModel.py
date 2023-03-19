"""
Class which manages predictions related to the heart.
"""

import joblib
import pandas as pd

variable = joblib.load('../model_data/heart_disease.joblib')


class HeartDisease:

    def __init__(self, version: str = "latest"):
        self.version = version
        if version == "latest":
            try:
                # Load latest model and data
                self.classifier = joblib.load('../model_data/heart_disease.joblib')
                self.dataset = pd.read_csv("../../../datasets/health/heart.csv")
            except Exception as e:
                print("Error when loading data and model: ", e)
        else:
            raise Exception("No other models saved for this task!")

    @staticmethod
    def __heuristic(heart_data: pd.DataFrame):
        """
        This method returns the results from the heuristics
        :param heart_data:
        :return:
        """
        if heart_data['pain'] > 0:
            return True
        else:
            return False

    def __predict(self, heart_data: pd.DataFrame):
        """
        This method returns the result from the prediction of the model
        :param heart_data:
        :return:
        """
        return self.classifier.predict(heart_data)

    def decide(self, heart_data: pd.DataFrame):
        if self.__heuristic(heart_data):
            "CHECK ! CHECK !"
        else:
            "Usain Bolt Heart"
