class ConfigData:
    """
    Classe singleton pour la configuration des données.
    """
    __instance = None

    def __new__(cls) -> None:
        if ConfigData.__instance is None:
            ConfigData.__instance = super(ConfigData, cls).__new__(cls)
            ConfigData.__instance._config = {}
        return ConfigData.__instance
    
    def __init__(self) -> None:
        self.stations = [
            {
                "capteur": "42",
                "name": "Compans Cafarelli",
                "api_label": "42-station-meteo-toulouse-parc-compans-cafarelli"
            },
            {
                "capteur": "31",
                "name": "Mons station épuration",
                "api_label": "31-station-meteo-mons-station-epuration"
            },
            {
                "capteur": "24",
                "name": "Colomiers ZI Enjacca",
                "api_label": "24-station-meteo-colomiers-zi-enjacca"
            }
        ]
    
    def get(self):
        return {
            "stations": self.stations
        }