from appmeteo.MainObjects.Station import Station


class LinkedStation(Station):
    def __init__(self, nom: str, capteur: int, api_label: str, next=None) -> None:
        super().__init__(nom, capteur, api_label)
        self.next:LinkedStation = None