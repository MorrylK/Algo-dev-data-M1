"""
API Data Extractor
"""
from appmeteo.data_extractor.idata_extractor import IDataExtractor


class IAPIDataExtractor(IDataExtractor):
    """
    Interface d'extraction des données
    """
    @staticmethod
    def extract(route: str):
        raise NotImplementedError("This function must be implemented.")