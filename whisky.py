import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd 
import os 

headers = {
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}

productlisk = []
p_name = []
p_rating = []
p_price = []

for page in tqdm(range(1,4)):
    heml = requests.get(f'https://www.whiskyshop.com/scotch-whisky?p={page}')

    soup = BeautifulSoup(heml.content, "lxml")
    productlisk = soup.find_all('li', class_ = 'item product-item')

    for product in tqdm(productlisk):
        prod_name = product.find('a', class_='product-item-link').text.strip()

        try:
            price = product.find('span', class_='price').text.repalce("£","")
        except:
            price = 'sold out'

        p_name.append(prod_name)
        p_price.append(price)

product = {
    "Name":p_name,
    "price":p_price
}
df = pd.DataFrame(product)
df.to_csv('whisky.csv')