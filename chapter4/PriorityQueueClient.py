from PriorityQueue import *

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}: {self.age}"

def agePriority(p: Person) -> float:
    return 1 / p.age ## oldest is top prio

personQueue = PriorityQueue(10, agePriority)

for person in [Person('Amine', 28), Person('Rafiga', 28), Person('Shahin', 43), Person('Yann', 58)]:
    personQueue.insert(person)
    print(person, "has arrived")
    

print("who's next ?", personQueue.remove())

print('the remaining people will go in this order please!')

while not personQueue.isEmpty():
    next = personQueue.remove()
    print(next)