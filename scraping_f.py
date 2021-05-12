# Failed method to try scrape all .zip files into local directory

from bs4 import SoupStrainer, BeautifulSoup as bs
import requests, re, os
import urllib.request
from requests.api import request

# Connect to the valuer general website and get list of all .zip files
url = "https://valuation.property.nsw.gov.au/embed/propertySalesInformation"
req = requests.get(url)
soup = bs(req.text, 'html.parser')
links = soup.find_all('a', href=re.compile(r'(.zip)'))
# print(links)

# Clean the .zip link names
url_list = []
for el in links:
    url_list.append(("https://valuation.property.nsw.gov.au/embed/propertySalesInformation" + el['href']))
# print(url_list)


for url in url_list:
    print(url)
    fullfilename = os.path.join('/Users/MichaelHu/Documents/Internship/property_values', url.replace('https://valuation.property.nsw.gov.au/embed/propertySalesInformation','').replace('.zip',''))
    print(fullfilename)
    urllib.request.urlretrieve(url)

# for link in soup.find_all('a'):
#     url = link.get('href')
#     if url.endswith('.zip'):
#         print(url)
