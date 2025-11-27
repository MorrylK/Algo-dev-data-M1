from appmeteo.data_extractor.record_extractor import RecordExtractor
from appmeteo.test.test import Test
import pandas as pd


class TestMissing(Test):
    @staticmethod
    def test(line) -> None:
        record = RecordExtractor.extract(line)
        fields = ["temperature", "humidite", "pression", "heure", "station"]
        #passed = True
        for field in fields:
            valeur = getattr(record, field)
            #assert pd.notnull(valeur), f"Le champ {field} est nul dans la ligne extraite!"
            if (not pd.notnull(valeur)):
                #print(f"Le champ {field} est nul dans la ligne!")
                #passed = False
                return False
        #if not passed:
        #    print(f"Test échoué : ligne {i+2}.")
        return True