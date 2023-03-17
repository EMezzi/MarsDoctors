"""
This class manages the predictions for the stress coming from the habitat.
"""

import joblib
import pandas as pd


class HabitatModel:
    version = None
    classifier = None
    dataset: pd.DataFrame = None

    def __init__(self, version: str = "latest"):
        self.version = version
        if version == "latest":
            try:
                # Load latest model and data
                self.classifier = joblib.load('machine_learning/model_data/habitat_random_forest_model.joblib')
                self.dataset = pd.read_csv("../../../datasets/habitat/Habitat_Stress.csv")
            except Exception as e:
                print("Error when loading data and model: ", e)
        else:
            raise Exception("No other models saved for this task!")

    @staticmethod
    def __heuristic(habitat_data: pd.DataFrame):
        """
        This method returns the result from the heuristic
        :param habitat_data: data from the habitat
        :return: True or False
        """
        if habitat_data['PM2.5'] > 0.25 and habitat_data['Rh'] > 0.45:
            return True
        else:
            return False

    def __predict(self, habitat_data: pd.DataFrame):
        """
        :param habitat_data: data from the habitat
        :return: prediction, stressed or not
        """
        return self.classifier.predict(habitat_data)

    def decide(self, habitat_data: pd.DataFrame):
        """
        The method calls both the heuristic and the prediction method. It returns a hard warning if both are True
        otherwise it returns a soft warning, otherwise it returns something nice
        :param habitat_data:
        :return:
        """
        if self.__heuristic(habitat_data) and self.__predict(habitat_data):
            return "You are about to die"

        elif self.__heuristic(habitat_data) or self.__predict(habitat_data):
            return "This habitat is stressing you. Normal, it's not earth"

        else:
            return "You are not stressed"

    def get_accuracy_metrics(self):
        pass

    def get_water_data(self, limit: int = 10, offset: int = 0):
        return self.dataset.iloc[::-1].iloc[offset:limit]
