import csv
import json


csv_file = "Country_Data.csv"
json_file = "Country_Data.json"

# Define the data table
headers = ["Country", "Capital", "Continent", "Language"]
data = [
    ["Australia", "Canberra", "Australia", "English"],
    ["China", "Beijing", "Asia", "Mandarin"],
    ["Germany", "Berlin", "Europe", "German"],
    ["France", "Paris", "Europe", "French"],
    ["Brazil", "Brazilia", "South America", "Portugese"],
]

# Create and Write into a CSV
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(headers)
    csv_writer.writerows(data)

print("CSV File Created")

# Open the CSV
with open(csv_file, "r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
