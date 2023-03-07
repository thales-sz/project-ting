from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        self._queue.pop()

    def search(self, index):
        if index in range(self.__len__()):
            return self._queue[index]
        else:
            raise IndexError
