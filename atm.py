#---->ATM Program without Functions---->
balance=1000
user_name=input("Enter username:")
pin=int(input("Enter PIN Number:"))
if user_name=="pruthvi" and pin==1234:
    while True:
        print("=== Welcome to ManaCoders ATM===")
        print("1.Check balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            print(f"Your current Balance is:{balance}")
        elif choice==2:
            amount=float(input("Enter Deposit Amount:"))
            if amount>0:
                balance+=amount
                print(f"Available Balance:{balance}")
            else:
                print("Invalid Deposit Amount..Please Enter greater than zero")
        elif choice==3:
            amount=float(input("Enter withdrawl amount:"))
            if amount<=balance:
                balance-=amount
                print(f"Available Balance :{balance}")
            else:
                print("Insufficient Funds...")
        elif choice==4:
            print("Thank Your for using our ATM Services")
            break
        else:
            print("Invalid Choice...please chooose (1-4)")
else:
    print("Authentication failed...Invalid username or pin")

