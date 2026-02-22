import pytest
from appmeteo.data_structure.queue import Queue

@pytest.fixture
def queue():
    return Queue([{"name":"Test 1", "capteur":"1", "api_label":"test1"}])

def test_queue_add(queue):
    queue.add({"name":"Test 2", "capteur":"2", "api_label":"test2"})
    assert len(queue.queue) == 2
    assert queue.queue[0].api_label == "test1"
    assert queue.queue[1].api_label == "test2"

def test_queue_get(queue):
    assert queue.get().api_label == "test1"
    queue.add({"name":"Test 2", "capteur":"2", "api_label":"test2"})
    assert queue.get().api_label == "test2"
    assert queue.get() == None