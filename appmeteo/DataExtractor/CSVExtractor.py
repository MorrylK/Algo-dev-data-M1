from appmeteo.DataExtractor.IDataExtractor import IDataExtractor
import pandas as pd

class CSVExtractor(IDataExtractor):
    @staticmethod
    def extract(filename: str):
        return pd.read_csv(filename, sep=";")