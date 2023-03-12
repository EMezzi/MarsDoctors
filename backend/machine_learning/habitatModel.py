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
                self.dataset = pd.read_csv("../../datasets/habitat/Habitat_Stress.csv")
            except Exception as e:
                print("Error when loading data and model: ", e)
        else:
            raise Exception("No other models saved for this task!")

    def heuristic(self, habitat_data: pd.DataFrame):
        if habitat_data['PM2.5'] > 0.25 and habitat_data['Rh'] > 0.45:
            return True
        else:
            return False

    def predict(self, habitat_data: pd.DataFrame):
        return self.classifier.predict(habitat_data)

    def get_accuracy_metrics(self):
        pass

    def get_water_data(self, limit: int = 10, offset: int = 0):
        return self.dataset.iloc[::-1].iloc[offset:limit]
