from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_asset_management_firms'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html5lib')

table = soup.find('table', class_ ='wikitable')
print(soup.prettify())

for row in table.find_all('tr')[1:]: 
    columns = row.find_all(['th', 'td'])
    if columns:
        rank = columns[0].text.strip()
        firm_name = columns[1].text.strip()
        country = columns[2].text.strip()
        value = columns[3].text.strip() #value is in billions
        print(f"Rank: {rank}, Firm Name: {firm_name}, Country: {country}, Value: {value}")
