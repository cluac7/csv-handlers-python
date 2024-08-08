import csv

def read_numbers_from_csv(filename):
    numbers = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                for item in row:
                        numbers.append(int(item.strip()))
    return numbers

def calculate_average(numbers):
        average = sum(numbers) / len(numbers)
        return average

def main():
    filename = input("Enter the filename: ")
    numbers = read_numbers_from_csv(filename)
    average = calculate_average(numbers)
    if average is not None:
        print(f"The average of the numbers is: {average}")

if __name__ == "__main__":
    main()
