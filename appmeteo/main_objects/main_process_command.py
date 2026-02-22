"""
Main Process
"""
from InquirerPy import inquirer
from appmeteo.data_extractor.api_stations import APIStations
from appmeteo.main_objects.operate_with_linked_list import OperateWithLinkedList
from appmeteo.main_objects.operate_with_queue import OperateWithQueue
from appmeteo.printing.all_stations_printing import AllStationsPrinting
from appmeteo.printing.batch_stations_printing import BatchStationsPrinting


class Command():
    """
    Classe abstraite des commandes
    """
    def execute(self) -> None:
        """
        Commande à exécuter
        """
        raise NotImplementedError("Subclasses must implement this method")


class TitlePrintingCommand(Command):
    """
    Commande pour afficher le titre.
    """
    def execute(self) -> None:
        """
        Affiche le titre de l'application.
        """
        print("\n******* TOULOUSE METEO *******\n")


class AllStationsPrintingCommand(Command):
    """
    Commande pour afficher toutes les stations.
    """
    def execute(self) -> None:
        """
        Lance l'affichage de toutes les stations.
        """
        AllStationsPrinting()


class LinkedStationsPrintingCommand(Command):
    """
    Commande pour le parcours par liste chaînée.
    """
    def execute(self) -> None:
        """
        Lance la démonstration de la liste chaînée.
        """
        OperateWithLinkedList()


class QueueStationsPrintingCommand(Command):
    """
    Commande pour le parcours par file.
    """
    def execute(self) -> None:
        """
        Lance la démonstration de la file.
        """
        OperateWithQueue()


class SelectMenuCommand(Command):
    """
    Commande pour afficher le menu principal.
    """
    def execute(self) -> None:
        """
        Affiche le menu et retourne le choix utilisateur.
        """
        choice = inquirer.select(
            message="Menu de stations :",
            choices=[
                ("Afficher les derniers relevés de toutes les stations", "1"),
                ("Afficher les derniers relevés de stations spécifiques", "2"),
                ("Afficher les derniers relevés des stations : Compans Cafarelli, "+
                    "Mons station épuration et Colomiers ZI Enjacca (par une liste chaînée)", "3"),
                ("Afficher les derniers relevés des stations précédentes (par une file).", "4")
            ]
        ).execute()
        return choice[1]


class SelectSpecificStationCommand(Command):
    """
    Commande pour sélectionner et afficher des stations spécifiques.
    """
    def execute(self) -> None:
        """
        Permet la sélection et l'affichage de stations.
        """
        stations = APIStations().extract()
        print(stations)
        selected_station_ids = inquirer.checkbox(
            message="Sélection de stations spécifiques "+
                "(sélection avec [Espace] et validation avec [Entrée]) :",
            choices=stations["id_nom"]
        ).execute()
        selected_stations = stations[stations['id_nom'].isin(selected_station_ids)]
        BatchStationsPrinting.print(selected_stations)


class MainProcessCommand:
    """
    Processus principal de l'application.
    """
    def __init__(self) -> None:
        """
        Initialise les commandes disponibles.
        """
        self.commands = {
            "title": TitlePrintingCommand(),
            "C0": SelectMenuCommand(),
            "C1": AllStationsPrintingCommand(),
            "C2": SelectSpecificStationCommand(),
            "C3": LinkedStationsPrintingCommand(),
            "C4": QueueStationsPrintingCommand(),
        }

    def process(self) -> None:
        """
        Point d'entrée de l'application
        """
        self.commands["title"].execute()
        restart = True
        while restart:
            choice = self.commands["C0"].execute()
            self.commands["C" + choice].execute()
            restart = inquirer.confirm("Nouvelle opération ?", default=True).execute()
