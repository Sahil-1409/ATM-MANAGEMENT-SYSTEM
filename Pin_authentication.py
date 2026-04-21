from Utils import Acc_Details,Acc_holder_details



def Pin_authentication():   
   while True:
      Acc_number=int(input("Enter Your 10 Digit Account Number :"))
      if len(str(Acc_number))==10:
               def Pin_input():
                  Acc_pin=int(input("Enter Your 4 Digit Account Pin :"))
                  if len(str(Acc_pin))==4: 
                     Acc_Details.update({Acc_number:Acc_pin})
                     while True:
                        Acc_holder_mobile=int(input("Enter Your Mobile Number :"))
                        if len(str(Acc_holder_mobile))==10:
                           Acc_holder_name= input("Enter Your name :").isupper()
                           Acc_holder_details.update({Acc_holder_name:Acc_holder_mobile})
                           print({"Account number : Pin Number"})
                           print("⬇️")
                           print("YOUR ACCOUNT DETAILS ARE: ","ACCOUNT NUMBER : ",Acc_number,", ACCOUNT PIN : ",Acc_Details.get(Acc_number,0))
                           print("\n\n❌❌THIS IS ONLY FOR EDUCATION PURPOSE❌❌\n\n")
                        
                           print(Acc_Details)

                           print("\n\n❌❌   PLZZ 🙏 DON'T MISUSE IT❌❌\n\n")
                           break
                        else:
                           print("❌INVALID MOBILE NUMBER❌")
                  
                  else:
                     print("❌INVALID PIN FORMAT❌")
                     Pin_input()
               Pin_input()
               break

      else:
         print("❌INVALID ACCOUNT FORMAT❌")
                 
         
         

           
               
    
              