import requests
from lxml import html 
url = 'https://authoraditiagarwal.com/leadershipmanagement/'
path = '//*[@id="panel-836-0-0-1"]/div/div/p[1]'
response = requests.get(url)
byte_string = response.content
source_code = html.fromstring(byte_string)
tree = source_code.xpath(path)
print(text_content()) 
