import requests
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import io
import math
import os
import time
import geocoder
import webbrowser

#set parent directory
current_directory = os.path.dirname(__file__)

#create function to access API and save to dataframe
def list_stations(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.read_csv(io.StringIO(response.text))
        return data
    
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to calculate Haversine distance between two lat/long points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c  # Distance in km
    return distance

#define URL and call function
url = "https://www2.sepa.org.uk/rainfall/api/Stations?csv=true"
stations = list_stations(url)

#Tell GeoPandas which columns to use for data points
geostations = gpd.GeoDataFrame(stations, geometry=gpd.points_from_xy(stations["station_longitude"], stations["station_latitude"]), crs="EPSG:4326")

# Plot the stations
ax = geostations.plot(marker='*', color='green', markersize=10)
plt.title("SEPA Rainfall Stations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("rainfall_stations.png")  # Save the plot as an image
plt.show()

#create file
file = open("rainfall.txt", "w")
file.write("SEPA Rainfall Stations\n")      

#update user location long/lat
g = geocoder.ip('me')
if g.latlng:  # Check if we got a valid location
    user_lat, user_lon = g.latlng
    file.write(f"\nBased on your IP, your current latitude is {user_lat}, and your current longitude {user_lon}\n")

    # Find nearest rainfall station
    nearest_station = None
    min_distance = float('inf')

    for index, row in geostations.iterrows():
        station_lat = row['station_latitude']
        station_lon = row['station_longitude']
        distance = haversine(user_lat, user_lon, station_lat, station_lon)

        if distance < min_distance:
            min_distance = distance
            nearest_station = row['station_name']  # Adjust this to the correct column name for the station name

    file.write(f"Your nearest station is: {nearest_station} at {min_distance:.2f} km away.\n")
else:
    file.write("\nCould not get your location.\n")

file.close()

# Open the file in a browser
webbrowser.open("rainfall.txt")