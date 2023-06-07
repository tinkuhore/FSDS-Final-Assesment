import time
import urllib.request
import zipfile
import os

# Specify the URL to download the data from
data_url = "https://www.kaggle.com/competitions/microsoft-malware-prediction/data"

# current dir
cwd = os.getcwd()

# Specify the path to save the downloaded zip file
zip_path = os.path.join(cwd, "data/data.zip")

# Specify the path to save the unzipped data
data_folder = os.path.join(cwd, "data/")

# Create the data folder if it doesn't exist
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

start = time.time()
# Download the zip file
urllib.request.urlretrieve(data_url, zip_path)

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(data_folder)

# Remove the zip file
os.remove(zip_path)

end=time.time()
# Print a message indicating the completion
print("Data downloaded and extracted successfully!")

# Calculate the time taken
elapsed_time = end - start

# Print the time taken
print("Time taken: {:.2f} seconds".format(elapsed_time))
