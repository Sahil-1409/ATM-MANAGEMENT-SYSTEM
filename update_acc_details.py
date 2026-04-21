from Utils import Acc_Details,Balance,Acc_holder_details


def update_acc_datails():   
            while True:
                
                Acc_number=int(input("Enter Your 10 Digit Account Number ✅WHOSE PASSWORD DETAILS YOU WANR TO CHANGE✅ :"))
                if len(str(Acc_number))==10:
                    if Acc_number in Acc_Details.keys():
                                while True:
                                    Acc_pin=int(input("Enter Your 4 Digit ❌PREVIOUS❌ Account Pin :"))
                                    if len(str(Acc_pin))==4: 
                                        if Acc_pin==Acc_Details[Acc_number]:
                                                print("\n\n\nIT'S NOT THAT MUCH EASY TO CHANGE YOUR PIN FIRST YOU HAVE TO CONFIRM THIS IS YOUR ACCOUNT OR NOT\n\n")
                                                while True:
                                                        Acc_holder_name= input("Enter Your name :").isupper()
                                                        if Acc_holder_name in Acc_holder_details.keys():
                                                                    while True:
                                                                        Acc_holder_mobile=int(input("Enter Your Mobile Number :"))
                                                                        if len(str(Acc_holder_mobile))==10:
                                                                            if Acc_holder_mobile == Acc_holder_details[Acc_holder_name]:
                                                                                print("\n\nYEAAAH.....❤️IT IS CONFIRM THAT YOU ARE THE ACCOUNT HOLDER OF THIS ACCOUNT❤️.......\n\n")
                                                                                while True:
                                                                                    New_pin=int(input("ENTER THE NEW PIN WHICH YOU WANT TO UPDATE : "))
                                                                                    if len(str(New_pin))==4: 
                                                                                        Acc_Details.update({Acc_number:New_pin})
                                                                                        print("\n\nYOUR PIN HAS BEEN UPDATED\n\n")
                                                                                        print("YOUR NEW ACCOUNT PIN IS : ",New_pin)
                                                                                        
                                                                                        return
                                        
                                                                                    else:                     
                                                                                        print("❌INVALID PIN FORMAT❌")
                                                                                        
                                                                                        
                                                                            else:                         
                                                                                print("\n\n❌ 😡😡YOUR PIN UPDATION FAILED!!!!!!😡😡ERROR 404!!! THIS ACCOUNT IS NOT YOURS... YOU ARE TRYING TO ACCESS ANOTHER'S ACCOUNT❌\n\n") 
                                                                        else:
                                                                            print("invalid mobile number format...")
                                                                    
                                                        else:              
                                                            print("\n\nTHIS IS NOT THE ACCOUNT HOLDER'S CORRECT NAME TRY AGAIN....... ❌\n\n")   
                                                            
                                        else:
                                            print("❌YOU ENTERED A WRONG PIN..... 🔑TRY AGAIN🔑.....❌")
                                    else:
                                        print("❌INVALID PIN FORMAT❌")
                    else:
                        print("This Account Number Doesn't Exist In Our bank")
                else:
                    print("❌INVALID ACCOUNT FORMAT❌")
                
                        
                    