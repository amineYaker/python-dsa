## using an ordered array  O(n) insertion & removal

def identity(x): return x

class PriorityQueue(object):
    def __init__(self, size, pri= identity):
        self.__maxSize = size
        self.__que = [None] * size
        self.__pri =pri
        self.__nItems = 0

    def insert(self, item) :
        if self.isFull():
            raise Exception("Queue Overflow")
        j = self.__nItems - 1

        while j >= 0 and (self.__pri(item) >= self.__pri(self.__que[j])):
            self.__que[j +1] = self.__que[j]
            j -= 1
        
        self.__que[j + 1] = item
        self.__nItems += 1
        return True
    
    def remove(self):
        if self.isEmpty():
            raise Exception("Queue undeflow")
        
        self.__nItems -=1
        front = self.__que[self.__nItems]
        self.__que[self.__nItems] = None
        return front
    
    def peek(self):
        return None if self.isEmpty() else self.__que[self.__nItems -1]

    def isFull(self): return self.__nItems == self.__maxSize
   
    def isEmpty(self): return self.__nItems == 0

    def __len__(self): return self.__nItems

    def __str__(self):
        ans = "["
        for i in range(self.__nItems -1, -1, -1):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__que[i])
        ans += "]"
        return ans
