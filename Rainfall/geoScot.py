import geopandas as gpd

url = r"https://www2.sepa.org.uk/rainfall/api/Stations?csv=true"
scotland = gpd.read_file(url)

scotland.plot()



#setting up turtle map
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)
# load the map image
screen.bgpic(r"C:\Users\heath\Desktop\HFA_projects\Data_Viz\Rainfall\map.gif")
screen.register_shape(r"C:\Users\heath\Desktop\HFA_projects\Data_Viz\Rainfall\icon.gif")
icon = turtle.Turtle()
icon.shape(r"C:\Users\heath\Desktop\HFA_projects\Data_Viz\Rainfall\icon.gif")
icon.shapesize(stretch_wid=0.05, stretch_len=0.05) 
icon.setheading(4)
icon.penup()

while True:
    # Update the user location on the map
    icon.goto(g.latlng)

    # Refresh every 5 seconds
    time.sleep(5)