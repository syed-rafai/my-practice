def fun():
    return "hi"

def even(a):
    if a%2==0:
        print("even")#m (alaiyas name )
    else:
        print("odd")
        
def pal(value):
    revalue = value[::-1]
    if value==revalue :
        print("it is pal")
    else:
        print('it is not pal')

def prime(num):
    flag=0
    if num<=0:
        prime("please enter pos num")
    elif num==1:
        print("1 is not a prime")
    else:
        for i in range(2,num):
            if num%i==0:
                flag=1
                break
    if flag:
        print(num,"is not a prime num")
    else:
        print(num,"it is a prime num")