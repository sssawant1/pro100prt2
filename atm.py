class ATM(object):
    def __init__ (self, cardnumber, pin, balance):
        self.cardnumber = cardnumber
        self.pin = pin
        self.balance = balance

    
    def check_balance(self):
        print(self.balance)

    def CashWithdrawl(self, balance):
        self.balance = self.balance - balance
        print("Your balance 50000")

new_user = ATM(10101010, 666, 50000)
new_user.CashWithdrawl(5000)
new_user.check_balance()