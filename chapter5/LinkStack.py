from chapter5.LinkedList import LinkedList


class LinkStack(object):
    def __init__(self):
        self.__sList = LinkedList()

    def push(self, item):
        self.__sList.insert(item)

    def pop(self):
        return self.__sList.deleteFirst()

    def peek(self):
        if not self.__sList.isEmpty():
            return self.__sList.first()

    def isEmpty(self):
        return self.__sList.isEmpty()

    def __len__(self):
        return len(self.__sList)

    def __str__(self):
        return str(self.__sList)


class Stack(LinkedList):
    push = LinkedList.insert
    pop = LinkedList.deleteFirst
    peek = LinkedList.first
