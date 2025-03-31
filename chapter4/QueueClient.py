from Queue import *

queue = Queue(10)

for person in ['Amine', 'Eduardo', 'Wini']:
    queue.insert(person)

print(queue)

print("Next client please:", queue.remove())

while not queue.isEmpty():
    print(queue.remove(), end=' ')

print()