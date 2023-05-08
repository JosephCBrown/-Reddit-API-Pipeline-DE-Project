from config import CLIENT_ID,CLIENT_SECRET
import requests
import json
from datetime import datetime
import csv


# set up API endpoint URL and headers
endpoint = 'https://www.reddit.com/api/v1/access_token'
headers = {'User-Agent': 'MyAPI/0.0.1'}

# authenticate with Reddit API and retrieve access token, id and key stored in config file.
data = {'grant_type': 'client_credentials'}
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
response = requests.post(endpoint, auth=auth, data=data, headers=headers)
access_token = response.json()['access_token']

# set up parameters for API request
url = 'https://oauth.reddit.com/r/dataengineering'
headers = {'Authorization': f'Bearer {access_token}', 'User-Agent': 'MyAPI/0.0.1'}
params = {'limit': 1000}

# send API request and print results
response = requests.get(url, headers=headers, params=params)
data = response.json()


# to test in the commandline
""" for post in data['data']['children']:
    date_time = datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Author: {post['data']['author']}")
    print(f"Title: {post['data']['title']}")
    print(f"Number of upvotes: {post['data']['ups']}")
    print(f"Number of downvotes: {post['data']['downs']}")
    print(f"Number of comments: {post['data']['num_comments']}")
    print(f"Date of post: {date_time}")
    print("----------")
 """

# Extract data and write to CSV file
with open('dataengineering_posts.csv', 'w', newline='') as csvfile:
    fieldnames = ['Author', 'Title', 'Upvotes', 'Downvotes', 'Comments', 'Date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for post in data['data']['children']:
        date_time = datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow({'Author': post['data']['author'], 'Title': post['data']['title'],
                         'Upvotes': post['data']['ups'], 'Downvotes': post['data']['downs'],
                         'Comments': post['data']['num_comments'], 'Date': date_time})