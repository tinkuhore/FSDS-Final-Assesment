# Question 3: -
# Write a program, which would download the data from the provided link, and then read the data and convert
# that into properly structured data and return it in Excel format.
# Note - Write comments wherever necessary explaining the code written.
# Link - https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json

# Data Attributes - id: Identification Number - int num: Number of the
# ●
# ●
# ●Pokémon in the official Pokédex - int name: Pokémon name -
# string img: URL to an image of this Pokémon - string type:
# Pokémon type -string height: Pokémon height - float
# ●weight: Pokémon weight - float candy: type of candy used to evolve Pokémon or
# given
# ●
# when transferred - string candy_count: the amount of candies required to evolve
# - int
# ●egg: Number of kilometers to travel to hatch the egg - float spawn_chance:
# ●Percentage of spawn chance (NEW) - float avg_spawns: Number of this
# pokemon on 10.000 spawns (NEW) - int
# ●
# spawn_time: Spawns most active at the time on this field. Spawn times are the same for all
# time zones and are expressed in local time. (NEW) - “minutes: seconds” multipliers:
# Multiplier of Combat Power (CP) for calculating the CP after evolution See below - list of int
# weakness: Types of
# ●
# Pokémon this Pokémon is weak to - list of strings next_evolution: Number and Name of
# successive evolutions of Pokémon - list of dict prev_evolution: Number and Name of previous
# evolutions of Pokémon - - list of dict


import pandas as pd
import requests

# Function to download the data from the provided link
def download_data(url)-> dict:
    response = requests.get(url)
    data = response.json()
    return data

# Function to process the data and convert it into a properly structured dataframe
def process_data(data)->pd.DataFrame:
    # Extract the 'pokemon' field from the data
    pokemon_data = data['pokemon']

    # Create empty lists to store the extracted attributes
    ids = []
    nums = []
    names = []
    imgs = []
    types = []
    heights = []
    weights = []
    candies = []
    candy_counts = []
    eggs = []
    spawn_chances = []
    avg_spawns = []
    spawn_times = []
    multipliers = []
    weaknesses = []
    next_evolutions = []
    prev_evolutions = []

    # Iterate over each pokemon in the data and extract the attributes
    for pokemon in pokemon_data:
        ids.append(pokemon['id'])
        nums.append(pokemon['num'])
        names.append(pokemon['name'])
        imgs.append(pokemon['img'])
        types.append(pokemon['type'])
        heights.append(pokemon['height'])
        weights.append(pokemon['weight'])
        candies.append(pokemon['candy'])
        candy_counts.append(pokemon.get('candy_count', None))
        eggs.append(pokemon.get('egg', None))
        spawn_chances.append(pokemon.get('spawn_chance', None))
        avg_spawns.append(pokemon.get('avg_spawns', None))
        spawn_times.append(pokemon.get('spawn_time', None))
        multipliers.append(pokemon.get('multipliers', None))
        weaknesses.append(pokemon.get('weaknesses', None))
        next_evolutions.append(pokemon.get('next_evolution', None))
        prev_evolutions.append(pokemon.get('prev_evolution', None))

    # Create a dictionary of the extracted attributes
    data_dict = {
        'id': ids,
        'num': nums,
        'name': names,
        'img': imgs,
        'type': types,
        'height': heights,
        'weight': weights,
        'candy': candies,
        'candy_count': candy_counts,
        'egg': eggs,
        'spawn_chance': spawn_chances,
        'avg_spawns': avg_spawns,
        'spawn_time': spawn_times,
        'multipliers': multipliers,
        'weaknesses': weaknesses,
        'next_evolution': next_evolutions,
        'prev_evolution': prev_evolutions
    }

    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data_dict)
    return df

# Function to export the dataframe to an Excel file
def export_to_excel(df, filename):
    df.to_excel(filename, index=False)

# Main function
def main():
    # Download the data from the provided link
    url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    data = download_data(url)

    # Process the data and convert it into a dataframe
    df = process_data(data)

    # Export the dataframe to an Excel file
    filename = "pokemon_data.xlsx"
    export_to_excel(df, filename)
    print(f"Data exported to {filename} successfully.")

# Run the program
if __name__ == "__main__":
    main()
