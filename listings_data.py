import pandas
import requests

def filter_listings():

    """ Function to read 'listings.csv' and extract only 
    the necessary data (latitude, longitude and price),
    converts latitude and longitude to the proper outcode and
    creates a new csv file 'newlistings' """
    
    latitudes = []
    longitudes = []
    prices = []
    outcodes = []
    outcodes = []

    data = pandas.read_csv('listings.csv')

# extracts prices, latitude and longitudo from listings.csv
# and appends to its lists
    for i in range(len(data)):
        lat = data['latitude'][i]
        lgn = data['longitude'][i]
        price = data['price'][i]
        prices.append(price)
        latitudes.append(lat)
        longitudes.append(lgn)

# using latitude and longitude calculates the outcode and
# appends to outcodes list
    for i in range(len(data)):
        params = {
            "lon": longitudes[i],
            "lat": latitudes[i],
        }
        response = requests.get("http://api.postcodes.io/outcodes", params=params)
        data = response.json()
        out = data['result'][0]['outcode']
        outcodes.append(out)

    

# creates newlistings.csv with outcode and price only
    rows =[]
    for i in range(len(outcodes)):
        rows.append([outcodes[i], prices[i]])

    df = pandas.DataFrame(rows, columns=['outcode', 'price'])
    df.to_csv('newlistings.csv')

if __name__ == '__main__':
    filter_listings()



