"""
Record
"""
import datetime
from appmeteo.main_objects.station import Station

class Record:
    """
    Objet Record racine pour les enregistrements
    """
    def __init__(self, temperature:float, humidite:int, pression:int, heure:datetime, station:Station) -> None:
        self.temperature:float = temperature
        self.humidite:int = humidite
        self.pression:int = pression
        self.heure:datetime = heure
        self.station:Station = station
