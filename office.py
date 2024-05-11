# name =["syed", "yusuf"", hussain"]
# name.append("sadiq")
# name.pop(0)
# name.remove("syed")
# print(name)

#sort the list alphabetically
# x=["orange", "mango","kivi","pineapple","banan"]
# x.sort()
# print(x)
# sort the list numerically, smallest to larget is assending order
# a= [100,50,65,87,23]
# a.sort()
# print(a)
#sort the list descending:
# y=["orange", "mango","kivi","pineapple","banan"]
# y.sort(reverse= True)
# print(y)

#  sort the list descending:
# y=["orange", "mango","kivi","pineapple","banan"]
# y.sort(reverse= False)
# print(y)


# reverse order
# b=["banana","orange","kiwi","cherry"]
# b.reverse()
# print(b)

 #sort the list descending
# x=[1,2,3,4,5]
# x.sort(reverse=True)
# print(x)

# #tuple
# a=("apple", "bababa","cherry")
# print(a)
# print(type(a))

#tuple methods
#finding tuple length
# s=("apple", "bababa","cherry")
# print(s)
# print(len(s))

# #to acces tuple items
# u=("apple", "bababa","cherry")
# print(u)
# print(a[2])

# t=("apple", "bababa","cherry")
# t.count("apple")
# print(t)

# remove all the elements from list
# a=["syed","yusuf",23, 56.89,True]
# print(a.clear())

# y=['hussain',65,1234]
# print(y.copy())

# t=("apple", "bababa","cherry")
# print(t.count("cherry"))


#date 26/2/2024
# b=['hi']
# s=[23,65,12,34]
# s.extend(b)
# print(s)

# w=[12,34,56,67]
# x=w.index(12)
# print(x)

# r=["syed","yusuf","hussain"]
# r.insert(0,12)
# print(r)

#set and not allow dublicate value (immutable )
# a={"apple", "banana", "cherry", "cherry"}
# print(a)

#get the lenght
# r={"syed yusuf  hussian"}
# print(len(r))

#get the presence of element in sequence (member operator)
# e={"apple", "banana", "cherry"}
# print("apple" in e)

#add the  vale in list
# e={"apple", "banana", "cherry"}
# e.add("orange")
# print(e)

# add the elements of other set to current set
# e={"apple", "banana", "cherry"}
# b={"pineapple", "mango", "papaya"}
# e.update(b)
# print(e)

#it also add other iterables not only set, list tuple dict added

# f={"apple", "banana", "cherry"}
# g=["syed","yusuf","hussain"]
# f.update(g)
# print(f) bhaviva

# remove element using  remove()
# x={"apple", "banana", "cherry"}
# x.remove("banana")
# print(x)
# removing the  element as above
# x={"apple", "banana", "cherry"}
# x.discard("cherry")
# print(x)

#pop method  removes the  last item present in set  as per memory 
# a={"apple", "banana", "cherry"}
# a.pop()
# print(a)
# claer method is used to empty the set , 
# x={"apple", "banana", "cherry"}
# x.clear()
# print(x)
# del keyword to delete the whole set or sequence type from memory 
# x={"apple", "banana", "cherry"}
# del x
# print(x)

#uniom keyword to add both seys and combine into one set,
#we can also use update method 
# set1={"a","b","c"}
# set2={1,2,3}
# set3= set1.union(set2)
# print(set3)
# Date 27/2/2024
# set1={"a","b","c"}
# set2={1,2,3}
# set1.update(set2)
# print(set1)
# a={12,"syed",34,89}
# a.copy()
# print(a)

# x={"syed", "yusuf","hussain"}
# x.clear()
# print(x)

#dictionary creation and type() kay and  vale is  called one element supereted by coma
# x={"brand": "Ford", "model":"mustang","year":1964}
# print(x)
# print(type(x))

#print the brand value of dictionary
# a={"brand": "Ford", "model":"mustang","year":1964}
# print(a["brand"])
#overwride the dublicate  value
# a={"brand": "Ford", "model":"mustang","year":1964,"year":2000}
# print(a["year"])
#len in dictionary kay and vale is single element
# a={"brand": "Ford", "model":"mustang","year":1964,"year":2000}
# print(len(a))

#update the year of the car by using  the update() method
# a={"name":"syed","age":14,"class":"12th"}
# a.update({"class":"b.com"})
# print(a)

#updtae the new kay and value
# a={"name":"syed","age":14,"class":"12th"}
# a.update({"clg":"teachers academy"})
# print(a)

#adding a new element using key index and assign value
# a={"brand": "Ford", "model":"mustang","year":1964}
# a["color"]="red"
# print(a)

#pop method to remove the  element using  key name
# a={"brand": "Ford", "model":"mustang","year":1964}
# a.pop("model")
# print(a)

#the popitme()method removes last inserted item
# a={"brand": "Ford", "model":"mustang","year":1964}
# a.popitem()
# print(a)

#difference
# x={"apple","banana","cherry"}
# y={"google","microsoft","apple"}
# z=y.difference(x)
# print(z)
# print(y)

#difference_update
# x={"apple","banana","cherry"}
# y={"google","microsoft","apple"}
# x.difference_update(y)
# print(x)
# print(x)

#intersection
# x={"apple","banana","cherry"}
# y={"google","microsoft","apple"}
# z=x.intersection(y)
# print(z)

#intersectionupdate
# x={"apple","banana","cherry"}
# y={"google","microsoft","apple"}
# x.intersection_update(y)
# print(x)
# print(x)

#isdisjoint:returns false if both sets have some same value or true
# x={"apple","banana","cherry"}
# y={"google","microsoft","facebook"}
# z=x.isdisjoint(y)
# print(z)
#issubset
# x={"a","b","c",}
# y={"f","e","d","c","b","a"}
# z=x.issubset(y)
# print(z)

#issuperset #hight value
# x={"f","e","d","c","b","a"} #
# y={"a","b","c"}
# z=x.issuperset(y)
# print(z)

#symmetric_diifference
# x={"apple","banana","cherry"}
# y={"google","microsoft","apple"}
# z=x.symmetric_difference(y)
# print(z)
# print(x)
#symmetric_difference_update
# x={"apple","banana","cherry"}
# y={"google","microsoft","apple"}
# x.symmetric_difference_update(y)
# print("after applying the method",x)
# print("after updation",x)
#dict
#the del keyword removes the items with the sepcified key name
# a={"brand":"ford","model":"mustang","year":1967}
# del a["model"]
# print(a)
#the clear() method empties the dic
# a={"brand":"ford","model":"mustang","year":1967}
# a.clear()
# print(a)

#copy
# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":"1968"
# }
# x=car.copy()
# print(x)

#fromkey

# x=('key1','key2','key3')
# y=0
# a=dict.fromkeys(x,y)
# print(a)

#get
# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# x=car.get("model")
# print(x)

#items
# x={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# x=car.items()
# print(x)
#keys
# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# x=car.keys()
# print(x)
#valuse

# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# x=car.values()
# print(x)

# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# x=car.setdefault('color',"white")
# print(x)
# #print(car)

#2/29
#string format
# name="joy"
# age="20"
# clg="GVT"
# message='''hi, my name is {0},
# iam {1} year old.,studing in {2} clg'''.format(name,age,clg)
# print(message)

# name="joy"
# age="20"
# clg="GVT"
# message=f'''hi, my name is {name},
# iam {age} year old.\n,studing in {clg} clg'''
# print(message)

#input function
# a=input("enter your name :")
# print(a)

# a=input("enter your name")
# print("welcome to python class",a)

# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# print("sum = ",a+b)
#type casting one data type to aonther data type


# a=input("enter your name: ")
# print(type(a))

# a=10
# if a!=2:
#     print("yes")
# else:
#     print("no")

# b=21
# if b<20:
#     print("yes")
# else:
#     print("no")    


# char=input("enter  a char ")
# char=char.lower()
# if(char=="a" or char=="e" or char=="i"or char =="o" or char=="u" ):
#     print("vowel")
# else:
#     print("consonant") 


#dt 01/03
#nested in tuple
# employee =((10,'eahul',1300),(20,'tiger',2000),(30,'lion',5000))
# print(employee)
# print(employee[2][2])

#nested in dictionary
# people={1:{'name':'michal','age':'23','place':'delhi'},
#         2:{'name':'john','age':'13','place':"bangalore"}}
# print(people)
# print(people[2]['name'])
# print(people[2]['age'])
# print(people[2]['place'])

# a=4
# b=8.0
# c=a+b
# print(type(a))
# print(type(b))
# print(type(c))

