"""
Batch stations printing
"""
from appmeteo.printing.iprinting import IPrinting
from appmeteo.printing.station_printing import StationPrintingDecorator
from appmeteo.main_objects.station import Station


class BatchStationsPrinting(IPrinting):
    """
    Classe permettant l'affichage de plusieurs stations.
    """
    @staticmethod
    def print(stations: list[Station]):
        for i in range(stations.shape[0]):
            station = stations.iloc[i]
            print(station['id_nom'][26:].center(60, "-"))
            stat = Station(station['id_nom'][11:], station['id_numero'], station['id_nom'])
            StationPrintingDecorator(stat).print()
