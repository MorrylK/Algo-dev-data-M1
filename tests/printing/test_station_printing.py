import pytest
from appmeteo.main_objects.station import Station
from appmeteo.printing.station_printing import StationPrintingDecorator


def test_station_printing(mocker):
    mock_extract = mocker.patch(
        "appmeteo.printing.station_printing.APIStationExtractor.extract",
        return_value={
            'total_count': 171581,
            'results': [{
                'data': '544c75af99d8000080004800',
                'id': 42,
                'humidite': 59,
                'pression': 90000,
                'temperature_en_degre_c': 12.6,
                'heure_de_paris' : '2026-02-12T11:00:00+00:00'
            }]
        }
    )
    mock_record_printing = mocker.patch(
        "appmeteo.printing.station_printing.RecordPrinting.print"
    )
    StationPrintingDecorator(Station("Test 1", 1, "test1")).print()
    mock_record_printing.assert_called_once()
    called_args = mock_record_printing.call_args[0]
    record_arg = called_args[0]
    assert record_arg.temperature == 12.6
    assert record_arg.humidite == 59
    assert record_arg.pression == 90000
    assert record_arg.heure == "2026-02-12T11:00:00+00:00"
    assert record_arg.station.nom == "Test 1"
    assert record_arg.station.capteur == 1
    assert record_arg.station.api_label == "test1"