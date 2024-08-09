import csv

def read_cake_data(filename):
    cake_data = {}
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cake_choice = row['choice']
            friend = row['friend']
            if cake_choice not in cake_data:
                cake_data[cake_choice] = set()
            cake_data[cake_choice].add(friend)
    return cake_data

def find_cake_sharers(cake_data, cake_of_the_day):
    if cake_of_the_day in cake_data:
        return cake_data[cake_of_the_day]
    else:
        return set()

