from chapter5.LinkedList import LinkedList, Link


class DoubleEndedList(LinkedList):
    def __init__(self):
        self.__first = None
        self.__last = None

    def getFirst(self):
        return self.__first

    def first(self):
        if self.isEmpty():
            raise Exception("No first element in empty list")
        return self.__first.getData()

    def getLast(self):
        return self.__last

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
            if link is None or self.getLast() is None:
                self.__last = link
        else:
            raise Exception("First link must be a link object or None")

    def last(self):
        if self.isEmpty():
            raise Exception("No last element in empty list")
        return self.__last.getData()

    def insertLast(self, datum):
        if self.isEmpty():
            return self.insert(datum)
        link = Link(datum)
        self.__last.setNext(link)
        self.__last = link

    def insertAfter(self, goal, newDatum, key=lambda x: x):
        link = self.find(goal, key)
        if link is None:
            return False
        newLink = Link(newDatum, link.getNext())
        link.setNext(newLink)
        if link == self.__last:
            self.__last = newLink
        return True

    def delete(self, goal, key=lambda x: x):
        if self.isEmpty():
            raise Exception("Cannot delete from empty list")
        previous = self
        while previous.getNext() is not None:
            link = previous.getNext()
            if goal == key(link.getData()):
                if link == self.__last:
                    self.__last = previous
                previous.setNext(link.getNext())
                return link.getData()
            previous = link

        raise Exception("Item not found in the list")
