class Link(object):
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def is_last(self):
        return self.__next is None

    def getData(self):
        return self.__data

    def setData(self, datum):
        self.__data = datum

    def getNext(self):
        return self.__next

    def setNext(self, link):
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception("Next linki must be a link object or None")

    def __str__(self):
        return str(self.getData())


class LinkedList(object):
    def __init__(self):
        self.__first = None

    def getFirst(self):
        return self.__first

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            raise Exception("First link must be a link object or None")

    def getNext(self):
        if self.__first is not None:
            return self.__first.getNext()
        else:
            return None

    def setNext(self, link):
        """Synonym of setFirst() to facilitate list manipulations  in which
        either the __first pointer of the list or the __next pointer of a
        link object is updated depending on the context.
        """
        print("setNext called", "link:", link)
        self.setFirst(link)

    def isEmpty(self):
        return self.getFirst() is None

    def first(self):
        if self.__first is not None:
            return self.getFirst().getData()
        else:
            raise Exception("List is empty")

    def traverse(self, func=print):
        link = self.getFirst()
        while link is not None:
            func(link.getData())
            link = link.getNext()

    def __len__(self):
        length = 0
        link = self.getFirst()
        while link is not None:
            length += 1
            link = link.getNext()
        return length

    def __str__(self):
        result = "["
        link = self.getFirst()
        while link is not None:
            if len(result) > 1:
                result += "->"
            result += str(link)
            link = link.getNext()
        return result + "]"

    def insert(self, datum):
        """Inserts at the front of the list"""
        link = Link(datum, self.getFirst())
        self.setFirst(link)

    def find(self, goal, key=lambda x: x):
        link = self.getFirst()
        while link is not None:
            if key(link.getData()) == goal:
                return link
            link = link.getNext()
        return None

    def search(self, goal, key=lambda x: x):
        link = self.find(goal, key)
        if link is not None:
            return link.getData()

    def insertAfter(self, goal, datum, key=lambda x: x):
        link = self.find(goal, key)
        if link is not None:
            newLink = Link(datum, link.getNext())
            link.setNext(newLink)
            return True
        else:
            return False

    def deleteFirst(self):
        if not self.isEmpty():
            first = self.getFirst()
            self.setFirst(first.getNext())
            return first.getData()
        else:
            raise Exception("Cannot delete from empty list")

    def delete(self, goal, key=lambda x: x):
        if self.isEmpty():
            raise Exception("cannot Delete from an empty linked list")

        elif goal == key(self.getFirst().getData()):
            self.deleteFirst()

        else:
            previous = self
            while previous.getNext() is not None:
                link = previous.getNext()
                if goal == key(link.getData()):
                    previous.setNext(link.getNext())
                    return link.getData()
                previous = link
            raise Exception("No item with matching key found in list")

    class __ListIterator(object):
        def __init__(self, llist):
            self._llist = llist
            self._next = llist.getNext()

        def next(self):
            if self._next is None:
                raise StopIteration
            else:
                item = self._next.getData()
                self._next = self._next.getNext()
                return item

        def has_more(self):
            return self._next is not None

    def iterator(self):
        return LinkedList.__ListIterator(self)

    ##using a generator to iterate through the linked list
    def __iter__(self):
        next = self.getFirst()
        while next is not None:
            yield next.getData()
            next = next.getNext()
