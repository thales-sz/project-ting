from ting_file_management.priority_queue import PriorityQueue
import pytest


MOCK_1 = {"qtd_linhas": 7}
MOCK_2 = {"qtd_linhas": 2}


def test_basic_priority_queueing():
    queue = PriorityQueue()

    queue.enqueue(MOCK_1)
    queue.enqueue(MOCK_2)

    with pytest.raises(IndexError):
        queue.search(89)
    
    assert queue.__len__() == 2