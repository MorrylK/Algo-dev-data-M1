"""
Interface Printing
"""
class IPrinting:
    """
    Interface pour l'affichage d'objets
    """
    @staticmethod
    def print() -> None:
        raise NotImplementedError("This function must be implemented")
