import joblib
import json
import numpy as np
from sklearn import metrics
import pandas as pd


class WaterPotabilityModel:
    version = None
    classifier = None
    dataset: pd.DataFrame = None

    def __init__(self, version: str = "latest"):
        self.version = version
        if version == "latest":
            try:
                # Load latest model and data
                self.classifier = joblib.load('machine_learning/model_data/water_potability_model.pkl')
                self.dataset = pd.read_csv("../datasets/habitat/water_potability.csv")
            except Exception as e:
                print("Error when loading data and model: ", e)
        else:
            raise Exception("No other models saved for this task!")

    def predict(self, water_data: pd.DataFrame):
        return self.classifier.predict(water_data)

    def get_accuracy_metrics(self):
        pass

    def get_water_data(self, limit: int = 10, offset: int = 0):
        return self.dataset.iloc[::-1].iloc[offset:limit]
