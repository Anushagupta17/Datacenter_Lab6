from __future__ import print_function
import requests
import json
import sys
import time

ip = sys.argv[1]
endpoint_name = sys.argv[2]
iterations = int(sys.argv[3])
queries = iterations

addr = 'http://'+ ip +':5000'

# prepare headers for http request
if endpoint_name == 'image':
    headers_value = 'image/png'
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
else:
    headers_value = 'text/plain'

headers = {'content-type': headers_value}
# send http request with data and receive response
url = addr + '/api/' + endpoint_name

start_time = time.time()
while iterations > 0:
    if endpoint_name == 'image':
        response = requests.post(url, data=img, headers=headers)
    else:
        url = url + '/10/20'
        response = requests.post(url, headers=headers)
    # decode response
    print("Response is", response)
    print(json.loads(response.text))
    iterations = iterations - 1

print("Time taken = ", ((time.time() - start_time) * 1000)/queries, " millisecs")
