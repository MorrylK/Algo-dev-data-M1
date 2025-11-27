

from appmeteo.Printing.IPrinting import IPrinting
from appmeteo.Printing.StationPrinting import StationPrinting
from appmeteo.MainObjects.Record import Record
from appmeteo.MainObjects.Station import Station


class BatchStationsPrinting(IPrinting):
    @staticmethod
    def print(stations: list[Station]):
        for i in range(stations.shape[0]):
            station = stations.iloc[i]
            print(station['id_nom'][26:].center(60, "-"))
            stat = Station(station['id_nom'][11:], station['id_numero'], station['id_nom'])
            StationPrinting.print(stat)