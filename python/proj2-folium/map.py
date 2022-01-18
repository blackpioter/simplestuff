import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]
name = list(data["NAME"])

def color_producer(elev):
    if elev < 1000:
        return "green"
    elif elev < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[40.7735, -111.9143], zoom_start=6)

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                     popup=folium.Popup(iframe, parse_html=True),
                                     fill_opacity=0.7,
                                     fill=True,
                                     color = 'grey',
                                     fill_color=color_producer(el)))

fgp = folium.FeatureGroup(name="Population")
with open('world.json', 'r', encoding='utf-8-sig') as file:
    data = file.read()
    fgp.add_child(folium.GeoJson(
            data=data,
            style_function=lambda x: {
                'fillColor':
                    'green' if x['properties']['POP2005'] < 10000000
                    else 'orange' if x['properties']['POP2005'] < 20000000
                    else 'red'
            }
        )
    )

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
