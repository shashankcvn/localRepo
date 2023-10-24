
NUM1=int(input("Enter number 1 : "))
NUM2=int(input("Enter number2 : "))
NUM3=int(input("Enter number 3 : "))
NUM4=int(input("Enter number 4 : "))

if(NUM1>NUM4):
    f1=NUM1
else:
    f1=NUM4


if(NUM2>NUM3):
    f2=NUM2

else:
    f2=NUM3


if (f1>f2):

    print(str(f1)  +  " is Greatest")

else:
    print(str(f2) + " is Greatest")

    