from appmeteo.main_objects.operate_with_linked_list import OperateWithLinkedList
from appmeteo.main_objects.operate_with_queue import OperateWithQueue
from appmeteo.printing.all_stations_printing import AllStationsPrinting


if __name__ == "__main__":
    print("\n******* TOULOUSE METEO *******\n")
    print("\nMenu de sélection :")
    print("1 -> Afficher les derniers relevés dans toutes les stations")
    print("2 -> Afficher les derniers relevés dans les stations de Compans Cafarelli, Mons station épuration et Colomiers ZI Enjacca (par une liste chaînée)")
    print("3 -> Afficher les derniers relevés des stations précédentes (par une file).")
    print("4 -> Sélectionner une station à afficher (pas encore fonctionnel)")
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
            OperateWithLinkedList()
        elif c == 3:
            OperateWithQueue()
        else:
            print("Choix inconnu.")
            c = None