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
                self.dataset = pd.read_csv("../datasets/habitat/Habitat_Stress.csv")
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
            return 1
        else:
            return 0

    def __predict(self, habitat_data: pd.DataFrame):
        """
        :param habitat_data: data from the habitat
        :return: prediction, stressed or not
        """
        print(habitat_data)
        print(self.classifier.predict(habitat_data))
        return self.classifier.predict(habitat_data)

    def decide(self, habitat_data: pd.DataFrame):
        """
        The method calls both the heuristic and the prediction method. It returns a hard warning if both are True
        otherwise it returns a soft warning, otherwise it returns something nice
        :param habitat_data:
        :return:
        """
        if self.__predict(habitat_data)[0] == 1 and self.__heuristic(habitat_data) == 1:
            return 2
        elif self.__predict(habitat_data)[0] == 1 or self.__heuristic(habitat_data) == 1:
            return 1
        else:
            return 0

    def get_accuracy_metrics(self):
        pass

    def get_habitat_data(self, limit: int = 10, offset: int = 0):
        return self.dataset.iloc[::-1].iloc[offset:limit]
