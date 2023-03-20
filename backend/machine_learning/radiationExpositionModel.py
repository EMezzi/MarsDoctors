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

        s_at_11757650 = 5.376935,
        s_at_11746506 = 7.215063,
        a_at_11727942 = 6.360752,
        a_at_11739534 = 5.635366,
        x_at_11749460 = 5.273240,
        x_at_11754604 = 7.672275,
        x_at_11745837 = 5.308073,
        x_at_11739536 = 5.810706,
        x_at_11737944 = 7.846322,
        x_at_11755730 = 7.782462,
        a_at_11724463 = 4.551536,

        a_at_11756809 = 6.141027,
        a_at_11730501 = 6.357842

        if (genes_data["11757650_s_at"] - s_at_11757650 > (s_at_11757650 * 1 / 100)) or \
                genes_data["11746506_a_at"] - s_at_11746506 > s_at_11746506 * 1 / 100 or \
                genes_data["11727942_a_at"] - a_at_11727942 > a_at_11727942 * 1 / 100 or \
                genes_data["11739534_a_at"] - a_at_11739534 > a_at_11739534 * 1 / 100 or \
                genes_data["11749460_x_at"] - x_at_11749460 > x_at_11749460 * 1 / 100 or \
                genes_data["11754604_x_at"] - x_at_11754604 > x_at_11754604 * 1 / 100 or \
                genes_data["11745837_x_at"] - x_at_11745837 > x_at_11745837 * 1 / 100 or \
                genes_data["11739536_x_at"] - x_at_11739536 > x_at_11739536 * 1 / 100 or \
                genes_data["11737944_x_at"] - x_at_11737944 > x_at_11737944 * 1 / 100 or \
                genes_data["11755730_x_at"] - x_at_11755730 > x_at_11755730 * 1 / 100 or \
                genes_data["11724463_a_at"] - a_at_11724463 > a_at_11724463 * 1 / 100 or \
                genes_data["11756809_a_at"] - a_at_11756809 < 0 and abs(
            genes_data["11756809_a_at"] - a_at_11756809) > a_at_11756809 * 1 / 100 or \
                genes_data["11730501_a_at"] - a_at_11730501 < 0 and abs(
            genes_data["11730501_a_at"] - a_at_11730501) < a_at_11730501 * 1 / 100:
            return 1
        else:
            return 0

    def decide(self, genes_data: pd.DataFrame):
        if self.__heuristic(genes_data):
            return "Immediate check"
        else:
            return "No radiations in your body"

    def get_accuracy_metrics(self):
        pass

    def get_genes_data(self):
        pass
