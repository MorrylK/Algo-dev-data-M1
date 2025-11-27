from appmeteo.MainObjects.Operate import Operate
from appmeteo.Printing.AllStationsPrinting import AllStationsPrinting


if __name__ == "__main__":
    print("******* TOULOUSE METEO *******\n")
    print("\nMenu de sélection :")
    print("1 -> Afficher les derniers relevés dans toutes les stations")
    print("2 -> Afficher les derniers relevés dans les stations de Compans Cafarelli, Mons station épuration et Colomiers ZI Enjacca")
    print("3 -> Sélectionner une station à afficher (pas encore fonctionnel)")
    c = None
    while c is None:
        try:
            c = int(input("\nChoix: "))
        except:
            print("Mauvaise entrée. Veuillez réessayer.")
            c = None
        if c == 1:
            AllStationsPrinting()
        elif c == 2:
            Operate()
        else:
            print("Choix inconnu.")
            c = None