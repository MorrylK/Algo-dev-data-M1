"""
API Stations
"""
import pandas as pd
import requests
from appmeteo.data_extractor.api_data_extractor import IAPIDataExtractor

class APIStations(IAPIDataExtractor):
    """
    Classe pour extraire les stations à partir de l'API
    """
    @staticmethod
    def extract():
        url = "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/stations-meteo-en-place/records?select=id_nom%2C%20id_numero%2C%20ville&order_by=id_numero&limit=80"
        response = requests.get(url, timeout=60)
        stations = response.json()
        return pd.DataFrame(stations['results'])
