## The basic idea comes from the divide-and-conquer strategy, which is to break down a problem into smaller subproblems,
#  solve each subproblem independently, and then combine the results to solve the original problem.
# In the case of merge sort, we divide the list into two halves, recursively sort each half,
# and then merge the sorted halves back together.

from chapter2.Array import *


def identity(x):
    return x


class MergeSort(object):
    def __init__(self, unordered, key=identity):
        self.__arr = unordered
        self.__key = key
        n = len(unordered)
        self.__work = Array(n)
        for i in range(n):
            self.__work.insert(None)
        self.mergesort(0, n)

    def mergesort(self, lo, hi):
        if lo + 1 >= hi:
            return
        mid = (lo + hi) // 2
        self.mergesort(lo, mid)
        self.mergesort(mid, hi)
        self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):
        n = 0
        idxLo = lo
        idxHi = mid
        while idxLo < mid and idxHi < hi:
            itemLo = self.__arr.get(idxLo)
            itemHi = self.__arr.get(idxHi)

            if self.__key(itemLo) <= self.__key(itemHi):
                self.__work.set(n, itemLo)
                idxLo += 1
            else:
                self.__work.set(n, itemHi)
                idxHi += 1
            n += 1

        while idxLo < mid:
            self.__work.set(n, self.__arr.get(idxLo))
            idxLo += 1
            n += 1
            ## No need to copy the second half since they are already in place because the input array
            ## is being sorted in place and the second half is already sorted.
            # The merge process only needs to copy the first half into the work array and then copy back
            # the merged result into the original array.

        while n > 0:
            n -= 1
            self.__arr.set(lo + n, self.__work.get(n))
