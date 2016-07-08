import googlemaps

gmaps = googlemaps.Client(key='AIzaSyA7wJXHCIogCwz6D5ymPxdN5DMmaueFsco')

geocode_result = gmaps.geocode('pondok bambu')

for eachk in geocode_result:
    print eachk

