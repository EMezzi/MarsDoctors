import pickle as pk
import pandas as pd
import csv

# loading the data about astronauts gene expression
gene_expression = pd.read_pickle('../files/binary_files/gene_expression.pk')

# data about all the props
input_file = '../files/text_files/GPL15207-17536.txt'

print(gene_expression)

with open(input_file, 'r') as text_file:
    # Open the output CSV file for writing
    with open('../files/csv_files/genes_names.csv', 'w', newline='') as csv_file:
        # Create a CSV writer object with a space delimiter
        csv_writer = csv.writer(csv_file, delimiter=' ')
        # Read each line from the text file
        for line in text_file:
            # Split the line into fields using a space delimiter
            fields = line.strip().split(' ')
            # Write the fields as a row in the CSV file
            csv_writer.writerow(fields)

genes_names = pd.read_csv('../files/csv_files/genes_names.csv', delimiter='\t', dtype={"SPOT_ID": str}).\
    set_index('ID')

print(genes_names.columns)

to_consider = list(gene_expression.columns)
to_consider.append('Gene Title')

print(to_consider)

total = gene_expression.join(genes_names, on='ID_REF', how='inner')
total = total[to_consider]

print(len(genes_names['Gene Title']))