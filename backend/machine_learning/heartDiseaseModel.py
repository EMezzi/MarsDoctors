"""
Class which manages predictions related to the heart.
"""

import joblib
import pandas as pd


class HeartDisease:

    def __init__(self, version: str = "latest"):
        self.version = version
        if version == "latest":
            try:
                # Load latest model and data
                self.classifier = joblib.load('machine_learning/model_data/heartdisup.joblib')
                self.dataset = pd.read_csv("../datasets/health/heart.csv")
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
        if heart_data["chest_pain_type"].loc[0] > 0:
            return 1
        else:
            return 0

    def __predict(self, heart_data: pd.DataFrame):
        """
        This method returns the result from the prediction of the model
        :param heart_data:
        :return:
        """
        return self.classifier.predict(heart_data)

    def decide(self, heart_data: pd.DataFrame):
        """
        The method calls both the heuristic and the prediction method.
        :param heart_data:
        :return:
        """

        prediction = self.__predict(heart_data)[0]
        heuristic = self.__heuristic(heart_data)

        if prediction == 1 and heuristic == 1:
            return [2, "You are about to have an heart attack"]
        elif prediction == 1 or heuristic == 1:
            return [1, "You might be at risk of having an heart attack"]
        else:
            return [0, "Your heart is in good shape"]
