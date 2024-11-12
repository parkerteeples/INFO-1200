import csv

FILE_NAME = 'file.csv'

names_list = []

with open(FILE_NAME,'r', newline='') as input_file:
    reader = csv.reader(input_file)

    for row in reader:
        names_list.append(row)
        
for row in names_list:
    for sub_row in row:
        print(sub_row, end='\t')
    print()