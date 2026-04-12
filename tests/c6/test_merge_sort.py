from chapter6.MergeSort import MergeSort
from chapter2.Array import Array


class TestMergeSort:
    def test_merge_sort(self):
        lst = [5, 2, 9, 1, 5, 6]
        array = Array(len(lst))
        for item in lst:
            array.insert(item)
        MergeSort(array)
        assert array.asList() == [1, 2, 5, 5, 6, 9]
