import pytest
import pandas as pd
from appmeteo.data_extractor.api_stations import APIStations

def test_extract():
    df = APIStations.extract()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty