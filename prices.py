from bs4 import BeautifulSoup
from urllib2 import urlopen

my_address = "http://www.irishtimes.com/"
html_page = urlopen(my_address)
html_text = html_page.read()
soup = BeautifulSoup(html_text, "html.parser")

# Create a list to store our images in
prices = []
# Store the images in the list
prices = soup.find_all("departure-total-price")

# Iterate over 'images' list and
# print the 'src' of each image
for departure-total-price in prices:
    print departure-total-price