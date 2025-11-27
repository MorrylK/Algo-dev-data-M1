from appmeteo.DataExtractor.IDataExtractor import IDataExtractor


class IAPIDataExtractor(IDataExtractor):
    @staticmethod
    def extract(route: str):
        raise NotImplementedError("This function must be implemented.")