"""
0 rock
1 paper
2 scissor
rock wins against scissor
scissor wins against paper
paper wins agains rock
"""
# import random
# user_choice=int(input("Enter your choice : Type  0 for rock, 1 for paper,2 for scissors\nuser choice : "))
# if user_choice >=3 or user_choice <0:
#     print("invalid number ")
# else:

#     compurt_choice= random.randint(0,2)
#     print("computer chose : ")
#     print(compurt_choice)
#     if (compurt_choice== user_choice):
#         print("it's a drwa")
#     elif(compurt_choice == 0 and user_choice == 2):
#         print("you lose")
#     elif(user_choice ==0 and compurt_choice ==2):
#         print("You win...")
#     elif(compurt_choice >user_choice):
#         print("you lose")
#     elif(user_choice >compurt_choice):
#         print("you Win...")

#nested if else
# height=int(input("what is your height : "))
# if height >=3:
#     print("you can ride")
#     age=int(input("what is your age"))
#     if age <=12:
#         print("the ticket priice is 150")
#     elif age <=18:
#         print("ticket price is 250")
#     else:
#         print("tickect price is 500")
# else:
#     print("can't ride")

# num=int(input("enter a number : "))
# if num==1:
#     print("one")
# elif num==2:
#     print("two")
# elif num==3:
#     print("three")
# else:
#     print("four")

# multipul if 
# height=int(input("what is your height"))
# bill=0
# if height >=3:
#     print("you can ride")
#     age=int(input("what is your age"))
#     if age <=12:
#         bill=150
#         print("Ticket prince is 150")
#     elif age <=18:
#         bill=250
#         print("Ticket price is 250")
#     else:
#         bill=500
#         print("Ticket price is 500")
#     want_photo=input("do you want photo (Y/N)?")
#     if want_photo=="y" or want_photo=="Y":
#         bill+=50
#     print(f" your total is {bill}")
# else:
#     print("You can't ride....")

# size=input("what size do you want s/m/l ? \n")
# bill=0
# if size =="s"or size=="S":
#     bill+=100
#     print("samll pizza price is 100")
# elif size == "m" or size=="M":
#     bill +=200
#     print("medium pizza is 200")
# else:
#     bill+=300
#     print("large prizza is 300")
# add_pepperoni=input("Do you wnat pepperoni y/n? \n")
# if add_pepperoni =="y" or add_pepperoni=="Y":
#     if size =="s" or size=="S":
#         bill+=30
#     else:
#         bill+=50
# extra_chees=input("do you want extra chess y/n? \n")
# if extra_chees =="y" or extra_chees=="Y":
#     bill+=20
# print(f"total bill is {bill}")

# import random
#lodo
# a=random.randint(0,1)
# if a==1:
#     print("head")
# else:
#     print("tail")

# import random
# a=random.randint(1,6)
# if a==1:
#     print(a)
#     print("moving one number forward")    
# elif a==2:
#     print(a)
#     print("moving two number forward")    
# elif a==3:
#     print(a)
#     print("moving three number forward")
# elif a==4:
#     print(a)
#     print("moving four number forward")
    
# elif a==5:
#     print(a)
#     print("moving five number forward")
# else:
#     print(a)
#     print("come out of the home / moving six number forward")
# import random
# name =input("enter your friends names : ")
# name_list=name.split(",")
# len_list=len(name_list)
# rand_choice=random.randint(0,len_list-1)
# print(f"{name_list[rand_choice]} will pay the bill")

##program to cal overage height from alist 
# height=(input("enter a number : "))
# height_list=height.split()
# connt=0
# for height in height_list:
#     connt=connt+1
# print(connt)
# for i in range(0,connt):
#     height_list[i]=int(height_list[i])
# print(height_list)
    
# num=input("enter any number ")
# number_list= num.split( )
# for i in range(0,len(number_list)):
#     number_list[i]=int(number_list[i])
# print(number_list)
    
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FIZZBUZZ",i)
#     elif i%3==0:
#         print("FIZZ",i)
#     elif i%5==0:
#         print("BUZZ",i)
#     else:
#         print("number",i)

### creat password easy one 
# import random
# letter=["a","b","C","D","E","F","G","h","i","g"]
# symboles=["!","@","#","$","%","^","&"]
# number=["0","1","2","3","4","5"]

# print("welcome to password genrate ")
# password= ''
# letter_n=int(input("what many number do you want ? \n"))
# symboles_n=int(input("what many number do you want ? \n"))
# number_n=int(input("what many number do you want ? \n"))
# for i in range(1,letter_n+1):
#     char=random.choice(letter)
#     password=char+password
# for i in range(1,symboles_n+1):
#     char=random.choice(symboles)
#     password=char+password
# for i in range(1,number_n+1):
#     char=random.choice(number)
#     password=char+password
# print(password)

# import random
# letter=["a","b","C","D","E","F","G","h","i","g"]
# symboles=["!","@","#","$","%","^","&"]
# number=["0","1","2","3","4","5"]

## hard one password
# print("welcome to password genrate ")
# password= [] # to shuffle here need to give in list
# letter_n=int(input("what many number do you want ? \n"))
# symboles_n=int(input("what many number do you want ? \n"))
# number_n=int(input("what many number do you want ? \n"))
# for i in range(1,letter_n+1):
#     char=random.choice(letter)
#     password+=char
# for i in range(1,symboles_n+1):
#     char=random.choice(symboles)
#     password+=char
# for i in range(1,number_n+1):
#     char=random.choice(number)
#     password+=char
#     random.shuffle(password)
# print(password)
# a=""# converting to str
# for i in password:
#     a+=i
# print(a)


## with out for loop 
# import random
# chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
# symbols = "!@#$%^&*()`~_=+<?:|"
# number = "0123456789"
# print("Welcome to password generator")
# letters = int(input("How many lowercase letters do you want?\n"))
# n_symbols = int(input("How many symbols do you want?\n"))
# num_numbers = int(input("How many numbers do you want?\n"))
# password_chars = []
# password_chars.extend(random.sample(chars, letters))#sample is takening any random 
# password_chars.extend(random.sample(symbols, n_symbols))
# password_chars.extend(random.sample(number, num_numbers))
# random.shuffle(password_chars)
# password = ''.join(password_chars)
# print("Generated password:", password)

# import random
# lower="qwertyuiopasdfghjklzxcvbnm"
# upper="QWERTYUIOPASDFGHJKLZXCVBNM"
# symbols="!@#$%^&*()`~_=+<?:|"
# number="0123456789"
# password=[]#shuffle
# all_char=lower+upper+symbols+number
# length=int(input("Enter a password length : "))
# random.shuffle(password)
# password="".join(random.sample(all_char,length))
# print("Generate password : ", password)
# print(type(password))

## zero to quit
# num=int(input("Enter a number (0 to quit)\n"))
# while num !=0:
#     print("the given number is ",num)
#     num=int(input("Enter a number (0 to quit)"))
    
# else:
#     print("The given number is zero so quit")



