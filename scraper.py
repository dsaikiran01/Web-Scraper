import requests
from bs4 import BeautifulSoup
import re

def scrape():
    url = "https://www.example.com/" #give your own url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # storing the scraped data in a file name with domain
    match = re.search(r'https?://(?:www\.)?([^.]+)', url)
    filename = match.group(1)
    #change extension from txt to html for html page
    with open(f"{filename}.txt", "w") as file:
        file.write(f'''{soup.html}''')

if __name__ == "__main__":
    scrape()