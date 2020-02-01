from bs4 import BeautifulSoup
import requests

headers = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0' }
def main(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    price = soup.find(id='priceblock_ourprice')
    return([soup,price])


def checkprice(url):
    f=1
    while f:
        price=main(url)
        soup=price[0]
        price=price[1]
        if price!=None:
            price = price.get_text()
            title = soup.find(id='productTitle')
            title = title.get_text().strip()
            print(title)
            print(price[2:])
            f=0
            return([title,price])
        else:
            print("fail")
