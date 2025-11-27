from appmeteo.DataExtractor.APIDataExtractor import IAPIDataExtractor
import pandas as pd
import requests

class APIStations(IAPIDataExtractor):
    @staticmethod
    def extract():
        url = "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/stations-meteo-en-place/records?select=id_nom%2C%20id_numero%2C%20ville&order_by=id_numero&limit=80"
        response = requests.get(url)
        stations = response.json()
        return pd.DataFrame(stations['results'])