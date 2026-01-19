"""
CSV Exctractor
"""
import pandas as pd
from appmeteo.data_extractor.idata_extractor import IDataExtractor

class CSVExtractor(IDataExtractor):
    """
    Classe pour extraire les données à partir d'un fichier CSV
    """
    @staticmethod
    def extract(filename: str):
        return pd.read_csv(filename, sep=";")