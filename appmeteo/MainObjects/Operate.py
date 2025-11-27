from appmeteo.DataStructure.LinkedList import LinkedList
from appmeteo.Printing.StationPrinting import StationPrinting
import json
import os

class Operate:
    def __init__(self) -> None:
        print(f"Nous allons afficher la météo dans quelques stations.")

        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)

        station = LinkedList(config['stations']).tete
        while station is not None:
            print("\n[Cliquez sur Entrée pour continuer]\n")
            input()
            print(station.nom.center(60, "-"))
            StationPrinting.print(station)
            station = station.next