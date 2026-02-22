"""
Linked Station
"""
from appmeteo.main_objects.station import Station


class LinkedStation(Station):
    """
    classe Décorateur sur Station
    """
    def __init__(self, nom: str, capteur: int, api_label: str) -> None:
        super().__init__(nom, capteur, api_label)
        self.next_station:LinkedStation = None
