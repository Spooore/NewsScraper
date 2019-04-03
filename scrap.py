from bs4 import BeautifulSoup
import requests

url = "http://www.bbc.co.uk/news/world-us-canada-47797478"
content_list =[]

page_response = requests.get(url, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

content=page_content.find_all("p")

for s in content:
    content_list.append(s.text.strip().replace('$',''))

print(content_list)