from secrets import SecretFile
import pandas as pd
import requests


class DataAPI:
    def __init__(self):
        self.url = "https://api.api-ninjas.com/v1/city"
        self.headers = {'X-API-KEY': SecretFile.api_key}
        self.country_list = ["US", "TR", "DE", "ES", "JP", "GB", "RU"]
        self.extracted_data = pd.DataFrame(columns=['name', 'latitude', 'longitude', 'country', 'population', 'is_capital'])
        self.num_items = 200

    def extract_from_api(self):
        for country in self.country_list:
            request = self.url + f"?country={country}&limit=30"
            response = requests.request("GET", request, headers=self.headers)
            data = pd.DataFrame(response.json())
            self.extracted_data = pd.concat([self.extracted_data, data], axis=0, ignore_index=True)

    def save_extracted_data_as_csv(self):
        self.extracted_data[:self.num_items].to_csv("data/cities.csv", index=False)

    def load_data(self):
        self.extract_from_api()
        self.save_extracted_data_as_csv()
