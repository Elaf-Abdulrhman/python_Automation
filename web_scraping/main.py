import requests
from bs4 import BeautifulSoup
URL = 'https://www.namshi.com/saudi-en/buy-adidas-ultraboost-light-w/Z25EE2FDF0914CE5D1943Z/p/'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

product_title = soup.find(class_='ProductConversion_productTitle__dvlc5').get_text()
product_price = soup.find(class_='ProductPrice_value__hnFSS').get_text()
product_price_value = int(product_price[1:4])

print(product_title)
print(product_price_value)

def check_price():
    if(product_price_value < 200):
        print('Congrats!! the price has fallen to : $',
            product_price_value  )
    else:
        print('Unfortunately the price is still above $500')

if __name__ == "__main__":
    check_price()