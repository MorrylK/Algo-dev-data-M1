"""
JSON Extractor
"""
import json
import os
from appmeteo.data_extractor.idata_extractor import IDataExtractor


class JSONExtractor(IDataExtractor):
    """
    Classe pour extraire les données à partir d'un fichier JSON
    """
    @staticmethod
    def extract(filename: str):
        path = os.path.normpath(os.path.join(os.path.dirname(__file__), "../"+filename))
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
