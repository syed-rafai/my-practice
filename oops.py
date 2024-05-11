#two type of programing are procegure orinded pro and oops c proces lan is procegure orinted lanu
# disadvantage of c 
# procesdure meaning same way 

# class is structed for, 
# oops realtime project
# class Student:# class name 
#     name="rahul"# class attribute
#     roll_number=1
#     subject="maths"
#     grade= 5
#pass
# s1=Student()#s1 =object
# print(s1.name)
# print(s1.roll_number)
# print(s1.subject)
# print(s1.grade)

# van=Student()
# van.name="raj"
# van.roll_number=3
# van.grade=10
# van.subject="science"
# print(van.name)
# print(van.roll_number)
# print(van.subject)
# print(van.grade)

# class Aerplan:

#     pass
# s2=Aerplan()
# s2.name="syed"

# print(s2.name)

# class Car:
#     #class object varaible
#     #can directly initialise data attributes while creating objects
#     car_color="red"
#     car_M_date="2020"
#     car_model="benz"

# c1=Car()
# print(c1.car_color,c1.car_M_date,c1.car_model)
# c2=Car()
# c2.car_color="blue"
# c2.car_M_date=2021
# c2.car_model="Maruti"
# print(c2.car_color,c2.car_M_date,c2.car_model)

#construction (dunder method)
#fundtion in oops cons is called method 

#parameterised constructor
# class Person:
#     def __int__(self,fname,my_age):#parameters
#         self.name=fname
#         self.age=my_age
#         print("executed")

# h=Person("name1",23)
# print(h.name,h.age)
      

# h1=Person("name2",23)# name1 is instance/ object
# print(h1.name,h1.age)#

# class Emplo:
#     #const 2 E name and EID
#     #var onject shlol name and id
#     def __init__(self,emp_name,emp_id):
#         self.name=emp_name# statments 
#         self.id=emp_id#statments/attribute
#         print("Emp detsils")
# Emp=Emplo("yusuf",2334)
# print(Emp.name,Emp.id)

# Emp1=Emplo("syed",1654)
# print(Emp1.name,Emp1.id)
# class Person:
#     subject=0
#     #parameterised constractors
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("executed")

#     def print_details(self,subject_name):#paermeter / aurgmet
#         print(f"hello, my name is {self.name},i learn {subject_name}")# f string formating
#     def update_subjects(self,subject_name):
#         self.subject+=1
# h=Person("name",23)
# print(h.name,h.age)
# # h.print_details("python")
# h.update_subjects("h")
# print(h.subject)

# h1=Person("name2",23)
# print(h1.name,h1.age)
# h1.print_details("C")
# h1.update_subjects("C")
# print(h1.subject)

#dunder method
#return for mate
#__str__

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def __str__(self):# to return only for str dunder method 
#         return f"my name is {self.name} and age is {self.age}"
    
# n1=Person("pavan",30)
# print(n1)
# print(type(n1))


# class method will is not object's, it will not change in object, it will wok only on  class 
# class Student:
#     subject="c"
#     def stu_details(self):# method
#         print(f"my name is {self.name}, iam studing {self.subject}")
#     @classmethod#decorators 
#     def change_sub(self,newsub):
#         self.subject=newsub
# stu_1=Student()
# stu_1.name="syed"
# #stu_1.subject="python"
# stu_1.stu_details()
# print(Student.subject)
# stu_1.change_sub("C++")
# stu_1.stu_details()
# print(Student.subject)

#to find the circumferebce of the  circle
# class Circle:
#     pi=3.14#attribute
#     def __init__(self,radius):# init is excueted while object  is created the init function excuted
#         self.radius=radius

#     def circumfrence(self):
#         return 2*self.pi*self.radius#we can also call cricle.pi(classobject)
# circle_1=Circle(4)
# print(circle_1.circumfrence())

#private class and attribute
# class Name:
#     __a="python"# private attribute / private class# this is userr defined function
#     def __program(self):
#         print("we call a function in oops as method ")
#     def print_details(self):
#             print(self.__a)
#             self.__program()
# obj=Name()
# obj.print_details()
#print(obj.a)# this for ex it wii not run in pricate
#obj.program()# same as above

#Constructors init dunder 

# class destructor:
# #initializing the class 
#     def __init__(self):
#         print("object gets created")
# #calling the destructor
#     def __del__(self):
#         print("object gets destroyed")
# #create an object
# object=destructor()
# #deleting the object
# del object

# class destructor:
#     #using constructor
#     def __init__(self,name):
#         print("inside the constructor")
#         self.name=name
#         print("object gets initialized")
#     def show(self):
#         print("the name is",self.name)
# #using destructor
#     def __del__(self):
#         print("Inside the destructor")
#         print("object gets destroyed")
# #creationg an object
# d=destructor("Destroyed")
# d.show()
# #deleting the object
# del d
#single line 
#inheritance_
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return "unknown sound"
    
