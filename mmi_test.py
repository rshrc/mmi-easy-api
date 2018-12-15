from mmi import MapMyIndia

print("Testing for MapMyIndia Python Class")
testing = MapMyIndia()
print("Testing for MapMyIndiaCustomLicense Python Class")
testing = MapMyIndiaPythonCustomLicense("zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5")
print("MapMyIndiaPythonCustomLicense class initialized")
print("Geocoding")
print(testing.geocoding("Asansol", 713304).content)
print("Reverse Geocoding ")
print(testing.reverse_geocoding(41, -71).content)
print("Still Map Image ")
print(testing.still_map_image().content)
print("Nearby Places ")
print(testing.nearby_places("shoes").content)
print("eLoc API")
print(testing.eLoc("D75CA2").content)
print("Routing")
print(testing.routing("28.111,77.111", "28.22, 77.22").content)
print("Driving Distance Matrix")
print(testing.driving_distance_matrix().content)
