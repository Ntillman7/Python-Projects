#this is the parent class which contains one regular and one abstract method
from abc import ABC, abstractmethod
class Animal(ABC):
    def hunt(self, food): #regular method
        print("This animal is hunting for {}".format(food))

    @abstractmethod #abstract method
    def sound(self, sound):
        pass

#his is the child class that defines the implementation of the parent's abstract method
class Lion(Animal):
    def sound(self, sound):
        print("The dog makes this sound... {}.".format(sound))

#this is an object utilizing both the regular and abstract method
obj = Lion()
obj.hunt("gazelle")
obj.sound("roar")

