"""
Station printing
"""
import pandas as pd
from appmeteo.data_extractor.api_station_extractor import APIStationExtractor
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
        data = APIStationExtractor.extract(self.station.api_label)
        if not data.get('results'):
            print("Aucun résultat trouvé pour cette station.")
            return
        data = pd.DataFrame(data['results']).iloc[0] # première ligne
        record = Record(data["temperature_en_degre_c"], data["humidite"], \
            data["pression"], data["heure_de_paris"], self.station)
        print(self.station.nom.center(60, "-"))
        RecordPrinting.print(record)
