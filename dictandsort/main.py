import csv
import sorter.py

def read_clothing_data(filename):
    clothing_data = {}
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            clothing_data[int(row['id'])] = (row['clothing_type'], row['colour'], row['size'])
    return clothing_data


def main():
    filename = "clothing.csv"
    clothing_data = read_clothing_data(filename)

    sort_choice = int(input("What would you like to sort on?\ntype - 1, colour - 2, size - 3: "))
    print(f"You are sorting on the {['type', 'colour', 'size'][sort_choice - 1]} of clothing.")

    sorted_data = sorter.sort_clothing(clothing_data, sort_choice)
    for item in sorted_data:
        print(item)

if __name__ == "__main__":
    main()

