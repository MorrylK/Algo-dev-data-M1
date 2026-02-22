"""
API Station extractor
"""
import requests
from appmeteo.data_extractor.api_data_extractor import IAPIDataExtractor

class APIStationExtractor(IAPIDataExtractor):
    """
    Classe pour extraire le dernier relevé d'une station spécifique à partir de l'API
    """
    @staticmethod
    def extract(route):
        url = f"https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/{route}/"\
                "records?select=data%2C%20id%2C%20humidite%2C%20pression%2C%20"\
                "temperature_en_degre_c%2C%20heure_de_paris&order_by=-heure_utc&limit=1"
        response = requests.get(url, timeout=60)
        return response.json()
