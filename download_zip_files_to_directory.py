# https://stackoverflow.com/questions/54616638/download-all-pdf-files-from-a-website-using-python

from urllib import request
from bs4 import BeautifulSoup as bs
import requests, re, os
from urllib.parse import urljoin


def download_all_zip(url, folder_location):
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')
    for link in soup.select("a[href$='.zip']"):
        #Name the .zip files using the last portion of each link, which are unique in this case
        filename = os.path.join(folder_location, link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url, link['href'])).content)


if __name__ == '__main__':
    url = "https://valuation.property.nsw.gov.au/embed/propertySalesInformation"

    # If there is no such folder, the script will create one automatically in your file path
    folder_location = 'property_values'
    if not os.path.exists(folder_location): os.mkdir(folder_location)

    download_all_zip(url, folder_location)