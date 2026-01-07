from chapter5.LinkQueue import Queue


class TestLinkQueue:
    def test_queue(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        assert len(queue) == 2
        assert queue.peek() == 10
        assert queue.dequeue() == 10
        assert len(queue) == 1
        assert queue.dequeue() == 20
        assert queue.isEmpty()
