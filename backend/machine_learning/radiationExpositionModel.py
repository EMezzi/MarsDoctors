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

        s_at_11757650 = 5.376935
        s_at_11746506 = 7.215063
        a_at_11727942 = 6.360752
        a_at_11739534 = 5.635366
        x_at_11749460 = 5.273240
        x_at_11754604 = 7.672275
        x_at_11745837 = 5.308073
        x_at_11739536 = 5.810706
        x_at_11737944 = 7.846322
        x_at_11755730 = 7.782462
        a_at_11724463 = 4.551536
        a_at_11756809 = 6.141027
        a_at_11730501 = 6.357842

        if ((genes_data["s_at_11757650"].iloc[0] - s_at_11757650) > (s_at_11757650 / 100)) or \
                (genes_data["s_at_11746506"].iloc[0] - s_at_11746506) > (s_at_11746506 / 100) or \
                (genes_data["a_at_11727942"].iloc[0] - a_at_11727942) > (a_at_11727942 / 100) or \
                (genes_data["a_at_11739534"].iloc[0] - a_at_11739534) > (a_at_11739534 / 100) or \
                (genes_data["x_at_11749460"].iloc[0] - x_at_11749460) > (x_at_11749460 / 100) or \
                (genes_data["x_at_11754604"].iloc[0] - x_at_11754604) > (x_at_11754604 / 100) or \
                (genes_data["x_at_11745837"].iloc[0] - x_at_11745837) > (x_at_11745837 / 100) or \
                (genes_data["x_at_11739536"].iloc[0] - x_at_11739536) > (x_at_11739536 / 100) or \
                (genes_data["x_at_11737944"].iloc[0] - x_at_11737944) > (x_at_11737944 / 100) or \
                (genes_data["x_at_11755730"].iloc[0] - x_at_11755730) > (x_at_11755730 / 100) or \
                (genes_data["a_at_11724463"].iloc[0] - a_at_11724463) > (a_at_11724463 / 100) or \
                (genes_data["a_at_11756809"].iloc[0] - a_at_11756809) < 0 and \
                abs(genes_data["a_at_11756809"].iloc[0] - a_at_11756809) > (a_at_11756809 / 100) or \
                genes_data["a_at_11730501"].iloc[0] - a_at_11730501 < 0 and \
                abs(genes_data["a_at_11730501"].iloc[0] - a_at_11730501) > (a_at_11730501 / 100):
            return [1, "You have been exposed to ionizing radiation"]
        else:
            return [0, "You have not been exposed to ionizing radiation"]

    def decide(self, genes_data: pd.DataFrame):
        return self.__heuristic(genes_data)

    def get_accuracy_metrics(self):
        pass

    def get_genes_data(self):
        pass
