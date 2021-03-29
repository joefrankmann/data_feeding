import pandas
import requests

def post_outcode():
    df = pandas.read_csv('newlistings.csv')
    
    item_counts = df["outcode"].value_counts()
    item_counts = item_counts.to_frame()
    outcode_codes = []
    listing_counts = []
    total_daily_rate = []
    average_daily_rate = []

    for ind in item_counts.index: 
        outcode_codes.append((ind).lower())
        listing_counts.append(item_counts['outcode'][ind])
        total_daily_rate.append(df[df['outcode']==ind]['price'].sum())

    for i in range(len(listing_counts)):
        x = round((total_daily_rate[i] / listing_counts[i]), 2)
        average_daily_rate.append(x)

    for i in range(len(outcode_codes)):
        url = "http://127.0.0.1:8000/api/outcode/"
        data = {
            'outcode_code': outcode_codes[i],
            'listing_count': listing_counts[i],
            'average_daily_rate': average_daily_rate[i]
            }
        headers = {'Content-type': 'application/json'}
        post = requests.post(url, data=data)
        print(post)

if __name__ == '__main__':
    post_outcode()

