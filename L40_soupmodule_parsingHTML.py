import bs4 #beautifulsoup4
import requests # to handle actual downloading
def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    soup.select('')

### couldn't complete as the example on Amazon has changed
### since publicatoion


price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_2?crid=2E9FM44U92NQO&dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1607313537&sprefix=automate+the+bor%2Caps%2C229&sr=8-2')
print('The price is ' + price)




