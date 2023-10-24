class Person:
     country= 'India'

     def takebreath(self):
          print("I am breathing")

class Employee(Person):
    company='google'

    def getSalary(self):
         print("No salary")

    def takebreath(self):
         print("I am breathing very well")

class Programmer(Employee): 
        company='cisco'

def takebreath(self):
        print("I am  a programmer and I am breathing++")

p = Person()
e = Employee()
pr = Programmer()

print(p.country)