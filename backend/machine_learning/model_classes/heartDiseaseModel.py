"""
Class which manages predictions related to the heart.
"""

import pandas as pd


class HeartDisease:

    def __init__(self, version: str = "latest"):
        self.version = version

    @staticmethod
    def __heuristic(heart_data: pd.DataFrame):
        if heart_data['pain']:
            return True

    def decide(self, heart_data: pd.DataFrame):
        if self.__heuristic(heart_data):
            "CHECK ! CHECK !"
        else:
            "Usain Bolt Heart"
