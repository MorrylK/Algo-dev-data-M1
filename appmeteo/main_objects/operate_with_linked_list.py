from appmeteo.data_structure.linked_list import LinkedList
from appmeteo.main_objects.config_data import ConfigData
from appmeteo.printing.station_printing import StationPrinting


class OperateWithLinkedList:
    def __init__(self) -> None:
        print(f"Nous allons afficher la météo dans quelques stations.")

        config = ConfigData.get()
        station = LinkedList(config['stations']).tete
        while station is not None:
            print("\n[Cliquez sur Entrée pour continuer]\n")
            input()
            print(station.nom.center(60, "-"))
            StationPrinting.print(station)
            station = station.next