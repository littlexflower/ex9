import requests
import json

api_key_path = r'C:\Users\Ms. Kim Hoa\pyfml\exercises\api_maps.txt'
features = []

with open(api_key_path, 'r') as f:
    your_api_key = f.read()

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'\
      'location=-33.8670522,151.1957362&radius=2000&type=restaurant&key={}'\
      .format(your_api_key)

resp = requests.get(url)
content = json.loads(resp.text)

for i in content['results']:
    features.append(
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    i['geometry']['location']['lat'],
                    i['geometry']['location']['lng']
                ]
            },
            'properties': {
                'name': i['name'],
                'address': i['vicinity']
            }
        }
    )

format_geojson = {
    'type': 'FeatureCollection',
    'features': features
}

with open('pymi_beer.geojson', 'w') as f:
    json.dump(format_geojson, f)
