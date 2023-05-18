# Question 5 -
# Write a program to download the data from the given API link and then extract the following data with
# proper formatting
# Link - http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes
# Note - Write proper code comments wherever needed for the code understanding

# Excepted Output Data Attributes -
# ● id - int 
# ● url - string
# ● name - string 
# ● season- int 
# ● number - int
# ● type - string 
# ● airdate - date format 
# ● airtime - 12-hour time format
# ● runtime - float
# ● average rating - float
# ● summary - string without html tags 
# ● medium image link - string
# ● Original image link - string


import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

# Function to download data from the provided API link
def download_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# Function to extract data attributes with proper formatting
def extract_data(data):
    # Extract episode information
    episodes = data.get('_embedded', {}).get('episodes', [])

    # Initialize empty lists to store extracted attributes
    episode_ids = []
    episode_urls = []
    episode_names = []
    episode_seasons = []
    episode_numbers = []
    episode_types = []
    episode_airdates = []
    episode_airtimes = []
    episode_runtimes = []
    episode_ratings = []
    episode_summaries = []
    episode_medium_images = []
    episode_original_images = []

    # Extract attributes for each episode
    for episode in episodes:
        episode_ids.append(episode.get('id', None))
        episode_urls.append(episode.get('url', None))
        episode_names.append(episode.get('name', None))
        episode_seasons.append(episode.get('season', None))
        episode_numbers.append(episode.get('number', None))
        episode_types.append(episode.get('type', None))
        episode_airdates.append(episode.get('airdate', None))
        episode_airtimes.append(episode.get('airtime', None))
        episode_runtimes.append(episode.get('runtime', None))
        episode_ratings.append(episode.get('rating', {}).get('average', None))
        
        # Remove HTML tags from the summary
        summary_html = episode.get('summary', None)
        if summary_html:
            soup = BeautifulSoup(summary_html, 'html.parser')
            summary = soup.get_text()
        else:
            summary = None
        episode_summaries.append(summary)

        episode_medium_images.append(episode.get('image', {}).get('medium', None))
        episode_original_images.append(episode.get('image', {}).get('original', None))

    # Create a dictionary of the extracted attributes
    data_dict = {
        'id': episode_ids,
        'url': episode_urls,
        'name': episode_names,
        'season': episode_seasons,
        'number': episode_numbers,
        'type': episode_types,
        'airdate': episode_airdates,
        'airtime': episode_airtimes,
        'runtime': episode_runtimes,
        'average rating': episode_ratings,
        'summary': episode_summaries,
        'medium image link': episode_medium_images,
        'original image link': episode_original_images
    }

    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data_dict)
    return df

# Function to export the dataframe to a CSV file
def export_to_csv(df, filename):
    df.to_csv(filename, index=False)

# Main function
def main():
    # Download data from the API link
    url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
    data = download_data(url)

    # Extract data attributes with proper formatting
    df = extract_data(data)

    # Export the dataframe to a CSV file
    filename = "westworld_episodes.csv"
    export_to_csv(df, filename)
    print(f"Data exported to {filename} successfully.")

# Run the program
if __name__ == "__main__":
    main()
