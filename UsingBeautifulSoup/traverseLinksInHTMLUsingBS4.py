# To find the link at position n (the first name is 1). Follow that link. Repeat this process m times. 
# The answer is the last name that you retrieve.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#Enter the URL. For example:  http://py4e-data.dr-chuck.net/known_by_Lani.html
url = input('Enter URL - ')

#Enter the position of the URL link to be followed
position = input('Enter position - ')

#Enter the count for which the traversal has to be repeated
count = input('Enter count - ')

lastTag=None
tagHref=url

#Loop for which traversal has to be repeated
for i in range(0,int(count)):
    html = urlopen(tagHref, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')

    index=0
    #Loop to get the nth position tag
    for tag in tags:
        index=index+1
        if index==int(position):
            tagHref=tag.get('href', None)
            lastTag=tag
            print("Retrieving: ",tagHref)

#Print the contents of the last tag
print(lastTag.contents[0])

