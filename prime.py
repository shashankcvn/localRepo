num=int(input("Enter the Number :"))
prime = True
for i in range(2,num):
    if (num%i==0):
       
        prime = False 
        break
if prime:
       print ("This number is prime")
     

else:
       print ("Enter number is not prime")
        