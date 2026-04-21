from Pin_authentication import Acc_Details,Pin_authentication
from Utils import Balance

def Check_balance():

        x=int(input("ENTER YOUR 10 DIGIT ACCOUNT NUMBER:"))
        if len(str(x))==10:
            while True:
                if x in Acc_Details.keys():
                        y=int(input("ENTER YOUR 4 DIGIT ACCOUNT PIN:"))
                        if len(str(y))==4:
                                if y==Acc_Details[x]:
                                    print("Your account Balance Is : ₹",Balance.get(x,0))
                                    break
                                else:
                                    print("❌YOU ENTERED A WRONG PIN..... 🔑TRY AGAIN🔑.....❌")
                                                               
                        else:
                            print("❌IN VALID PIN FORMAT❌") 
                else:
                    print("This Account Number Doesn't Exist In Our bank")
                    print("\n\nCREATE YOUR ACCOUNT FIRST IN OUT BANK\n\n")
                    print("\n\nTHIS IS YOUR ACCOUNT CREATION PROCESS......\n\n")
                    print("\n\n⬇ENTER CHOICE 1 AND THEN ENTER ACCOUNT NUMBER TO ADD ACCOUNT⬇️\n\n")
                    break
        else:
            print("❌IN VALID ACCOUNT FORMAT❌") 
            Check_balance()      
           
          
          
