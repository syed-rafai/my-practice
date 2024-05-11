class Acoount:
    def __init__(self,balance,acc):
        self.balance=balance
        self.acc_no=acc

    def debit(self,amount):
        self.balance +=amount
        print("RS",amount,"was debit")
        print("total balnce = ",self.get_balance())

    def credit(self,amount):
        self.balance -=amount
        print("RS",amount,"was credited")
        print("total balance = ",self.get_balance())
    def get_balance(self):
        return self.balance
    
acc1=Acoount(500,1234)
acc1.debit(1000)
acc1.credit(200)
print(acc1.get_balance()) #out my negative jara