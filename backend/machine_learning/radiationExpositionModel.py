"""
This class manages the predictions about the radiation exposition. This class has no models
only heuristics.
"""

import pandas as pd


class RadiationExpositionModel:
    def __init__(self, version: str = 'latest'):
        self.version = version

    @staticmethod
    def __heuristic(genes_data: pd.DataFrame):
        """
        This method returns the result from the heuristic
        :param genes_data: data about genes' expression
        :return: returns True if there is something wrong
        """
        pass

    def decide(self, genes_data: pd.DataFrame):
        if self.__heuristic(genes_data):
            return "Immediate check"
        else:
            return "No radiations in your body"

    def get_accuracy_metrics(self):
        pass

    def get_genes_data(self):
        pass
