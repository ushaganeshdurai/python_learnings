class BankAccSys:
    def __init__(self,acc_num,init_bal):
        self.acc_num = acc_num
        self.init_bal = init_bal

    def deposit (self,amount):
       self.init_bal = self.init_bal + amount
       return self.init_bal

    def withdraw(self,amount):
        if self.init_bal<amount or self.init_bal<=0:
            return None
        else:
            self.init_bal=self.init_bal-amount
            return self.init_bal
    def get_balance(self):
        return self.init_bal

