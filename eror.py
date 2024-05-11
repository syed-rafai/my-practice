#compile time error/syntax error:
#Any error occuring b/t the conversion process of source code to 
#byte code is called  as  syntax error or complile time error

# a=
# a='name
# a="name"
# print(a
# 1name="name"

#these are the above  given example for compile time error 

# a=10
# b=0
# c=a/b
# print(c)#runtime errors # the error is called expcation 
# print("name")


# a=int(input("enter a number : "))
# print(a)
# print(type(a))


#types of exxeptions

#1. Predefined exception
#2.user-difined exception

# predefined exceptions

# EOFError	Raised when the input() method hits an "end of file" condition (EOF)

# ImportError	Raised when an imported module does not exist

# IndentationError	Raised when indentation is not correct

# IndexError	Raised when an index of a sequence does not exist

# KeyError	Raised when a key does not exist in a dictionary

# KeyboardInterrupt	Raised when the user presses Ctrl+c, Ctrl+z or Delete

# MemoryError	Raised when a program runs out of memory

# NameError	Raised when a variable does not exist

# SyntaxError	Raised when a syntax error occurs

# TypeError	Raised when two different types are combined

# ValueError	Raised when there is a wrong value in a specified data type

# ZeroDivisionError	Raised when the second operator in a division is zero

#try except block

# a=10
# b=10
# try:
#     print(a/b)
# except:
#     print("division erorr")
# print("the program executed successfully")

#expliclit exception handling

# values=[23,45,2,1,5,0,12]

# for value in values:
#     try:
#         print(10/value)
#     except ZeroDivisionError as e:
#         print(e)
# to see the exception
# a=None
# b=2
# print(a+b)

# #exception handling
# a=None
# b=2
# try:
#     print(a+b)
# except:
#     print("not valid")

# #explicit exception handling
# a=None
# b=2
# try:
#     print(a+b)
# except TypeError as e:
#     print(e)

#try except block using else
# a=10
# b=10
# try:
#     print(a/b)
# except:
#     print("division error")
# else:
#     print("the program executed successfully")

#try except block using else and finally
# a=10
# b=0
# try:
#     print(a/b)
# except:
#     print("division")
# else:
#     print("the program exexuted sucessfully ")
# finally:
#     print("however done ")

#handling multiple exceptions
# try:
#     data={"A":1,"B":2}
#     print(10/0)
#     print(data["c"])
#     # this one we can give in above what first will give it will work 
# except KeyError:
#     print("key exception in the code")
# except ZeroDivisionError:
#     print("zerodivision error")
# finally:
#     print("execution completed...")

#predefined exception herirarchy
# print(IndentationError.mro())#mro: method resolution order
# print(KeyError.mro())

#Raise
# raise ZeroDivisionError("no")

#maanually raising an error and handling it
# try:
#     raise NameError("hello")
# except NameError as e:
#     print("An NameError exception found")

#manually reraising an error/exception

# try:
#     raise NameError("hello")
# except NameError as e:
#     print("An NameError exception found")
#     raise

#raising an error on a given condition
# def value(num):
#     if num<1:
#         raise Exception(num)
#     return num
# call=value(1)#-1 0
# print(call)

#user defined exception
# class InvalidData(Exception):
#     pass
# # class InvalidMarks(Exception):#13 this is optional 
# #     pass
# marks=int(input("enter marks for student"))
# try:
#     if marks<0 or marks>100:
#         raise InvalidMarks
# except InvalidMarks:
#     print("marks should be given between 0to 100")

#assert
try:
    num=int(input("enter the number equal or lesser then 5 : "))
    assert num<=5
    print("yess, your right!!")

except AssertionError :
    print("number is either not equal or less then 5")
#138