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
coolest station(s). The results are saved to the following files inside the results folder:
- average_temp.txt: Contains the average temperature for each month across all years.
- largest_temp_range_station.txt: Contains the station(s) with the largest temperature range.
- warmest_and_coolest_station.txt: Contains the warmest and coolest station(s).
"""
import os
import pandas as pd


def main():
    # Files paths are relative to the location of this python script file.
    # List of temperature data files
    DATA_DIR = "temperature_data"  # Directory containing the data files
    OUTPUT_DIR = "results"  # Directory to save the analysis files

    # Setup the data files for input and output
    # Exit program if there are problems with data files
    data_files_ok = setup_data_files(DATA_DIR, OUTPUT_DIR)
    if not data_files_ok:
        exit()

    file_paths = get_files(DATA_DIR)

    # Initialize a list to store data from all files
    all_data = get_data(DATA_DIR, file_paths)

    # Combine all data into a single DataFrame
    combined_data = pd.concat(all_data, ignore_index=True)

    # Calculate the average temperature for each month
    monthly_avg_temps = combined_data.iloc[:, 4:].mean()

    # Save the average temperature for each month to a file
    save_avg_temp(OUTPUT_DIR, monthly_avg_temps)

    # Calculate the temperature range for each station
    combined_data["Temperature Range"] = combined_data.iloc[:, 4:].max(
        axis=1) - combined_data.iloc[:, 4:].min(axis=1)

    # Find the station(s) with the largest temperature range
    max_temp_range = combined_data["Temperature Range"].max()
    largest_temp_range_stations = combined_data[combined_data["Temperature Range"]
                                                == max_temp_range]["STATION_NAME"]

    # Save the stations with the largest temperature range to a file
    save_large_temp_range(OUTPUT_DIR, largest_temp_range_stations)

    # Calculate the average temperature for each station across all months
    combined_data["Average Temperature"] = combined_data.iloc[:, 4:].mean(
        axis=1)

    # Find the warmest and coolest stations
    max_avg_temp = combined_data["Average Temperature"].max()
    min_avg_temp = combined_data["Average Temperature"].min()

    warmest_stations = combined_data[combined_data["Average Temperature"]
                                     == max_avg_temp]["STATION_NAME"]
    coolest_stations = combined_data[combined_data["Average Temperature"]
                                     == min_avg_temp]["STATION_NAME"]

    # Save the warmest and coolest stations to a file
    save_warm_cool_stations(OUTPUT_DIR, warmest_stations, coolest_stations)

# end main() function


def get_files(path="") -> list[str]:
    """
    Returns the names of all the files in the given path
    """
    files = []
    if os.path.isdir(path):
        files = os.listdir(path)
    return files


def setup_data_files(data_dir, output_dir) -> bool:
    """
    Checks that the data directory and output directories exist
    Creates an output directory if it does not exist
    Returns False if the data directory does not exist or if the 
    output directory could not be created
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as error:
        print("Error: Could not create output directory")
        return False

    if not os.path.exists(data_dir):
        print("Error: Data directory not found")
        return False

    return True  # Data files are ok

def get_data(DATA_DIR, file_paths) -> list:
    """
    Uses pandas to read the data from each file in the file_paths list
    and appends the data to the all_data list
    """
    # Read and combine data from all files
    data_list = []
    for file_path in file_paths:
        data_file = os.path.join(DATA_DIR, file_path)
        data = pd.read_csv(data_file)
        data_list.append(data)
    return data_list


def save_avg_temp(output_dir, monthly_avg):
    """
    Saves the average temperature for each month to a file
    """
    avg_temp_file = os.path.join(output_dir, "average_temp.txt")
    monthly_avg.to_csv(
        avg_temp_file,
        header=["Average Temperature"],
        index_label="Month"
    )

def save_large_temp_range(output_dir, largest_temp_range_stations):
    """
    Saves the stations with the largest temperature range to a file
    """
    max_temp_file = os.path.join(output_dir, "largest_temp_range_station.txt")
    largest_temp_range_stations.to_csv(
        max_temp_file,
        header=["Station Name"],
        index=False
    )

def save_warm_cool_stations(output_dir, warmest_stations, coolest_stations):
    """
    Saves the warmest and coolest stations to a file
    """
    warm_cool_file = os.path.join(
        output_dir, "warmest_and_coolest_station.txt")
    with open(
        warm_cool_file,
        "w"
    ) as file:
        file.write("Warmest Stations:\n")
        file.write("\n".join(warmest_stations))
        file.write("\n\nCoolest Stations:\n")
        file.write("\n".join(coolest_stations))


# Check that the program is being run directly and not imported as a module.
# See https://docs.python.org/3/library/__main__.html for more information.
if __name__ == "__main__":
    main()
