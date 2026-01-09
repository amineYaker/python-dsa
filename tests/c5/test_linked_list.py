from chapter5 import LinkedList as ll


class TestLinkedList:
    def test_insertion(self):
        test_list = ll.LinkedList()
        test_list.insert(10)
        assert test_list.getFirst().getData() == 10

    def test_len(self):
        test_list = ll.LinkedList()
        test_list.insert(10)
        assert len(test_list) == 1

    def test_find(self):
        test_list = ll.LinkedList()
        test_list.insert(10)
        test_list.insert(20)
        assert test_list.find(20).getData() == 20

    def test_deleteFirst(self):
        test_list = ll.LinkedList()
        test_list.insert(10)
        test_list.insert(20)
        assert test_list.deleteFirst() == 20
        assert len(test_list) == 1

    def test_str(self):
        test_list = ll.LinkedList()
        test_list.insert(10)
        test_list.insert(20)
        assert str(test_list) == "[20->10]"

    def test_insertAfter(self):
        test_list = ll.LinkedList()
        test_list.insert(10)
        test_list.insert(20)
        test_list.insertAfter(10, 15)
        assert str(test_list) == "[20->10->15]"

    def test_iteration(self):
        test_list = ll.LinkedList()
        test_list.insert(10)
        test_list.insert(20)
        test_list.insert(30)
        data = [data for data in test_list]
        assert data == [30, 20, 10]
