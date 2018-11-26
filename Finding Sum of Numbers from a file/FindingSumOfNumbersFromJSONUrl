import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Enter the URL from which the data has to be read
url = input('Enter - ')
urlReq = urllib.request.urlopen(url)

data=urlReq.read().decode()

try:
    #The data read from URL is of JSON format
    dataJSON=json.loads(data)
    sumTot = 0
    commentsList = dataJSON['comments']
    for comment in commentsList:
        sumTot = sumTot + int(comment['count'])

    print(sumTot)
except:
    dataJSON=None

