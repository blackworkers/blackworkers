
import requests

def reverse_geocode(lat, lon):
    url = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?f=pjson&featureTypes=&location=" + str(lon) + "," + str(lat)

    req = requests.get(url)

    query=req.json()

    location = {}

    location['city'] = query['address']['City']
    location['state'] = query['address']['Region']
    location['country']=query['address']['CountryCode']

    return location

print(reverse_geocode('33.522960010097982','-112.0232999405623'))
