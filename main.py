from Pin_authentication import Pin_authentication
from Check_balance import Check_balance
from Deposit import Deposit
from Withdraw import Withdraw
from update_acc_details import update_acc_datails



def Atm_Management():
    print("Ram Ram ji!!!!! 🙏🙏")
    print("Welcome To Our Atm Management System ✌️")
    while True:

        print("\n1. Pin Authentication 🔑")
        print("\n2. Check Balance💵")
        print("\n3. Deposit Money💲")
        print("\n4. Withdraw Money💳")
        print("\n5. Update account Details")
        print("\n6. Exit❌")

       
        choice=int(input("Enter your choice :"))

        if choice==1: Pin_authentication()
        elif choice==2: Check_balance()
        elif choice==3: Deposit()
        elif choice==4: Withdraw()
        elif choice==5: update_acc_datails()
        elif choice==6:
            print("Thank You For Using Our Atm. Hope You Liked Our Service.")
            print("Your Account Will Be Permanently Deleted If YOu Don't Visit Us Again!!!")
            break
        else:
            print("Invalid Choice")
        
Atm_Management()  

                 

        

  