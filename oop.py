class Person:
    #properties/vars/instances
    def __init__(self,name,age,gender):
        self.name = name
        self.age =age
        self.gender =gender
        
        #behaviour/method/function
        def study(self):
            print("student is studying")
            
#creating an object
student1 = Person("Hussein", 23, "male")
student2 = Person("Sebastian", 20, "male")
student3 = Person("Christine", 20, "female")
print(student1.name)