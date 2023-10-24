sub1= int(input("Enter first subject marks\n"))
sub2= int(input("Enter second subject marks\n"))
sub3= int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because of your marks less than 33% in one subject")

elif(sub1+sub2+sub3)/3 < 40:
        print("yor are fail because your total percentage are less than 40%")


else :
    print("Congartulations ! you passed the exam")