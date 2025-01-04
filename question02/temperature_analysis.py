"""
Group Name: CAS/DAN 07
Group Members:
Jason Angus - S365855
Marco Giacomelli - S383510
Yoana Vasileva - S263707

HIT137 Assignment 2 Question 2
File: temperature_analysis.py

This program analyses temperature data collected from multiple weather stations 
in Australia. It calculates the average temperature for each month, finds the 
station(s) with the largest temperature range, and identifies the warmest and 
coolest station(s). The results are saved to the following files:
- average_temp.txt: Contains the average temperature for each month across all years.
- largest_temp_range_station.txt: Contains the station(s) with the largest temperature range.
- warmest_and_coolest_station.txt: Contains the warmest and coolest station(s).
"""
import os
import pandas as pd

def get_files(path="") -> list[str]:
  """
  Returns the names of all the files in the given path
  """
  files = []
  if os.path.isdir(path):
    files = os.listdir(path)
  return files

# List of temperature data files
DATA_DIR = "temperature_data" # Directory containing the data files
OUTPUT_DIR = "results" # Directory to save the analysys files
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
    
# Get data file names
file_paths = get_files(DATA_DIR)
if file_paths.__len__() == 0:
    print("No data files found")

# file_paths = [
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1986.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1987.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1988.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1989.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1990.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1991.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1992.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1993.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1994.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1995.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1996.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1997.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1998.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_1999.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_2000.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_2001.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_2002.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_2003.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_2004.csv",
#     r"C:\Users\yoana\Downloads\CDU\Software Now\Assignment 2\HIT137 Assignment 2 SS 2024\temperature_data\stations_group_2005.csv"
# ]

# Initialize a list to store data from all files
all_data = []

# Read and combine data from all files
for file_path in file_paths:
    data = pd.read_csv(DATA_DIR + "/" + file_path)
    all_data.append(data)

# Combine all data into a single DataFrame
combined_data = pd.concat(all_data, ignore_index=True)

# Calculate the average temperature for each month
monthly_avg_temps = combined_data.iloc[:, 4:].mean()

# Save the average temperature for each month to a file
OUTPUT_AVG_TEMP_FILE = OUTPUT_DIR + "/" + "average_temp.txt"
monthly_avg_temps.to_csv(
    OUTPUT_AVG_TEMP_FILE,
    header=["Average Temperature"],
    index_label="Month"
)

# Calculate the temperature range for each station
combined_data["Temperature Range"] = combined_data.iloc[:, 4:].max(axis=1) - combined_data.iloc[:, 4:].min(axis=1)

# Find the station(s) with the largest temperature range
max_temp_range = combined_data["Temperature Range"].max()
largest_temp_range_stations = combined_data[combined_data["Temperature Range"] == max_temp_range]["STATION_NAME"]

# Save the stations with the largest temperature range to a file
OUTPUT_MAX_TEMP_FILE = OUTPUT_DIR + "/" + "largest_temp_range_station.txt"
largest_temp_range_stations.to_csv(
    OUTPUT_MAX_TEMP_FILE,
    header=["Station Name"],
    index=False
)

# Calculate the average temperature for each station across all months
combined_data["Average Temperature"] = combined_data.iloc[:, 4:].mean(axis=1)

# Find the warmest and coolest stations
max_avg_temp = combined_data["Average Temperature"].max()
min_avg_temp = combined_data["Average Temperature"].min()

warmest_stations = combined_data[combined_data["Average Temperature"] == max_avg_temp]["STATION_NAME"]
coolest_stations = combined_data[combined_data["Average Temperature"] == min_avg_temp]["STATION_NAME"]

# Save the warmest and coolest stations to a file
OUTPUT_WARMEST_COOLEST_FILE = OUTPUT_DIR + "/" + "warmest_and_coolest_station.txt"
with open(
    OUTPUT_WARMEST_COOLEST_FILE, 
    "w"
) as file:
    file.write("Warmest Stations:\n")
    file.write("\n".join(warmest_stations))
    file.write("\n\nCoolest Stations:\n")
    file.write("\n".join(coolest_stations))