#nested list
# list=['a','b',['c','d',['e','f']],'g'],'h']
# print(list[2])
# print(list[2][2])
# print(list[2][2][0])

#to find whwther given number is postive or negative or zero
# num=int(input("enter a number "))
# if num > 0:
#     print("postive num")
# elif num <0:
#     print("negative num")
# else:
#     print("zero")


# a=int (input("enter a first number"))
# b=int (input("enter a second number"))
# c=int (input("enter a third number"))
# d=int (input("enter a fourth number"))
# if(a>b):
#     print("number 1 is greater")
# elif(b>c):
#     print("number 2 is greater")
# elif(c>d):
#     print("number 3 is greater")
# else:
#     print("number 4 is greater")

# a=30
# b=20

# if a>b:
#     print("a is greater b")
# elif a==b:
#     print("a and b are equal")
# to check the student percentage in one subject <33% and total percentage <40% is fail

# sub1=int(input("enter the marks of sub1:"))
# sub2=int(input("enter the marks of sub2:"))
# sub3=int(input("enter the marks of sub3:"))
# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are fail as you have less than 33% in one of the subject ")
# elif(sub1+sub2+sub3)/3 <40:
#     print("you are fail as you have total percentage less than 40%")
# else:
#     print("congratulstions!, you are pass in the exam")

#5/3
# a=10#/1
# b=125#/100
# if a>10:
#     print("a greater than 10")
#     if b==100:
#         print("b equal to 100")
#     elif b>100:
#         print("b greater then 100")
#     else:
#         print("b less then 100")
# elif a==10:
#     print("a equal to 10")
# else:
#     print("a less then 10")

#member ship operator
# for i in range(11):
#     print(i)    

# for i in range(1,8,2):
#     print(i)

# iterating with cequenc as out of the list
# l1=[1,2,3,4,5,6]
# for i in l1:
#     print(i)


# for i in range(5):
#     print("hello")

#table
# num=int(input("enert a number :"))
# for i in range(1,11):
#     print(f"{num}X{i}={num*i}")
#     print(str(num)+ "X" + str(i)+ "=" +str(i*num)) this one is other sept to do

#factorial
# num=int(input("enter the number :"))
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
# print(f"the factorial of {num} is :{factorial}")

# num=int(input("enter a number :"))
# sum=0
# for i in range(1,num+1):
#     sum=sum+i
# print(sum)

#program to reet name starting with letter"a"
# list=["ashok","anand","rajesh","shruthi"]
# for name in list:
#     if name.startswith("a"):
#         print("hello",name)

#to print star pattern
# for i in range(4):
#     print("*"*(i+1))#2

#nested for loop 

# for i in range(1,10):#i is a variable start from 1 if not, stat from 0
#     for j in range(i):
#         print(i,end='')
#     print()

# for loop with else
# for i in range(1,6):
#     print("hi")
# else:
#     print("done")

# infinite for loop # unlim time
# num=[0]
# for i in num:
#     print(i)
#     num.append(i+1)

# while loop

# i=0
# while i<10:
#     print("yes",i)
#     i+=1

# i=1
# while i<=50:
#     print(i)
#     i+=1
# i=1
# while i<=5:
#     print("yusuf",i)
#     i+=1

# list=[1,2,3,4,5,6,]#iteration 
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1
# nested whilw loop
# x=[1,2]
# y=[4,5]
# i=0
# while i<len(x):
#     j=0
#     while j<len(y):
#         print(x[i],y[j])
#         j+=1
#     i+=1

#infinite whileloop
# while True:
#     print("hello")

# num=int(input("enter the number : "))
# i=1
# while i<=10:
#     print(f"{num}X{i}={num*i}")
#     i+=1

# i=1
# while i <6:
#     print(i)
#     i+=1
# else:
#     print("i is no lomger less than 6")

# for i in range(1,8):
#     if (i==5):
#         break
#     print(i)
# val=1
# while val<10:
#     print(val)
#     val+=1
#     if val==3:
#         break
# for i in range (1,8):
#     if(i==6):
#         continue
#     print(i)

# i=1
# while i<=10:
#     i+=1
#     if i==4:
#         continue
#     print(i)
#pass
# i=2
# if i>5:
#     pass
# else:
#     print

#prime number which can't 
# num=8
# for i in range(2,num):
#     if num% i==0:
#         print("not prime number",i)
        #break
