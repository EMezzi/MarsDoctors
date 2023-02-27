import csv
import pandas as pd
import pickle as pk

input_file = '../files/text_files/GSE63952_normalized_data_with_controls.txt'

with open(input_file, 'r') as text_file:
    # Open the output CSV file for writing
    with open('../files/csv_files/gene_expression.csv', 'w', newline='') as csv_file:
        # Create a CSV writer object with a space delimiter
        csv_writer = csv.writer(csv_file, delimiter=' ')
        # Read each line from the text file
        for line in text_file:
            # Split the line into fields using a space delimiter
            fields = line.strip().split(' ')
            # Write the fields as a row in the CSV file
            csv_writer.writerow(fields)

gene_expression = pd.read_csv('../files/csv_files/gene_expression.csv', delimiter='\t').set_index('ID_REF')

"""
Check if the transformation to csv was correct. 
"""
columns = list(gene_expression.columns)
indexes = list(gene_expression.index)

print(columns[5], indexes[10])
print(columns[98], indexes[11])

print(gene_expression.loc[indexes[10], columns[5]])
print(gene_expression.loc[indexes[11], columns[98]])

"""
Saving the pandas dataframe to pickle
"""
with open('../files/binary_files/gene_expression.pk', 'wb') as file:
    pk.dump(gene_expression, file)
