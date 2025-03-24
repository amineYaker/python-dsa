
class Array(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0
    
    def __len__(self):
        return self.__nItems
    
    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]
    
    def set(self, n , value):
        if 0 <= n and  n < self.__nItems:
            self.__a[n] = value
    
    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1
    
    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        return -1
    
    def search(self, item):
        return self.get(self.find(item))
    
    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k + 1]
                return True
        return False

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def bubbleSort(self): # Sort comparing adjacent vals and bubble up
        for last in range(self.__nItems - 1, 0, -1): 
            for inner in range(last):
                if self.__a[inner] > self.__a[inner + 1]:
                    self.swap(inner, inner + 1)
        # Complexity: O(n²)
        # invariant: elemnts right to last are always sorted (accumulates to the right)

    def selectionSort(self):                   # sort by selecting min
        for outer in range(self.__nItems - 1): # and swapping min to leftmost
            min = outer                        # assume min is the leftmost
            for inner in range(outer + 1, self.__nItems):
                if self.__a[inner] < self.__a[min]:
                    min = inner
            self.swap(outer, min) # swap leftmost and min
            # Complexity O(n²) however it is faster than bubleSort because there are O(n) swaps insteand of O(n²)
            # invariant: array elements with indices less than **outer** are always sorted (accumulates to the left)

    def insertionSort(self): # sorts by repeated inserts
        for outer in range(1, self.__nItems): # mark one element
            temp = self.__a[outer] # store marked elem in temp
            inner = outer # inner loop starts and mark
            while inner > 0 and temp < self.__a[inner -1]: # Marked elem is smaller so we shift to the right
                self.__a[inner] = self.__a[inner - 1]
                inner -= 1
            self.__a[inner] = temp # marked elem is no longer smaller we put it in the "hole"
        # invariant data items with indices smaller than outer are partially sorted
        # complexity O(n²) but for random data it is twice as fast as the bubble sort and faster than selection sort
        # for Data that is almost sorted it runs at almost O(n)
        # for data arranged in reversed order it is worse than the bubble sort

                
    def swap(self, idx1, idx2):
        if (0 <= idx1 and idx1 < self.__nItems and 0 <= idx2 and idx2 < self.__nItems):
            self.__a[idx1], self.__a[idx2] = self.__a[idx2], self.__a[idx1]

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans+="]"
        return ans