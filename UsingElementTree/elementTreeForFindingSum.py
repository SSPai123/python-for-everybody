#ElementTree represents the whole XML document as a tree, and Element represents a single node in this tree.
#Used to read and parse XML files

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Enter the location of the XML file
url = input('Enter - ')
data = urlopen(url, context=ctx).read()

print('Retrieved', len(data), 'characters')

#Parses an XML section from a string constant.
#Returns Element Instance
tree = ET.fromstring(data)

#Finds all matching subelements, by tag name or path. Returns a list containing all matching elements in document order.
results = tree.findall('.//count')

#Iterate through the element list and get the sum
sumTot=0
for result in results:
    #Element.text accesses the element’s text content.
    sumTot=sumTot+int(result.text)

print(sumTot)
