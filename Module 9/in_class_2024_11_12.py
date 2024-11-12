import csv

FILE_NAME = "test.csv"

master_list = []
master_list.append(['Name','Age']) # Appending a Header Row

more = 'y'
while more == 'y':
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    master_list.append([name,age])
    more = input('Continue? (y/n):')

with open(FILE_NAME, 'w', newline ='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(master_list)