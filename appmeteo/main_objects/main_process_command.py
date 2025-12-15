
from appmeteo.main_objects.operate_with_linked_list import OperateWithLinkedList
from appmeteo.main_objects.operate_with_queue import OperateWithQueue
from appmeteo.printing.all_stations_printing import AllStationsPrinting


class Command():
    def execute(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")


class TitlePrintingCommand(Command):
    def execute(self) -> None:
        print("\n******* TOULOUSE METEO *******\n")


class AllStationsPrintingCommand(Command):
    def execute(self) -> None:
        AllStationsPrinting().print()


class LinkedStationsPrintingCommand(Command):
    def execute(self) -> None:
        OperateWithLinkedList().print()


class QueueStationsPrintingCommand(Command):
    def execute(self) -> None:
        OperateWithQueue().print()


class SelectStationCommand(Command):
    def execute(self) -> None:
        print("Menu de sélection :")
        print("1 -> Afficher les derniers relevés dans toutes les stations")
        print("2 -> Afficher les derniers relevés dans les stations de Compans Cafarelli, Mons station épuration et Colomiers ZI Enjacca (par une liste chaînée)")
        print("3 -> Afficher les derniers relevés des stations précédentes (par une file).")
        print("4 -> Sélectionner une station à afficher (pas encore fonctionnel)")
        choice = input("Choix: ")
        return choice


class MainProcessCommand:
    def __init__(self) -> None:
        self.commands = {
            "title": TitlePrintingCommand(),
            "C0": SelectStationCommand(),
            "C1": AllStationsPrintingCommand(),
            "C2": LinkedStationsPrintingCommand(),
            "C3": QueueStationsPrintingCommand(),
        }

    def process(self) -> None:
        choice = None
        while choice is None:
            self.commands["title"].execute()
            choice = self.commands["C0"].execute()
            if choice not in ["1", "2", "3"]:
                print("\n\tMauvaise entrée. Veuillez réessayer.")
                choice = None
        self.commands["C" + choice].execute()

