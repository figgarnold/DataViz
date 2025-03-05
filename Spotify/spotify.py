#import libraries
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import first data source and view high level
raw_data = pd.read_csv(r"c:/Users/heath/Desktop/HFA_projects/Data_Viz/Spotify/spotify_history.csv")
print(raw_data.head())

#high level visualisation of the data 
artist_plot = sns.countplot(raw_data, x=raw_data["artist_name"])
print(artist_plot)

print(raw_data["skipped"].count())

