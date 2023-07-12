from backend import Savings

account_1 = Savings("Hey David Adebayo","Balance: 5000","Account type: Current account")
print(account_1.name)
y = int(input("Type in password:  "))
if y == 5555:
     print(account_1.name)
     print(account_1.balance)
     print(account_1.type)
     x = int(input("How much will you like to withdraw: "))
     if x <= 5000:
         account_1.run()
         print(5000 - x)
     elif x > 5000:
         print("Insufficient balance")
if y < 5555:
    print("Wrong password")
if y > 5555:
    print("Wrong password")



