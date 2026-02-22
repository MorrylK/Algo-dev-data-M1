import pytest
from appmeteo.main_objects.config_data import ConfigData

def test_get_config_data():
    assert ConfigData().get()['stations'] == [
            {
                "capteur": "42",
                "name": "Compans Cafarelli",
                "api_label": "42-station-meteo-toulouse-parc-compans-cafarelli"
            },
            {
                "capteur": "31",
                "name": "Mons station épuration",
                "api_label": "31-station-meteo-mons-station-epuration"
            },
            {
                "capteur": "24",
                "name": "Colomiers ZI Enjacca",
                "api_label": "24-station-meteo-colomiers-zi-enjacca"
            }
        ]