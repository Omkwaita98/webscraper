from bs4 import BeautifulSoup
import requests

search = input("Search for:")
params = {"q", search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)

        children = item.find("h2")
        print("Next sibling of the h2:", children.next_sibling)