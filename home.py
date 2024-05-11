# x={"brand":"Ford","model":"mustang","year":1964}
# print(x)
# print(x["brand"])
# x={"brand":"Ford","model":"mustang","year":1964,"year":1880}
# print(x)
# print(len(x))
# x={"brand":"Ford","model":"mustang","year":1964}
# x.update({"model":"BMW"})
# print(x)
# x["color"]="red"
# print(x)
# x.pop("model")
# print(x)
# x.popitem()
# print(x)
# info={
#     "name":"syed",
#    "age":"21",
#    "class":"Graduate",
#    }
# print(info["name"])
# print(info["age"])
# print(info["class"])
# info["sure name"]="hussain"
# print(info)

# info={
# "name":"yusuf"
# }
# info["name"]="sadiq"
# info["sure name"]="syed"
# print(info)

# a=[1,2,1,"m"]
# b=[1,2,3]
# copy_a=a.copy()
# copy_a.reverse()

# if(copy_a==a):
#     print("palindrome")
# else:
#     print("not palindrome ")

# a=[1,2,1]
# copy_a=a.copy()
# copy_a=a.reverse()
# if(copy_a==a):
#     print("palindrome")
# else:
#   print("Not palindrome")

# a=int(input("enter a number "))
# if(a%3==0):
#         print("multipule of 3")
# else:
#          print("not amultiple")

# age=int(input("enter a number"))
# if(age>=18):
#      if(age>=70):
#       print("can't drive")
#      else:
#          print("can drive")
# else:
#         print("cannot drive")

# marks=int(input("enter a marks"))
# if(marks>=90):
#         print("grade A")
# elif(marks>=80 and marks<90):
#     print("grade B")
# elif(marks>=70 and marks<80):
#      print("grade C")
# elif(marks>=60 and marks<70):
#      print("grade D")
# else:
#      print("grade fail")


# # from math import e


# a=int(input("enter firt number"))
# b=int(input("enter  second number"))
# c=int(input("enter third number"))
# d=int(input("enter forth number"))
# e=int(input("enter five number"))
# if(a>b and a>=c and a>=d and a>=e):
#     print("first number greatest")
# elif(b>c and b>=c and b>=d):
#     print("second number is greatest")
# elif(c>d and c>=d):
#     print("third number is greatest")
# elif(d>=e):
#     print("forth number is greatest")
# else:
#     print("fith number is greatest")


# light=(input("enter color: "))
# if(light=="red"):
#     print("stop")
# elif(light=="yellow"):
#     print("look")
# elif(light=="green"):
#     print("go....")
# else:
#     print("other color is not list for signal")



# light=input("enter a color")
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("Go..")
# elif(light=="yello"):
#     print("look")
# else:
#     print("other color is not listed")
    
# age=int(input("enter a number"))

# if(age>=18):
#     print("can drive")
# else:
#     print("can't drive")

# rows=5
# for num in range(rows):
#     for i in range(num):
#         print(num,end= " ")
#     print(" ")

# rows=5
# b=1
# for i in range (rows,0,-1):
#     bt=1
#     for j in range (1,i+1):
#         print(b,end=" ")
#     print('\r')