import pytest
from appmeteo.data_extractor.api_station_extractor import APIStationExtractor

def test_extract():
    df = APIStationExtractor.extract("42-station-meteo-toulouse-parc-compans-cafarelli")
    assert isinstance(df, dict)