#     else:
#         print("it is a prime number",i)
#functions
# def name ():#user difined function
#     print('hello')
# name()
#built in function
#three type built in funtion
# print()
# input()
# len()

# def sum(a,b):
#     sum=a+b
#     print(sum)
# sum(2,3)  

# def sum(a,b):
#     sum=a+b
#     return sum
# add=sum(3,3)
# print(add)

# def sum(a,b):
#     sum=a**b
#     return sum
# add=sum(10,6)
# print(add)

# def sum(a,b):# argument 
#     sum=a/b
#     return sum
# add= sum(20,45)# function call /and argument value(20,45)
# print(add)


# def funcgreet(name):
#     print('good day,'+ name)
# funcgreet("raj")

# def funcfact_iter(n):#function defection
#     product=1
#     for i in range(n):
#         product=product*(i+1)
#     #print(product)
#         return
# fact=funcfact_iter(5)#funtion call
# print(fact)


# # recuesive function # means repeated function
# def factorial(y):
#     fact=1
#     if y==0:
#         print("0  factorial is 1")
#     else:
#         for i in range(1,y+1):
#             fact*=i
#         return fact
# ans=factorial(0)
# print(ans)

# #
# def perecent(marks):#ragument
#     p = ((marks[0]+marks[1]+marks[2]+marks[3])/400) *100
#     return p

# marks1=[45,55,65,75]
# percentage1=perecent(marks1)#call function

# marks2=[45,55,65,75]
# percentage2=perecent(marks2)
# print(percentage1,percentage2)

#define a function that returns the maxmimum of two numbers

# def max_of_two(x,y):
#     if x>y:
#         return x
#     return y

# def max_of_three(x,y,z):
#     return max_of_two(x,max_of_two(y,z))
# print(max_of_three(3,6,12))

# even odd
# def evenodd(x):
#     if x%2==0:
#         return "even"
#     else:
#         return "odd"
# num=int(input("enter a number : "))
# res=evenodd(num)# call statemnt 
# print(res)

# # eve whilw loop # user difin function
# def evenodd (x):
#     if x%2==0:
#         return"even"
#     else:
#         return "odd"
# while(True):
#     num=int(input("enter a number : "))
#     res=evenodd(num)
#     print(res)
#     con=int(input("do you want to continue \n1.yes\n2.no\n"))
#     if (con==2):
#             print("stop")
#             break

# def funcfact_iter(n):#function defection
#     product=1
#     for i in range(n):
#         product=product*(i+1)
#     print(product)
#     #return product
# funcfact_iter(5)#funtion call
# #print(fact)

# fact  using recurssion
# def fact_rec(n):
#     if n==1 or n==0:# fact of 0 is 1
#         return 1
#     else:
#         return n*fact_rec(n-1)#negative value 
# f=fact_rec(3)
# print(f)

#program for two function
# def evenodd(x):
#     return 'even' if x%2==0 else 'odd'
# def factorial(y):
#     fact=1
#     if y==0:
#         print("o factiorial is 1")
#     else:
#         for i in range(1,y+1):
#             fact*=i
#         return fact
# print("""selsect
# 1. Even and Odd Number
# 2.Factorial""")
# choice= int(input("enter your choice \n"))
# if choice==1:
#     apple=int(input("enter a number : "))  
#     print(evenodd(apple))
# elif choice==2:
#     apple=int(input("enter a number : "))
#     print(factorial(apple))
# else:
#     print("invalid")

# print("this is no input and no output function")
# def add():
#         a=20
#         b=10
#         c=a+b
#         print(c)
# add()

#print("this is input and no output function")
# def add (x,y):# pointing 
#         c=x+y
#         print(c)
# a=20# call 
# b=10
# add(a,b)
#print("this is no input and output function")
# def add():
#         a=20
#         b=10
#         c=a+b
#         return(c)
# res=add()
# print(res)

# #print("this is input and out function")
# def add(x,y):
#         c=x+y
#         return(c)
# a=20
# b=30
# res=add(a,b)
# print(res)

#RGUMENT: notes in pic
#type of argument
#1 posional argumnet 
# def power_of (num,power):
#     return num**power
# print(power_of(2,5))

# #2 keyword argument 
# def power_of(num,power):
#     return num*power
# print(power_of (num=2,power=5))

