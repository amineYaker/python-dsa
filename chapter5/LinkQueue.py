from chapter5.DoubleEndedList import DoubleEndedList


class Queue(DoubleEndedList):
    enqueue = DoubleEndedList.insertLast
    dequeue = DoubleEndedList.deleteFirst
    peek = DoubleEndedList.first
