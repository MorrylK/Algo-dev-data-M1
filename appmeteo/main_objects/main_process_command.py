
from appmeteo.data_extractor.api_stations import APIStations
from appmeteo.main_objects.operate_with_linked_list import OperateWithLinkedList
from appmeteo.main_objects.operate_with_queue import OperateWithQueue
from appmeteo.printing.all_stations_printing import AllStationsPrinting
from InquirerPy import inquirer

from appmeteo.printing.batch_stations_printing import BatchStationsPrinting


class Command():
    def execute(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")


class TitlePrintingCommand(Command):
    def execute(self) -> None:
        print("\n******* TOULOUSE METEO *******\n")


class AllStationsPrintingCommand(Command):
    def execute(self) -> None:
        AllStationsPrinting()


class LinkedStationsPrintingCommand(Command):
    def execute(self) -> None:
        OperateWithLinkedList()


class QueueStationsPrintingCommand(Command):
    def execute(self) -> None:
        OperateWithQueue()


class SelectStationCommand(Command):
    def execute(self) -> None:
        choice = inquirer.select(
            message="Menu de stations :",
            choices=[
                ("Afficher les derniers relevés de toutes les stations", "1"),
                ("Afficher les derniers relevés de stations spécifiques", "2"),
                ("Afficher les derniers relevés des stations : Compans Cafarelli, Mons station épuration et Colomiers ZI Enjacca (par une liste chaînée)", "3"),
                ("Afficher les derniers relevés des stations précédentes (par une file).", "4")
            ]
        ).execute()
        return choice[1]


class SelectSpecificStationCommand(Command):
    def execute(self) -> None:
        stations = APIStations().extract()
        print(stations)
        selected_station_ids = inquirer.checkbox(
            message="Sélection de stations spécifiques (sélection avec [Espace] et validation avec [Entrée]) :",
            choices=stations["id_nom"]
        ).execute()
        selected_stations = stations[stations['id_nom'].isin(selected_station_ids)]
        BatchStationsPrinting.print(selected_stations)


class MainProcessCommand:
    def __init__(self) -> None:
        self.commands = {
            "title": TitlePrintingCommand(),
            "C0": SelectStationCommand(),
            "C1": AllStationsPrintingCommand(),
            "C2": SelectSpecificStationCommand(),
            "C3": LinkedStationsPrintingCommand(),
            "C4": QueueStationsPrintingCommand(),
        }

    def process(self) -> None:
        """
        choice = None
        while choice is None:
            self.commands["title"].execute()
            choice = self.commands["C0"].execute()
            if choice not in ["1", "2", "3"]:
                print("\n\tMauvaise entrée. Veuillez réessayer.")
                choice = None
        self.commands["C" + choice].execute()
        """

        self.commands["title"].execute()
        restart = True
        while restart:
            choice = self.commands["C0"].execute()
            self.commands["C" + choice].execute()
            restart = inquirer.confirm("Nouvelle opération ?", default=True).execute()

