from appmeteo.data_extractor.idata_extractor import IDataExtractor
import json
import os


class JSONExtractor(IDataExtractor):
    @staticmethod
    def extract(filename: str):
        path = os.path.normpath(os.path.join(os.path.dirname(__file__), "../"+filename))
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data