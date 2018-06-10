
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#APIキーの情報
key = "a5f8e5a9000b5a4e131c927b8f611b3e"
secret = "4746554464a8716f"
wait_time=1

animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text=animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search =  1,
    extras = 'url_q, licence'
)

photos = result['photos']

# 返り値を表示する
# pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    pprint(url_q)
    filepath = savedir + '/' + photo['id'] + '.jpg'
    pprint(filepath)
    if os.path.exists(filepath):continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)




