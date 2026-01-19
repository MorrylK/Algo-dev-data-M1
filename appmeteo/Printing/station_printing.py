"""
Station printing
"""
import requests
import pandas as pd
from appmeteo.main_objects.record import Record
from appmeteo.main_objects.station import Station
from appmeteo.printing.record_printing import RecordPrinting
from appmeteo.printing.iprinting import IPrinting

class StationPrintingDecorator(IPrinting):
    """
    Classe decorator pour l'affichage d'une station.
    """
    def __init__(self, station: Station):
        self.station = station

    def print(self):
        url = f"https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/{self.station.api_label}/records?select=data%2C%20id%2C%20humidite%2C%20pression%2C%20temperature_en_degre_c%2C%20heure_de_paris&order_by=-heure_utc&limit=1"
        response = requests.get(url, timeout=60)
        data = response.json()
        if not data.get('results'):
            print("Aucun résultat trouvé pour cette station.")
            return
        data = pd.DataFrame(data['results']).iloc[0] # première ligne
        record = Record(data["temperature_en_degre_c"], data["humidite"], data["pression"], data["heure_de_paris"], self.station)
        RecordPrinting.print(record)
