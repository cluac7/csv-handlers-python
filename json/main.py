import csv
import json

def combine_and_calculate(movies_csv, reviews_json):
  movie_data = {}
  with open(movies_csv, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      movie_data[row['id']] = row['title']


def print_results(combined_data):

if __name__ == "__main__":
  movies_csv = "movies.csv"
  reviews_json = "reviews.json"
  combined_data = combine_and_calculate(movies_csv, reviews_json)
  print_results(combined_data)

