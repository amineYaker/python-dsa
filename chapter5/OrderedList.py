from chapter5.LinkedList import LinkedList, Link


class OrderedList(LinkedList):
    def __init__(self, key=lambda x: x):
        self.__key = key
        self.__first = None

    def getFirst(self):
        return self.__first

    def getNext(self):
        if self.__first is not None:
            return self.__first.getNext()
        else:
            return None

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            link.setNext(self.getFirst())
            self.__first = link
        else:
            raise Exception("First link must be a link object or None")

    def find(self, goal):
        link = self.getFirst()
        while link is not None and self.__key(link.getData()) < goal:
            link = link.getNext()
        return link

    def search(self, goal):
        link = self.find(goal)
        if link is not None and self.__key(link.getData()) == goal:
            return link.getData()
        return None

    def insert(self, newDatum):
        """
        By inheriting the definition of setNext() as a synonym for the setFirst() method,
        the OrderedList.insert() method updates either the
        __first pointer or the __next pointer depending on the data type of previous.
        """
        goal = self.__key(newDatum)
        previous = self
        while (
            previous.getNext() is not None
            and self.__key(previous.getNext().getData()) < goal
        ):
            previous = previous.getNext()
        newLink = Link(newDatum, previous.getNext())
        previous.setNext(newLink)

    def delete(self, goal):
        if self.isEmpty():
            raise Exception("Cannot delete from empty list")

        previous = self
        while (
            previous.getNext() is not None
            and self.__key(previous.getNext().getData()) < goal
        ):
            previous = previous.getNext()
        if previous.getNext() is None or goal != self.__key(
            previous.getNext().getData()
        ):
            raise Exception("no datum with matching key found")

        toDelete = previous.getNext()
        previous.setNext(toDelete.getNext())
        return toDelete.getData()

    def __len__(self):
        length = 0
        link = self.getFirst()
        while link is not None:
            length += 1
            link = link.getNext()
        return length
