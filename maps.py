import folium


# cri
maps = folium.Map(
    location =[],
    tiles = "Stamen Terrain",
    zoom_start = 16
)

folium.Marker(
    [],
    popup = "<i>Pr </i>",
    tooltip = "Click"
).add_to(maps)

maps.save(r'.\maps.html')