# #3 variable length argument
# def pizza_toppings(*toppings):#single stat for one time to print
#     print(toppings)
# pizza_toppings("onion","potato","chicken","paneer")

# #name is argumnet age phone 
# #keyword is megha
# #4 variable keyword argument
# def submit(**details):
#     print(details)
# submit(name='megha',age=25,gender="female",phone="why you want")

# #5 default or optional argument
# def my_function(country ="Norway"):
#     print("i am from " + country)# 
# my_function("sweden")
# my_function("india")
# my_function()
# my_function("Brazil")


# user defined function : are the function which are made by user
# recursive function : function call itself again and agai
# buli
# lambda function :single line function and it is also anomiuss funs(unnonone function)
# max= lambda a,b:a if

# max =lambda a,b : a if (a>b) else b
# print(max(1,2))

# sum =lambda a,b: a+b
# print(sum(5,6))

#passing collection to a function
# def my_function(food):
#     for x in food:
#         print(x)
# fruits=['apple','banana','cherry']
# my_function(fruits)

#set  pass collection to function # sequence
# def my_function(food):
#     for x in food:
#         print(x)
# fruits=('apple','banana','cherry')
# my_function(fruits)
#dictionary
# def my_function(food):
#     for x in food:
#         print(x)
# fruits={'apple':"value",'banana':"value",'cherry':"value"}
# my_function(fruits)

#passing function to functions
# def shout(text):
#     return text
# print(shout("rajesh"))

# yell=shout
# print(yell("raj"))
# laugh=shout
# print(laugh("andrew"))
#function to function
# def add(x,y):
#     return x+y
# def multiply (x,y):
#     return x*y
# def apply_operation (func,x,y):#func variable 
#     return func(x,y)#arument
# result= apply_operation(add,3,4)
# print(result)
# result =apply_operation(multiply,3,4)
# print(result)

#varible scope are two type 
# 1 local scope
# def myfunc ():
#     x=300
#     print(x)
# myfunc()

#2 global scope
# x=300
# def myfunc():
#     print(x)
# myfunc()
# print(x) # twice we can print 

#other ex
# x=300
# def myfunc():
#     x=200
#     print(x)
# myfunc()
# print(x)# first it will print func value then varaibale 

#global keyword
# def myfunction():
#     global x
#     x=300
# myfunction()
# print(x)

# x=300
# def myfun():
#     global x
#     x=200
# myfun()
# print(x)# which is near by x it will print  

#call by value
# string="hi"
# def test(string):
#     string="hello"
#     print("Inside function",string)
# #diver's code
# test(string)# give here
# print("outside function",string)# this can also 

# call by reference
# def add_more(list):
#     list.append(50)
#     print("Inside Function",list)
# # diver's code
# mylist=[10,20,30,40]
# add_more(mylist)
# print("outside Function",mylist)

#other ex call by value
# string="syed"
# def test(string):
#     string="Yusuf"
#     print("Inside function",string)
# #diver's code
# test(string)# give here
# print("outside function",string)

# def add_more(list):
#     list.append(40)
#     print("Inside Function",list)
# # diver's code
# mylist=[10,20,30,40]
# add_more(mylist)
# print("outside Function",mylist)

#map higher order funtion
# num_list=list(range(1,10))
# cub_list=map(lambda i:i**3,num_list)
# print(num_list,list(cub_list)) 

# #filter function
# num_list= list(range(1,10))
# gt_5=filter(lambda i:i>=5,num_list)
# print(num_list,list(gt_5))

# #reduce function
# # pre difiend value 
# from functools import reduce
# num_list=list(range(1,4))
# res=reduce(lambda i,j:i+j,num_list)# i is once j is 2 adding value
# print(num_list,res)


#regular exression new topic
import re
txt="the rain in spain"
#res=re.findall(r"[a-n]",txt) # finding in between a to n
#res=re.findall(r"[a-n]{2}",txt)# returing two accurance sing strtimes vale it will print
#res=re.findall(r"[a-n]*",txt)#
#res=re.findall(r'[a-n]+',txt)
#res=re.findall(r"in*",txt)
res=re.search(r'in',txt)
# print(res)
# if res:
#     print("word is present ")

#search
# it's not working 
# import re
# txt=input("enter a phone number :")
# res=re.search(r'^[6-9]{1}[0-9]$',txt)
# if res:
#     print("valid")
# else:
#     print("invalid")  


