from secrets import SecretFile
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests


class DataWebScraping:
    def __init__(self):
        self.url_base       = SecretFile.url_base
        self.class_products = SecretFile.class_products
        self.class_name     = SecretFile.class_name
        self.class_brand    = SecretFile.class_brand
        self.class_rating   = SecretFile.class_rating
        self.class_price    = SecretFile.class_price
        self.list_ = list()
        self.num_items = 200
        self.steps = 24

    def extract_from_web_scrape(self):
        pid = 1
        for i in range((self.num_items // self.steps) + 1):
            data = requests.get(self.url_base + str(pid)).content
            soup = BeautifulSoup(data, "html.parser")
            products = soup.find_all("div", attrs={"class": self.class_products})
            for product in products:
                try:
                    name = product.find("span",   attrs={"class": self.class_name}).decode_contents().strip()
                    brand = product.find("span",  attrs={"class": self.class_brand}).decode_contents().strip()
                    rating = product.find("span", attrs={"class": self.class_rating}).decode_contents().strip()
                    price = product.find("div",   attrs={"class": self.class_price}).decode_contents().strip()
                    self.list_.append(
                        {"product_name"  : name,
                         "product_brand" : brand,
                         "product_rating": rating,
                         "product_price" : price}
                    )
                except AttributeError:
                    self.list_.append({"product_name": np.NaN, "product_brand": np.NaN, "product_rating": np.NaN, "product_price": np.NaN})
            if len(self.list_) % 24 == 0:
                pid += 1

    def save_extracted_data_as_csv(self):
        extracted_data = pd.DataFrame(self.list_)[:self.num_items]
        extracted_data.to_csv("data/products.csv", index=False)

    def load_data(self):
        self.extract_from_web_scrape()
        self.save_extracted_data_as_csv()