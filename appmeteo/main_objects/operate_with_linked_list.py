"""
Operate with Linked List
"""
from appmeteo.data_structure.linked_list import LinkedList
from appmeteo.main_objects.config_data import ConfigData
from appmeteo.printing.station_printing import StationPrintingDecorator


class OperateWithLinkedList:
    """
    Classe pour la commande de démonstration du fonctionnement d'une liste chaînée
    """
    def __init__(self) -> None:
        print("Nous allons afficher la météo dans quelques stations.")
        config = ConfigData().get()
        station = LinkedList(config['stations']).tete
        while station is not None:
            print("\n[Appuyez sur Entrée pour continuer]\n")
            input()
            StationPrintingDecorator(station).print()
            station = station.next_station
