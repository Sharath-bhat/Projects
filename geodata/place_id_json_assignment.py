import urllib.request, urllib.parse, urllib.error
import json
# import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    # location = js['results'][0]['formatted_address']
    # print(location)
    placeid= js['results'][0]['place_id']
    print(placeid)


# {
#     "results": [
#         {
#             "address_components": [
#                 {
#                     "long_name": "Bengaluru",
#                     "short_name": "Bengaluru",
#                     "types": [
#                         "locality",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Bangalore Urban",
#                     "short_name": "Bangalore Urban",
#                     "types": [
#                         "administrative_area_level_2",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Karnataka",
#                     "short_name": "KA",
#                     "types": [
#                         "administrative_area_level_1",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "India",
#                     "short_name": "IN",
#                     "types": [
#                         "country",
#                         "political"
#                     ]
#                 }
#             ],
#             "formatted_address": "Bengaluru, Karnataka, India",
#             "geometry": {
#                 "bounds": {
#                     "northeast": {
#                         "lat": 13.173706,
#                         "lng": 77.8826809
#                     },
#                     "southwest": {
#                         "lat": 12.7342888,
#                         "lng": 77.3791981
#                     }
#                 },
#                 "location": {
#                     "lat": 12.9715987,
#                     "lng": 77.5945627
#                 },
#                 "location_type": "APPROXIMATE",
#                 "viewport": {
#                     "northeast": {
#                         "lat": 13.173706,
#                         "lng": 77.8826809
#                     },
#                     "southwest": {
#                         "lat": 12.7342888,
#                         "lng": 77.3791981
#                     }
#                 }
#             },
#             "place_id": "ChIJbU60yXAWrjsR4E9-UejD3_g",
#             "types": [
#                 "locality",
#                 "political"
#             ]
#         }
#     ],
#     "status": "OK"
# }