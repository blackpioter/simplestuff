import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]
name = list(data["NAME"])


map = folium.Map(location=[40.7735, -111.9143], zoom_start=6)

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

fg = folium.FeatureGroup(name="My Map")
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe, parse_html=True), icon=folium.Icon(color='darkblue')))

map.add_child(fg)

map.save("Map1.html")
