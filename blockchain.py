import requests
from bs4 import BeautifulSoup as bs
url = 'https://blockchain.info/balance?active='
var = ("393WFWHcA4JmehmKNKEzizwQi31zR595JG|1GKfk53nujZZEYZg86pPH5xmUM77Q8umq5|39cESrNC9EB1Ke4MwYMkAD89G45pMvtVaF")

req = requests.get(url + str(var))
soup = bs(req.text, 'html.parser')
print(soup)