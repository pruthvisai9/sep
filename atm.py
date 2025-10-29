#simple Bank ATM

a='''
1.Deposit
2.withdraw
3.Balance Enquiry
4.Exit
'''
name="pruthvi"
password="12345"
print("Welcome to PythonLife Bank ATM")
user_name=input("Enter the user name:")
pass_word=input("Enter the password:")
balance=1000
if name==user_name  and  password==pass_word:
    while True:
        print(a)
        option=int(input("Enter your option:"))
        if option==1:
            credit_amount=float(input("Enter the amount:"))
            if credit_amount<=0:
                print("please enter a postitive amount")
            else:
                balance+=credit_amount
                print("Deposit successful,your new balance is:",balance)
        elif option==2:
            debit_amount=float(input("Enter the amount:"))
            if debit_amount<=balance:
                balance-=debit_amount
                print("withdrawl successful,your new balance is:",balance)
            else:
                print("Insufficent funds")
        elif option==3:
            print("your current Balance is:",balance)

        elif option ==4:
            print("You are exited")
            break

        else:
            print("Invalid transaction type")
            break
else:
    print("Invalid detailes")
