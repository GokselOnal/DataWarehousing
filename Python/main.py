from WebScraping import DataWebScraping
from API import DataAPI


data_api = DataAPI()
data_web = DataWebScraping()

if __name__ == '__main__':
    data_api.load_data()
    data_web.load_data()
