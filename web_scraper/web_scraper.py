import requests
from bs4 import BeautifulSoup
from pyspark.sql.types import StructType, StructField, StringType

class Mazda_Cars:
    header = StructType([
    StructField('Model', StringType(), True),
    StructField('Calendar Year Introduced', StringType(), True),
    StructField('Current Model Introduced', StringType(), True),
    StructField('Lift', StringType(), True),
    StructField('Description', StringType(), True)])

    def __init__(self):
        self.response = requests.get('https://en.wikipedia.org/wiki/List_of_Mazda_vehicles')
        self.soup = BeautifulSoup(self.response.text, features="html.parser")
    def get_all_cars(self):
        models_list = []
        table = self.soup.find('table', attrs={'class':'wikitable'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 1:
                cols = [ele.text.strip() for ele in cols]
                models_list.append([ele for ele in cols if ele])
        return models_list

        
