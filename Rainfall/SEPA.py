import requests
import pandas as pd
import geopandas as gpd
import matplotlib as mpl
import io
import time
import geocoder
import webbrowser

#create function to access API
def list_stations(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.read_csv(io.StringIO(response.text))
        print(data.head)
        return data
    
    else:
        print(f"Error: {response.status_code}")
        return None

url = "https://www2.sepa.org.uk/rainfall/api/Stations?csv=true"
stations = list_stations(url)
geostations = gpd.GeoDataFrame(stations, geometry=gpd.points_from_xy(stations["station_longitude"], stations["station_latitude"]), crs="EPSG:4326")
geostations.plot()

#create file
file = open("rainfall.txt", "w")
file.write(
    "SEPA Rainfall Stations"
)      

#update user long/lat
g = geocoder.ip('me')
nearest = "TBC"
file.write("\nYour current lat / long is: " + str(g.latlng) + "\n Your nearest station is: " + str(nearest))
file.close()
webbrowser.open("rainfall.txt")
