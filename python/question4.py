# Question 4 -
# Write a program to download the data from the link given below and then read the data and convert the into
# the proper structure and return it as a CSV file.
# Link - https://data.nasa.gov/resource/y77d-th95.json
# Note - Write code comments wherever needed for code understanding.

# Excepted Output Data Attributes
# ● Name of Earth Meteorite - string 
# ● id - ID of Earth Meteorite - int 
# ● nametype - string 
# ● recclass - string
# ● mass - Mass of Earth Meteorite - float 
# ● year - Year at which Earth Meteorite was hit - datetime format
# ● reclat - float 
# ● recclong - float
# ● point coordinates - list of int



import pandas as pd
import requests

# Function to download data from the provided link
def download_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# Function to process the data and convert it into a properly structured dataframe
def process_data(data):
    # Create empty lists to store the extracted attributes
    names = []
    ids = []
    nametypes = []
    recclasses = []
    masses = []
    years = []
    reclats = []
    reclongs = []
    coordinates = []

    # Iterate over each meteorite in the data and extract the attributes
    for meteorite in data:
        names.append(meteorite.get('name', None))
        ids.append(meteorite.get('id', None))
        nametypes.append(meteorite.get('nametype', None))
        recclasses.append(meteorite.get('recclass', None))
        masses.append(meteorite.get('mass', None))
        years.append(meteorite.get('year', None))
        reclats.append(meteorite.get('reclat', None))
        reclongs.append(meteorite.get('reclong', None))
        if meteorite.get('geolocation', None) is not None:    
            coordinates.append(meteorite['geolocation'].get('coordinates', None))
        else:
            coordinates.append(None)

    # Create a dictionary of the extracted attributes
    data_dict = {
        'Name of Earth Meteorite': names,
        'id': ids,
        'nametype': nametypes,
        'recclass': recclasses,
        'mass': masses,
        'year': years,
        'reclat': reclats,
        'reclong': reclongs,
        'coordinates': coordinates,
    }

    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data_dict)
    return df

# Function to export the dataframe to a CSV file
def export_to_csv(df, filename):
    df.to_csv(filename, index=False)

# Main function
def main():
    # Download the data from the provided link
    url = "https://data.nasa.gov/resource/y77d-th95.json"
    data = download_data(url)

    # Process the data and convert it into a dataframe
    df = process_data(data)

    # Export the dataframe to a CSV file
    filename = "meteorite_data.csv"
    export_to_csv(df, filename)
    print(f"Data exported to {filename} successfully.")

# Run the program
if __name__ == "__main__":
    main()

