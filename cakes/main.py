import csv

def read_cake_data(filename):
    cake_data = {}
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cake_choice = row['choice']
            friend = row['friend']
    return cake_data

