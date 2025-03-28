from SortArray import *
import random
import timeit

def initArray(size=100, maxValue=100, seed=3.1459):
    """Create an Array of specified size with a fixed sequence or 'random' elements"""

    arr = Array(size)
    random.seed(seed)

    for i in range(size):
        arr.insert(random.randrange(maxValue))
    return arr

arr = initArray()

print("Array containing", len(arr), "items:\n", arr)

for test in ['initArray().bubbleSort()', 'initArray().selectionSort()', "initArray().insertionSort()"]:
    elapsed = timeit.timeit(test, number=100, globals= globals())
    print(test, "took", elapsed, "seconds", flush=True)

arr.insertionSort()
print('Sorted array contains:\n', arr)