from datetime import timedelta, datetime
from random import randrange
import pandas as pd


class TransformData:
    def __init__(self):
        self.path_shell = "/home/goksel/Documents/DataWarehousing/Shell"
        self.path_sql   = "/home/goksel/Documents/DataWarehousing/SQL"
        self.extracted_df   = None
        self.transformed_df = None
        self.country_map = {"US": "United States",
                            "TR": "Turkey",
                            "DE": "Deutschland",
                            "ES": "Spain",
                            "JP": "Japan",
                            "GB": "United Kingdom",
                            "RU": "Russian Federation"}

    def get_data(self):
        customers_df = pd.read_csv(self.path_shell + "/data_from_server/customers.csv")
        products_df  = pd.read_csv(self.path_shell + "/data_from_server/products.csv")
        cities_df    = pd.read_csv(self.path_shell + "/data_from_server/cities.csv")
        self.extracted_df   = pd.concat([customers_df, cities_df, products_df], axis=1)
        self.transformed_df = self.extracted_df.copy()

    def transform_df(self):
        self.transformed_df.columns = [col.upper() for col in self.transformed_df.columns]

        self.transformed_df.rename(columns={
            "ANNUAL_INCOME_(K$)": "ANNUAL_INCOME",
            "LATITUDE": "CITY_LATITUDE",
            "LONGITUDE": "CITY_LONGITUDE",
            "COUNTRY": "COUNTRY_CODE",
            "POPULATION": "CITY_POPULATION",
            "CUSTOMERID": "CUSTOMER_ID",
            "NAME": "CITY_NAME",
        }, inplace=True)

        self.transformed_df.ANNUAL_INCOME = self.transformed_df.ANNUAL_INCOME * 1000
        self.transformed_df.IS_CAPITAL = self.transformed_df.IS_CAPITAL.astype("i")
        self.transformed_df.PRODUCT_RATING = self.transformed_df.PRODUCT_RATING.str.strip("()")
        self.transformed_df.PRODUCT_RATING = self.transformed_df.PRODUCT_RATING.astype("i")
        self.transformed_df["COUNTRY_NAME"] = self.transformed_df.COUNTRY_CODE.map(self.country_map)
        self.transformed_df.PRODUCT_PRICE = self.transformed_df.PRODUCT_PRICE.apply(
            lambda val: val.replace(".", "").replace(",", ".").strip(" TL")).astype("float")

        def create_random_date(start, end):
            diff = end - start
            int_diff = (diff.days * 24 * 60 * 60) + diff.seconds
            random_second = randrange(int_diff)
            return start + timedelta(seconds=random_second)

        date_start = datetime.strptime("1/1/2021 1:00 AM", "%m/%d/%Y %I:%M %p")
        date_end = datetime.strptime("1/1/2022 1:00 AM", "%m/%d/%Y %I:%M %p")

        self.transformed_df["DATE"] = [create_random_date(date_start, date_end) for _ in
                                       range(self.transformed_df.shape[0])]

    def load_data(self):
        self.get_data()
        self.transform_df()
        self.extracted_df.to_csv(self.path_shell + "/data_from_server/extracted_data_total.csv", index=False)
        self.transformed_df.to_csv(self.path_sql + "/data/transformed_data.csv", index=False)


if __name__ == '__main__':
    transform = TransformData()
    transform.load_data()



