#read 
# file=open("new_txt","r")
# text=file.readline()#only first line #read both the line
# print(text)
# file.close

##write overriding
# file=open("new_txt","w") # w over ride # a will append
# file.write(" working ")
# file.close()

# file=open("new_txt","r")
# file.seek(4)#searching for fist line 
# print(file.readline())

file=open("new_txt","r")
print(file.readline())#total count readline is single line# read ful line 
print(file.tell())

##
