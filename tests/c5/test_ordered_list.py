from chapter5.OrderedList import OrderedList


class TestOrderedList:
    def test_ordered_insertion(self):
        ordered_list = OrderedList()
        ordered_list.insert(30)
        ordered_list.insert(10)
        assert str(ordered_list) == "[10->30]"
        assert len(ordered_list) == 2
