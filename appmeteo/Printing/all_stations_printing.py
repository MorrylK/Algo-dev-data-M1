"""
All stations printing
"""
from appmeteo.data_extractor.api_stations import APIStations
from appmeteo.printing.batch_stations_printing import BatchStationsPrinting


class AllStationsPrinting(BatchStationsPrinting, APIStations):
    """
    Classe d'extraction et d'affichage de toutes les stations
    """
    def __init__(self) -> None:
        self.print(self.extract())
