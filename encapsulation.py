



#This is the code to show how protected variables work
#they work inside the parent and derived classes
#parent class
class Person:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address


obj = Person("Nichol", 30, "430 S Lane")
print("User:", obj._name)
print("Age: {}".format(obj._age))

#child/derived class demonstrating inheritance 
class Other_Person:
    def __init__(self, name, age, address):
        Person.__init__(self, name, age, address)

obj2 = Other_Person("Debby", 23, "546 Sad Road")
print("Address: {}".format(obj2._address))

#This is the code to show how private variables work
#they can only be used wihtin the class they are a part of 
class Cartoon:
    def __init__(self, main_character, world):
       self.__main_character = main_character
       self.__world = world

    def displayName(self):
        print("The main character of this cartoon is named {}. He lives in {}.".format(self.__main_character, self.__world))

obj3 = Cartoon("Steven Universe", "Beach City")
obj3.displayName()

#how to access the private data without a function
obj4 = Cartoon("Finn", "Land of Ooo")
print(obj4._Cartoon__main_character)
    
    
