

from appmeteo.printing.iprinting import IPrinting
from appmeteo.printing.station_printing import StationPrinting
from appmeteo.main_objects.record import Record
from appmeteo.main_objects.station import Station


class BatchStationsPrinting(IPrinting):
    @staticmethod
    def print(stations: list[Station]):
        for i in range(stations.shape[0]):
            station = stations.iloc[i]
            print(station['id_nom'][26:].center(60, "-"))
            stat = Station(station['id_nom'][11:], station['id_numero'], station['id_nom'])
            StationPrinting.print(stat)