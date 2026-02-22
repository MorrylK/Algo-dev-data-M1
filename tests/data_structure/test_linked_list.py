import pytest
from appmeteo.data_structure.linked_list import LinkedList

@pytest.fixture
def linked_list():
    return LinkedList([{"name": "Test 1", "capteur": "1", "api_label": "test1"}, {"name": "Test 2", "capteur": "2", "api_label": "test2"}])

def test_linked_list_add(linked_list):
    linked_list.add({"name": "Test 3", "capteur": "3", "api_label": "test3"})
    assert linked_list.tete.api_label == "test1"
    assert linked_list.queue.api_label == "test3"
    assert linked_list.tete.next_station.api_label == "test2"
    assert linked_list.queue.next_station is None
