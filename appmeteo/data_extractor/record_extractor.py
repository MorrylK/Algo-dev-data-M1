from appmeteo.main_objects.record import Record


class RecordExtractor:
    @staticmethod
    def extract(data) -> Record:
        temperature = data.get("temperature")
        humidite = data.get("humidite")
        pression = data.get("pression")
        heure = data.get("heure_de_paris")
        station = data.get("id")
        return Record(temperature, humidite, pression, heure, station)