# class Lion(Animal):#lion class inherits from Animal class
#     def speak(self):
#         return "Roar!"
# #create instance of subclasses
# lion_instance= Lion("king")
# print(lion_instance.name,lion_instance.speak())

# #hierarchy inheretance
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return "unknown sound"
    
# class Lion(Animal):#lion class inherits from Animal class
#     def speak(self):
#         return "Roar!"
# class Tiger(Animal):#tiger class inherits from animal class
#     def speak(self):
#         return"Growl!"
# #create instance of subclasses
# lion_instance= Lion("king")
# tiger_instance=Tiger("tony")
# print(lion_instance.name)
# print(tiger_instance.name)

# #call the speak method of the subclasses
# print(lion_instance.speak())
# print(tiger_instance.speak())

#base Class
# class GrandPa:
#     def __init__(self):
#         self.age=100
#         self.name1="raghu"
# #Intermedicate class
# class Parent(GrandPa):
#     def __init__(self):
#         self.name="raj"
#         GrandPa.__init__(self)
# #derived class
# class Grandchild(Parent):
#     def __init__(self):
#         self.hobby="gaming"
#         Parent.__init__(self)
#     def display(self):
#         print("Grandpa:",self.age)
#         print("Grandpa:",self.name1)
#         print("Parent:",self.name)
#         print("Grandchild:",self.hobby)
# obj= Grandchild()
# obj.display()


#multipul inheitance, taking freture from paye class to child class  
# class lang_1():
#     def __init__(self,name):
#         self.name=name

#     def print(self):
#         print(f"the language is {self.name}")
# class lang_2():
#     def __init__(self,name1):
#         self.name1=name1

#     def print(self):
#         print(f"the language is {self.name1}")
# class Great(lang_2,lang_1):#this called multi because first prefrence is for lang2
#     def __init__(self,name,name1):
#         self.name=name
#         self.name1=name1
# obj=Great("namastey","heyy")
# print(obj.name)
# print(obj.name1)
# obj.print()

#polymorphism #poly means meany morhs forms, meany form 
#method overloading#ducktyping 
# class Mathoperations:
#     def add(self,a,b,c=0):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
#     def add(self,a,b,d):
#         return a+b+d
    
# obj1=Mathoperations()
# print(obj1.add(1,2,4))

# a="Aeroplane"
# print(len(a))# lenfunction 

# a=[1,2,3,4,5]
# print(len(a))
# print(a[0])
# car={
#     "barnd":"food",
#     "model":"mutang",
#     "yera":1967
#     }
# print(len(car))

# #import required module # heading
# from abc import ABC,abstractmethod# file name aur 
# #create Abstract baser class
# class Car(ABC):
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     #creat abstract method
#     @abstractmethod#  @ is caled decorater
#     def printdetails(self):
#         pass
#     #creat concret method
#     def accelerate(self):
#         print("speed up...")
#     def break_applied(self):
#         print("car stop")
# #created a child class
# class Hatchback(Car):
#     def printdetails(self):
#         print("Brand:",self.brand)
#         print("model",self.model)
#         print("year",self.year)
#     def Sunroof(self):
#         print("not having this feature")
# ##create a child class
# class Suv(Car):
#     def printdetails(self):
#         print("brand:",self.brand)
#         print("model",self.model)
#         print("year",self.year)
#     def Sumroof(self):
#         print("Available")
# car1=Suv("Maruti","Alto","2022")
# car2=Hatchback("honda","city","2016")
# car1.printdetails()
# car1.accelerate()
# car1.Sumroof()

# car2.printdetails()
# car2.accelerate()
# car2.Sunroof()
#@static method
#creat

 
#Public (public): Members declared public are accessible from anywhere, both inside and outside the class. Unless explicitly marked as private, all Python members are public by default.
# Protected (protected): Members declared as protected are accessible within the class and its subclasses. In order to declare a member protected, you can prefix its name with an underscore (_).
# Private (private): Members that are declared as private are only accessible within the class. To declare a member as private, you can prefix its name with double underscores (__).
class Bike:
    def __init__(self,make,model):
        self._make=make #protected attribute# 
        self.__model=model #private attribute
    def start_engine(self):
        print(f"{self._make} {self.__model} engine started")

    def __drive(self):
        print(f"{self._make} {self.__model} is driving")
##creating an instance /obj of the Bike class
my_bike=Bike("Harley_Davidson","Iron 883")
##Accessing public method
my_bike.start_engine()
##Accessing protected attribute
print(my_bike._make)#class and sub class 
##Accessing private attribute
print(my_bike._Bike__model)

#from348


