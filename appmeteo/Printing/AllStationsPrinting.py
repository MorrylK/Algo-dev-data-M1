from appmeteo.DataExtractor.APIStations import APIStations
from appmeteo.Printing.BatchStationsPrinting import BatchStationsPrinting


class AllStationsPrinting(BatchStationsPrinting, APIStations):
    def __init__(self) -> None:
        self.print(self.extract())