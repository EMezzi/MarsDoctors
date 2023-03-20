"""
In this script we consider the gene expression for the samples:
    1) We first calculate the average gene expression for hour and radiation level.
    2) We calculate the rate of growth from the 1st to the 6th hour for each radiation level.
    3) We consider, for each radiation level, the first 50 biggest growth rate and the smallest 50 growth rates.
"""

import re
import pandas as pd
import pickle as pk

gene_expression = pd.read_pickle('../files/binary_files/gene_expression.pk')

samples = gene_expression.columns.tolist()

# Dataframe which will contain the averages for specific radiations and hours
aggregation_data_frame = pd.DataFrame({'ID_REF': gene_expression.index}).set_index('ID_REF')

radiation_codes = ['0.00', '0.15', '0.30', '1.50']
hour_codes = ['1h', '2h', '6h']

"""
Here we average the values for the samples of a specific hour and radiation. 
"""
for rad in radiation_codes:
    for hour in hour_codes:
        path = rad + 'Gy_' + hour
        aggregation_data_frame['SAMPLES_' + rad + 'Gy_' + hour] = \
            gene_expression.loc[:, [sample for sample in samples if re.search(path, sample)]].mean(axis=1)

print(aggregation_data_frame.columns)
print(aggregation_data_frame)

idx = pd.IndexSlice
print("Base levels")

aggregation_data_frame["average_0"] = aggregation_data_frame.loc[
    idx["11757650_s_at", "11746506_a_at", "11727942_a_at", "11739534_a_at",
        "11749460_x_at", "11754604_x_at", "11745837_x_at", "11739536_x_at",
        "11737944_x_at", "11755730_x_at", "11724463_a_at", "11756809_a_at",
        "11730501_a_at"],
    ["SAMPLES_0.00Gy_1h", "SAMPLES_0.00Gy_2h", "SAMPLES_0.00Gy_6h"]].mean(axis=1)

print(aggregation_data_frame.loc[idx["11757650_s_at", "11746506_a_at", "11727942_a_at", "11739534_a_at",
                                     "11749460_x_at", "11754604_x_at", "11745837_x_at", "11739536_x_at",
                                     "11737944_x_at", "11755730_x_at", "11724463_a_at", "11756809_a_at",
                                     "11730501_a_at"],
                                 ["average_0"]])

# Dataframe which will contain the rates of change of the genes expressions
rate_data_frame = pd.DataFrame({'ID_REF': aggregation_data_frame.index}).set_index('ID_REF')

"""
Here we calculate the difference between the 1 hour radiation and the 6 hours for the same level of radiation. 
"""
for rad in radiation_codes:
    rate_data_frame['SAMPLE_Rate_' + rad + 'Gy'] = \
        aggregation_data_frame['SAMPLES_' + rad + 'Gy_6h'] / aggregation_data_frame['SAMPLES_' + rad + 'Gy_1h']

"""
Here we create a dataframe that for each level of radiation, will take the first 50 rates of growth and the first 50 
decrease. Everything will be store in a dictionary of dictionaries, where the main keys will be the Radiation level,
and then for each radiation level there will be a dictionary with two keys, the first keys for the first 50, and the
last key for the last 50 gene expressions. 
"""

"""
first_and_last = {}

for i, column in enumerate(rate_data_frame.columns):
    col = rate_data_frame.sort_values(by=[column], ascending=False)[column]
    grow = col.iloc[:50]
    decrease = col.iloc[-50:]
    first_and_last[column] = {"first": grow, "last": decrease}

with open('../files/binary_files/first_and_last.pk', 'wb') as f:
    pk.dump(first_and_last, f)
"""
