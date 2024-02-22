#!/usr/bin/env python3

class CashRegister:
    items = []
    def __init__(self, discount=0, total=0):

        self.discount = discount
        self.total = total

    def add_item(self, title, price, quantity=1):
        
        # print("Adding item")
        self.title = title
        self.price = price * quantity
        self.total = self.price + self.total
    
    def apply_discount(self):
        
        # print("Applying discount")
        self.total = self.total - (self.total * (self.discount/100))


cash_register = CashRegister(.2)
print(cash_register.discount)