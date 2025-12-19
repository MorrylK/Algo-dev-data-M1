from appmeteo.data_structure.queue import Queue
from appmeteo.main_objects.config_data import ConfigData
from appmeteo.printing.station_printing import StationPrintingDecorator

class OperateWithQueue:
    def __init__(self) -> None:
        print(f"Nous allons afficher la météo dans quelques stations.")

        config = ConfigData().get()
        queue = Queue()
        for station in config['stations']:
            queue.add(station)

        station = queue.get()

        while station is not None:
            print("\n[Appuyez sur Entrée pour continuer]\n")
            input()
            print(station.nom.center(60, "-"))
            StationPrintingDecorator(station).print()
            station = queue.get()
            
        