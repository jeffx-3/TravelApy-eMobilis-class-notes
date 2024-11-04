#parent class
class Animal:
    def move(self):
        print("animal is moving")
 
 #child class   
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
        
a = Animal()
d = Dog()
