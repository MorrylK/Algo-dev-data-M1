from appmeteo.data_extractor.api_stations import APIStations
from appmeteo.printing.batch_stations_printing import BatchStationsPrinting


class AllStationsPrinting(BatchStationsPrinting, APIStations):
    def __init__(self) -> None:
        self.print(self.extract())