import csv
import json

def combine_and_calculate(movies_csv, reviews_json):
  movie_data = {}
  """ Inputs the csv file and reads through each line as a row in 
  a dictionary using DictReader
  """
  with open(movies_csv, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      movie_data[row['id']] = row['title']

  # Loads the json file
  with open(reviews_json, 'r') as jsonfile:
    reviews = json.load(jsonfile)

  combined_data = []
  """ Iterates through each movie in the csv and looks for ratings in the 
  reviews in the json file. 
  collates and appends the data
  """
  for movie_id, title in movie_data.items():
    if movie_id in reviews:
      average_rating = sum(reviews[movie_id]) / len(reviews[movie_id])
      combined_data.append((movie_id, title, round(average_rating, 2)))

  return combined_data

def print_results(combined_data):
  """ Prints out ratings based on the data found in the array returned by 
  combined_data by iterating through each piece of info and printing
  the data about it to 2 decimal places
  """
  print("Movie ratings:")
  for i, (movie_id, title, average_rating) in enumerate(combined_data, start=1):
    print(f"{movie_id}. {title}: {average_rating:.2f}")

if __name__ == "__main__":
  movies_csv = "movies.csv"
  reviews_json = "reviews.json"
  combined_data = combine_and_calculate(movies_csv, reviews_json)
  print_results(combined_data)

