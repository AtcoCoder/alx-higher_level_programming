import csv

with open('sample.csv', 'a', newline='') as csvfile:
    datawriter = csv.writer(csvfile)
    datawriter.writerow([{'name': 'Binta', 'surname': 'Jammeh'}])
