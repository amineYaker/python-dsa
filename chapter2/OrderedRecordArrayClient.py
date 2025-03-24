from OrderedRecordArray import * 

class Person(object):

    def __init__(self, name, age):

        self.__name = name
        self.__age = age
        
    def orderByKey(self):
        return self.__age

    def __str__(self):
        return "({} , {})".format(self.__name, self.__age)

personArray = OrderedRecordArray(10, Person.orderByKey)

personArray.insert(Person("Amine", 28))
personArray.insert(Person("Shahin", 43))

print(personArray)

personArray.insert(Person("Hao", 30))

print(personArray)

print("searching for a guy aged 28 ... " + str(personArray.search(28)))