#to check for email id
# import re # regulal ercprence \s sub string 
# txt=input("enter a emial id :")
# res=re.search(r"[a-z,A-Z,0-9,_,-]+@[a-zA-Z0-9_.-]",txt)
# if res:
#     print("valid")
# else:
#     print("invalid")


#split

# import re 
# txt=input("enter a sentence:")
# res=re.split("\s",txt)# escpace charater \n \t\s
# print(res)       

#sub
# import re
# txt="the rain in spain "
# res=re.sub("\s","",txt) in supritng the each word with any symbol
# print(res)

#search
# import re
# txt = "the rain in spain "
# x=re.search("\s", txt)
# print("the first white-space character is located in position:",x.start())

# lambda function to find even or odd
# num=[1,2,3,4,5,6,7,8,9,20,35]
# even=filter(lambda n:n%2==0,num)
# odd=filter(lambda n:n%2==1,num)#n is argumnet 
# print(list (even))#returning the value in list 
# print(list(odd))

# list comprehension 
# number=[1,2,3,4,5]
# squared=[x**2 for x in number ]#exponents
# print(squared)

# #other one
# list=[i for i in range (11)if i % 2==0]
# print(list)

#user dif model
# def fun():
#     return "hi"

# def even(a):
#     if a%2==0:
#         print("even")#m (alaiyas name )
#     else:
#         print("odd")
# def pal(value):
#     revalue = value[::-1]
#     if value==revalue :
#         print("it is pal")
#     else:
#         print('it is not pal')

# def prime(num):
#     flag=0
#     if num<=0:
#         prime("please enter pos num")
#     elif num==1:
#         print("1 is not a prime")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 flag=1
#                 break
#     if flag:
#         print(num,"is not a prime num")
#     else:
#         print(num,"it is a prime num")


#system module is used to deeply interact with interpreter
# import sys
# print(sys.path)#to show the path of directory
# sys.path.append('d:\\py')
# import home

# #setting directory path
# #which supports module for windows, linux or mac os

# import sys
# from os.path import dirname,abspath
# apnd=dirname(dirname(abspath(__file__)))
# sys.path.append(apnd)
# import home

# search path
# import pracites # previous file my reun kary bad aha bi run hota
# import sys
# print(sys.path)

# print(dir())# this file are precent in python
# a=10
# b="name"
# print(dir())

# math model
# import math
# res=math.sqrt(9)
# print(res)

# #other ex:-
# import math as name
# res=name.sqrt(9)
# print(res)

# import math
# print(dir(math))

# from math import sqrt,pi
# res=sqrt(9)*pi
# print(res)
 
# from math import * # * is to take any thing like pi,facorialfor the below line 
# res=factorial(5)
# print(res)


       
# frm kay kato pi ki math 
# time module 
# import time
# print(time.time())

# # currect time 
# import time
# print(time.ctime(1711343105.7115598))


# date and time
# import datetime
# x=datetime.datetime.now()
# print(x)
# print(dir(datetime))# print what all are there in datetime
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.hour)

# another method
from datetime import datetime
x=datetime.now()
print(x.strftime("%A %D %Y")) #("A=day D=date Y=last 2 num of")

# todays date
from datetime import date
y=date.today()
print(y)

from datetime import date
z=date(2024,3,24) 
print (z)

import random
# x=random.random()
# print(x)# in betwen 0 to 1 in float value

# y=random.randrange(1,10)
# print(y)# only print sing value at a time

# z=random.randint(1,10)
# print(z)

# a=[1,23,4,5,6,7,8,9]
# print(random.choice(a))

#game program
# import random
# sn=random.randint(1,10)
# guess_limit=3
# guess_count=0
# print("guess the number from 1 to 10")
# while guess_count<guess_limit:
#     guess=int(input("enter your guess : "))
#     guess_count+=1
#     if guess>sn:
#         print("the number is greater")
#     elif guess<sn :
#         print("the number is lesser ")
#     else:
#         break
#     if (sn==guess):
#         print("you won")
#     else:
#         print("you lose ")
#         print("number is ",sn)

#user difiend function  ex even prali which user the funct whic user creat clled as unser defi function     
#user difine model # set of  user  define  are pre defin funcunt are stored in  a file creat by user  is aclled usr defeien moules
#pre defein moure are sandard modules ex math date time os sys  

#1032 and the above split