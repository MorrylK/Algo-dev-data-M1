from appmeteo.DataStructure.DataStructure import DataStructure
from appmeteo.DataStructure.LinkedStation import LinkedStation


class LinkedList(DataStructure):
    def __init__(self, stations) -> None:
        self.tete:LinkedStation = None
        self.queue:LinkedStation = None
        for station in stations:
            self.add(station)
    
    def add(self, station:LinkedStation):
        if self.tete == None:
            self.tete = LinkedStation(station["name"], station["capteur"], station["api_label"])
            self.queue = self.tete
        else:
            new_stat = LinkedStation(station["name"], station["capteur"], station["api_label"])
            self.queue.next = new_stat
            self.queue = new_stat
    
    def remove(self, data):
        maillon_prec = None
        maillon = self.tete
        while maillon.data != data and maillon.next != None:
            maillon_prec = maillon
            maillon = maillon.get_next()
        if maillon.data == data:
            maillon_prec.set_next(maillon.get_next())
        else:
            print("Élément à supprimer non trouvé.")
    
    def search(self, data):
        maillon = self.tete
        while maillon.data != data:
            maillon = maillon.get_next()
        if maillon.data == data:
            return maillon
        else:
            print("Élément non trouvé.")
    
    def print(self, stations):
        for station in stations:
            print(f"Data: {station.data} - Suivant: {station.next.data if station.next != None else "-"}")
