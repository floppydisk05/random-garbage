import requests
import re
from bs4 import BeautifulSoup
import os

query = input("Enter query: ")
print("Querying WinWorld...")

# Get page from search url + query and parse with bs4
url = f"https://winworldpc.com/search?q={query}"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Find all titles from results
results = soup.find_all("div", class_="mt-0")

res = []

# Append all titles found to array
i = 1
for result in results:
    tmp = []
    tmp.append(i)
    for item in result.find("a"):
        tmp.append(re.sub(' +', ' ', item))
    for item in result.find_all("a", href=True):
        tmp.append(f"https://winworldpc.com{item['href']}")
    res.append(tmp)
    i += 1


print(f"There were {len(res)} results for \"{query}\"...")
for item in res:
    print(f"{str(item[0])} -  {item[1]}")

idx = int(input("Enter ID of product to open: ")) - 1
os.system(f"microsoft-edge-dev {res[idx][2]}")