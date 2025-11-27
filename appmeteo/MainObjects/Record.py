from appmeteo.MainObjects.Station import Station
import datetime

class Record:
    def __init__(self, temperature:float, humidite:int, pression:int, heure:datetime, station:Station) -> None:
        self.temperature:float = temperature
        self.humidite:int = humidite
        self.pression:int = pression
        self.heure:datetime = heure
        self.station:Station = station