"Fibonacci Series upto n integers using Recurssion relation"

def Fib_Recurs(n):    #define a function for fibonacci series
   if n <= 1:  
       return n  
   else:  
       return(Fib_Recurs(n-1) + Fib_Recurs(n-2))  

nterms = int(input("Enter the number of terms "))  # take input of number of terms from the user
   
if nterms <= 0:  # check if the number is positive 
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(Fib_Recurs(i),end=' , ')
