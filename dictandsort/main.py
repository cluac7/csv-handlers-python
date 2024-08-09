import csv

def read_clothing_data(filename):
    clothing_data = {}
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            clothing_data[int(row['id'])] = (row['clothing_type'], row['colour'], row['size'])
    return clothing_data

def sort_clothing(clothing_data, sort_choice):


def main():
    filename = "clothing.csv"
    clothing_data = read_clothing_data(filename)


    sorted_data = sort_clothing(clothing_data, sort_choice)
    for item in sorted_data:
        print(item)

if __name__ == "__main__":
    main()

