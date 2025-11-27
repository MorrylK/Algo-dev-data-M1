class Station:
    def __init__(self, nom:str, capteur:int, api_label:str) -> None:
        self.nom:str = nom
        self.capteur:int = capteur
        self.api_label:str = api_label