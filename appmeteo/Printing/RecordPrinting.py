

from appmeteo.Printing.IPrinting import IPrinting
from appmeteo.MainObjects.Record import Record


class RecordPrinting(IPrinting):
    @staticmethod
    def print(record: Record):
        print(f"{record.heure}\nTempérature : {record.temperature} ; Humidité : {record.humidite} ; Pression : {record.pression}")
