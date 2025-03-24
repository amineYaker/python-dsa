from OrderedArray import *

maxSize = 10

arr = OrderedArray(maxSize)

arr.insert(3)

arr.insert(1)

arr.insert(2)

print(arr)

print("deleting 2 ...")

arr.delete(2)

print(arr)

print("array.find(1) returns " + str(arr.find(1)))