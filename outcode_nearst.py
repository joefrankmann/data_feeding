import requests
from geopy.distance import geodesic

def get_nearest_outcode_and_distance(outcode_code):

    """ Returns a nested list of the 10 nearest outcodes 
    and its distances in miles from a given valid outcode in the UK 
    param=lower string"""

    outcode_code = outcode_code
    response = requests.get(f'http://api.postcodes.io/outcodes/{outcode_code}/nearest/')
    data = response.json()

    lat_org = float(data['result'][0]['latitude'])
    long_org = float(data['result'][0]['longitude'])

    outcode_list = []
    distance_list = []
    outcode_and_distance = []

    for i in range(len(data['result'])):
        lat_dest = float(data['result'][i]['latitude'])
        long_dest = float(data['result'][i]['longitude'])
        origin = (lat_org, long_org)  # (latitude, longitude) don't confuse
        dest = (lat_dest, long_dest)
        # distance_mts = geodesic(origin, dest).meters
        # distance_km = geodesic(origin, dest).kilometers
        distance_miles = geodesic(origin, dest).miles
 
        nearest_outcode = data['result'][i]['outcode']
        distance_miles = round(distance_miles, 2)
      
        outcode_list.append(nearest_outcode.lower())
        distance_list.append(distance_miles)
        nested_list = []
        nested_list.append(outcode_list[i])
        nested_list.append(distance_list[i])
        outcode_and_distance.append(nested_list)

    return outcode_and_distance
    # print(len(outcode_and_distance))
    # print(outcode_and_distance)

