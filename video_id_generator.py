import json
import urllib.request
import string
import random, time
count = 50
# API_KEY = 'AIzaSyBJ7-Vj16CX7RQ4fT-fGtAXG5KX_K1CO_E'
# API_KEY = 'AIzaSyAm9kBVxO-2bjWGI9FqFkkSKgOTH5fCF1A'
with open("key.txt", 'r') as f:
    API_KEY = f.readline()
    print(API_KEY)
ids = set()
for i in range (60):
    randomQuery = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,randomQuery)

    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))
    time.sleep(8)
    for data in results['items']:
        videoId = (data['id']['videoId'])
        #store your ids
        ids.add(videoId)
    print('Videos added, current size: ', len(ids))

with open("video-ids.csv", "r") as f:
    for id in ids:
        f.write(id + ",")