def add(S, U):       
   return S + U   
def subtract(S, U):     
   return S - U   
def multiply(S, U):     
   return S * U   
def divide(S, U):       
   return S / U  
def remainder(S, U):
   return S % U     
print ("Please select the operation which you want to perform...")    
print ("1. Add")    
print ("2. Subtract")    
print ("3. Multiply")    
print ("4. Divide")
print ("5. Remainder") 
print ("6. Exit") 
choice = input("Please enter choice (1/ 2/ 3/ 4/ 5/ 6): ") 
while True: 
    num1 = int (input ("Please enter the first number: "))    
    num2 = int (input ("Please enter the second number: "))  
    if choice == '6':
       print("Exiting...!!")
       print("Thank you....!!")      
    
    elif choice == '1':    
       print (num1, " + ", num2, " = ", add(num1, num2))
       break    
    
    elif choice == '2':    
       print (num1, " - ", num2, " = ", subtract(num1, num2))
       break
    
    elif choice == '3':    
       print (num1, " * ", num2, " = ", multiply(num1, num2))
       break    
    elif choice == '4':    
       print (num1, " / ", num2, " = ", divide(num1, num2)) 
       break
    elif choice == '5' :
       print(num1, " % ", num2, " = ",remainder(num1, num2)) 
       break
    else:    
       print ("This is an invalid input . Enter the choice from 1 - 4 ......") 
       break   
print("Thank you...!!!")

