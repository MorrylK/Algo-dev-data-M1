"""
Interface Data Extractor
"""

class IDataExtractor:
    """
    Interface d'extraction des données
    """
    @staticmethod
    def extract() -> dict:
        """
        Méthode d'extraction des données
        """
        raise NotImplementedError("This function must be implemented.")
