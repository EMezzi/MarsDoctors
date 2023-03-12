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
                self.dataset = pd.read_csv("../../datasets/habitat/Sleep_Stress.csv")
            except Exception as e:
                print("Error when loading data and model: ", e)
        else:
            raise Exception("No other models saved for this task!")

    def heuristic(self, sleep_stress_data: pd.DataFrame):
        if sleep_stress_data['blood_oxygen'] < 88 and sleep_stress_data['heart_rate'] > 75 and \
                sleep_stress_data['limb movement'] > 17 and sleep_stress_data['rapid eye movement'] > 100 and \
                (sleep_stress_data['respiration rate'] > 96 and sleep_stress_data['snoring rate'] > 96) and \
                sleep_stress_data['temperature'] < 90:
            return True
        else:
            return False

    def predict(self, sleep_stress_data: pd.DataFrame):
        return self.classifier.predict(sleep_stress_data)

    def get_accuracy_metrics(self):
        pass

    def get_water_data(self, limit: int = 10, offset: int = 0):
        return self.dataset.iloc[::-1].iloc[offset:limit]
