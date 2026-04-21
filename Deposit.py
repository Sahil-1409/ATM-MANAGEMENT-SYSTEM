from Utils import Balance,Acc_Details
from Pin_authentication import Pin_authentication



def Deposit():
    
        x=int(input("ENTER YOUR 10 DIGIT ACCOUNT NUMBER:")) 
        if len(str(x))==10:
            while True:
                if x in Acc_Details.keys():
                        y=int(input("ENTER YOUR ACCOUNT PIN:"))
                        if len(str(y))==4:
                            if y==Acc_Details[x]:
                                z=int(input("Enter The Amount You Want To Deposit : "))
                                Balance[x] = Balance.get(x,0) + z

                                print("\nPLEASE DEPOSIT THE MONEY IN THE ATM\n")
                                print("\nMONEY DEPOSITED SUCCESSFUL\n")
                                print("💲💲💲💲💲💲💲💲💲💲",end="  ")
                                print("YOUR ACCOUNT BALANCE IS : ₹",Balance[x],end="  ")
                                print("💲💲💲💲💲💲💲💲💲💲")
                                break
                            else:
                                print("❌YOU ENTERED A WRONG PIN..... 🔑TRY AGAIN🔑.....❌")                                           
                        else:
                            print("❌IN VALID PIN FORMAT❌") 
                else:
                    print("This Account Number Doesn't Exist In Our bank")
                    ("\n\nCREATE YOUR ACCOUNT FIRST IN OUT BANK\n\n")
                    print("\n\nTHIS IS YOUR ACCOUNT CREATION PROCESS......\n\n")
                    print("\n\n⬇ENTER CHOICE 1 AND THEN ENTER ACCOUNT NUMBER TO ADD ACCOUNT⬇️\n\n")
                    break
        else:
            print("❌IN VALID ACCOUNT FORMAT❌") 
            Deposit()
                
                                

    
