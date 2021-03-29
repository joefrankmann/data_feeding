import pandas
import requests
from outcode_nearst import get_nearest_outcode_and_distance

def post_nearest_outcodes():
    df = pandas.read_csv('newlistings.csv')
    
    item_counts = df["outcode"].value_counts()
    item_counts = item_counts.to_frame()
    outcode_codes = []
    listing_counts = []
    total_daily_rate = []
    average_daily_rate = []

    # calculates the total daily rate for each outcode
    # and appends its values to the same index on total_daily_rate list
    for ind in item_counts.index: 
        outcode_codes.append((ind).lower())
        listing_counts.append(item_counts['outcode'][ind])
        total_daily_rate.append(df[df['outcode']==ind]['price'].sum())

    # takes the total daily rate by index and calculates 
    # the average daily rate for each index
    for i in range(len(listing_counts)):
        x = round((total_daily_rate[i] / listing_counts[i]), 2)
        average_daily_rate.append(x)

    # as each index of the lists outcode_codes, listing_counts, 
    # average_daily_rate represents the same outcode, the function below
    # creates a json(dictionary) with all the values and posts it to the database 
    for x in range(11):
        for i in range(len(outcode_codes)):
        # url = "http://127.0.0.1:8000/api/nexus/"
            if len(get_nearest_outcode_and_distance(outcode_codes[i])) == x:
                data = {
                    'outcode_code': outcode_codes[i],
                    'listing_count': listing_counts[i],
                    'average_daily_rate': average_daily_rate[i],
                }
                for j in range(x):
                    data[f'distance_{j+1}'] = get_nearest_outcode_and_distance(outcode_codes[i])[j][1]
                    data[f'next_outcode_{j+1}'] = get_nearest_outcode_and_distance(outcode_codes[i])[j][0]
                print(data)
                # post = requests.post(url, data=data)
                # print(post)
            
if __name__ == '__main__':
    post_nearest_outcodes()

        





