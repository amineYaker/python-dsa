from chapter6.MergeSort import MergeSort
from chapter2.Array import Array
from chapter3.SortArray import SortArray
import random

## This test uses the pytest-benchmark plugin to benchmark the performance of the MergeSort algorithm and
# compare it with bubble sort and insertion sort. The benchmark function is provided by the pytest-benchmark plugin
# and allows us to measure the execution time of a specific function or code block.

## Big O notation for MergeSort is O(n log n)
# While bubble sort, selection sort and insertion sort have a time complexity of O(n²) in the worst case,
#  merge sort has a time complexity of O(n log n) in all cases (best, average, and worst).
# This is because merge sort divides the list into halves log n times and processes each element n times during the merge step.
# In contrast, bubble sort and insertion sort require n comparisons
# and potentially n swaps for each of the n elements, leading to O(n²) time complexity.

# Therefore, merge sort is generally more efficient than bubble sort, selection sort, and insertion sort,
# especially for larger datasets.
## However, for small datasets, the overhead of the recursive calls and merging in merge sort may make it slower
# than simpler algorithms like insertion sort which this benchmark will help to demonstrate.
# in practice the constant factors for insertion sort are smaller than those for merge sort, so for small arrays
# insertion sort can be faster than merge sort.


def initArray(size=100000, maxValue=1000, seed=3.14591, array_class=Array):
    """Create an Array of specified size with a fixed sequence or 'random' elements"""

    if array_class is SortArray:
        arr = SortArray(size)
    elif array_class is Array:
        arr = Array(size)
    random.seed(seed)

    for i in range(size):
        arr.insert(random.randrange(maxValue))
    return arr


def test_benchmark(benchmark):
    array = initArray(array_class=Array)
    benchmark(MergeSort, array)


def test_benchmark_bubble(benchmark):
    array = initArray(array_class=SortArray)
    benchmark(SortArray.bubbleSort, array)


def test_benchmark_insertion(benchmark):
    array = initArray(array_class=SortArray)
    benchmark(SortArray.insertionSort, array)


def test_benchmark_selection(benchmark):
    array = initArray(array_class=SortArray)
    benchmark(SortArray.selectionSort, array)
