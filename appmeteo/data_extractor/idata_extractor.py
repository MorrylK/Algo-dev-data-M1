"""
Interface Data Extractor
"""

class IDataExtractor:
    """
    Interface d'extraction des données
    """
    @staticmethod
    def extract() -> dict:
        raise NotImplementedError("This function must be implemented.")
