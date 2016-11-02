import json, http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '52e1f43aa3114e8b924af3f84693877b',
}

params = urllib.parse.urlencode({
    # Request parameters
    'q': 'cats',
    'count': '10',
    'offset': '0',
    'mkt': 'en-us',
    'safeSearch': 'Moderate',
})

try:
    conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    parsed_data = json.loads(data)
    print(parsed_data['value'][0]['thumbnailUrl'])
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))