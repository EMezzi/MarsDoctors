import joblib
import json
import numpy as np
from sklearn import metrics
import pandas as pd


class RadiationExpositionModel:
    def __init__(self, version: str = 'latest'):
        self.version = version

        if version == 'latest':
            try:
                self.classifier = joblib.load('machine_learning/model_data/radiation_exposition_model.pkl')
            except Exception as e:
                print("Error when loading data and model: ", e)
        else:
            raise Exception("No other models saved for this task!")

    def heuristic(self, genes_data: pd.DataFrame):
        pass

    def predict(self, genes_data: pd.DataFrame):
        return self.classifier.predict(genes_data)

    def get_accuracy_metrics(self):
        pass

    def get_genes_data(self):
        pass
