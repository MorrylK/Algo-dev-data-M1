"""
Linked List
"""
from appmeteo.data_structure.datatructure import DataStructure
from appmeteo.data_structure.linked_station import LinkedStation


class LinkedList(DataStructure):
    """
    Linked List
    """
    def __init__(self, stations) -> None:
        self.tete:LinkedStation = None
        self.queue:LinkedStation = None
        for station in stations:
            self.add(station)

    def add(self, station:LinkedStation):
        """
        Adds a linked station to the linked list
        """
        if self.tete is None:
            self.tete = LinkedStation(station["name"], station["capteur"], station["api_label"])
            self.queue = self.tete
        else:
            new_stat = LinkedStation(station["name"], station["capteur"], station["api_label"])
            self.queue.next_station = new_stat
            self.queue = new_stat
