import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape
url = input("URL please!!!")

# Send a request to the URL and get the content
response = requests.get(url)
content = response.content

# Parse the content with Beautiful Soup
soup = BeautifulSoup(content, "html.parser")

# Find all the elements you're interested in
# (in this example, we're finding all <p> tags)
paragraphs = soup.find_all("p")

# Print out the text of each element
for paragraph in paragraphs:
    print(paragraph.text)
