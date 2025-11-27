from appmeteo.main_objects.record import Record
from appmeteo.main_objects.station import Station
from appmeteo.printing.record_printing import RecordPrinting
from appmeteo.printing.iprinting import IPrinting
import requests
import pandas as pd

class StationPrinting(IPrinting):
    @staticmethod
    def print(station: Station):
        url = f"https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/{station.api_label}/records?select=data%2C%20id%2C%20humidite%2C%20pression%2C%20temperature_en_degre_c%2C%20heure_de_paris&order_by=-heure_utc&limit=1"
        response = requests.get(url)
        data = response.json()
        if not data.get('results'):
            print("Aucun résultat trouvé pour cette station.")
            return
        data = pd.DataFrame(data['results']).iloc[0] # première ligne
        record = Record(data["temperature_en_degre_c"], data["humidite"], data["pression"], data["heure_de_paris"], station)
        RecordPrinting.print(record)