
from appmeteo.main_objects.station import Station


class Queue:
    """
    Classe définissant une file de stations.
    """
    def __init__(self) -> None:
        self.queue:[Station] = []
    
    def add(self, station):
        self.queue.append(Station(station["name"], station["capteur"], station["api_label"]))
    
    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None