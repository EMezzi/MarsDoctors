import pandas as pd


class HeartDisease:

    def __init__(self, version: str = "latest"):
        self.version = version

    def heuristic(self, heart_data: pd.DataFrame):
        if heart_data['pain']:
            return True
