import pytest
from appmeteo.data_extractor.record_extractor import RecordExtractor

def test_record_rextract():
    record = RecordExtractor.extract({
        "temperature": "t",
        "humidite": "h",
        "pression": "p",
        "heure_de_paris": "hp",
        "id": "0"
    })
    assert record.temperature == "t"
    assert record.humidite == "h"
    assert record.pression == "p"
    assert record.heure == "hp"
    assert record.station == "0"