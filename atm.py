#WELCOM TO ATM
print("welcom to baroda bank")
print("insert your card")
print("select language")
total=20000
language=input("enter language")
if language=="english" or language=="hindi":
	print("right language")
pin=1234
pin=int(input("enter pin"))
if pin==1234:
	print("transaction")
transaction=int(input("select transction 1. withdraw 2. deposit 3. total"))
if transaction==1:
	withdraw=int(input("enter amount"))
	total=total-withdraw
	print("balance is:",total)
elif transaction==2:
	deposit=int(input("enter amount"))
	balance=total+deposit
	print("balance is:",balance)
elif transaction==3:
	print("balance is:",balance)
else:
	print("quite")
	print ("THANK YOU")