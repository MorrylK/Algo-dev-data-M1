from appmeteo.data_extractor.idata_extractor import IDataExtractor
import pandas as pd

class CSVExtractor(IDataExtractor):
    @staticmethod
    def extract(filename: str):
        return pd.read_csv(filename, sep=";")