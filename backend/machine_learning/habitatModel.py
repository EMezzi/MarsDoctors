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
        if habitat_data['PM2_5'].loc[0] > 0.25 and habitat_data['Rh'].loc[0] > 0.45:
            return 1
        else:
            return 0

    def __predict(self, habitat_data: pd.DataFrame):
        """
        :param habitat_data: data from the habitat
        :return: prediction, stressed or not
        """

        habitat_data = habitat_data.drop(columns=["Setting", "Post", "STAI"])
        habitat_data["Stresslevel"] -= 1
        habitat_data["Sex"] = habitat_data["Sex"].map({'Male': 1, 'Female': 0})
        habitat_data["Healthcondition"] = habitat_data["Healthcondition"].map(
            {'Excellent': 3, 'Very good': 2, 'Good': 1, 'Fair': 0})
        habitat_data["Medicine"] = habitat_data["Medicine"].map({'Yes': 1, 'No': 0})
        habitat_data["Sleep"] = habitat_data["Sleep"].map({'Yes': 1, 'No': 0})
        habitat_data["Caffinebeverage"] = habitat_data["Caffinebeverage"].map({'Yes': 1, 'No': 0})
        habitat_data = habitat_data.drop(columns=["Stresslevel"])
        habitat_data = habitat_data.drop(columns=habitat_data.columns[19:].values)

        print(habitat_data.columns)

        return self.classifier.predict(habitat_data)

    def decide(self, habitat_data: pd.DataFrame):
        """
        The method calls both the heuristic and the prediction method. It returns a hard warning if both are True
        otherwise it returns a soft warning, otherwise it returns something nice
        :param habitat_data:
        :return:
        """

        print("Risultato di questo: ", self.__predict(habitat_data)[0])
        if (self.__predict(habitat_data)[0] == 1 or self.__predict(habitat_data)[0] == 2 or
            self.__predict(habitat_data)[0] == 3) and self.__heuristic(habitat_data) == 1:
            return [2, "Hard stress provoked by the habitat"]
        elif (self.__predict(habitat_data)[0] == 1 or self.__predict(habitat_data)[0] == 2 or
              self.__predict(habitat_data)[0] == 3) or self.__heuristic(habitat_data) == 1:
            return [1, "Mild stress, pay attention"]
        else:
            return [0, "You are not stressed"]

    def get_accuracy_metrics(self):
        pass

    def get_habitat_data(self, limit: int = 10, offset: int = 0):
        return self.dataset.iloc[::-1].iloc[offset:limit]
