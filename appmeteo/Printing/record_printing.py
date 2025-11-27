

from appmeteo.printing.iprinting import IPrinting
from appmeteo.main_objects.record import Record


class RecordPrinting(IPrinting):
    @staticmethod
    def print(record: Record):
        print(f"{record.heure}\nTempérature : {record.temperature} ; Humidité : {record.humidite} ; Pression : {record.pression}")
