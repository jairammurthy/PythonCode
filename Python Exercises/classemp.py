class Employee:
    TAX=1.05    #this TAX and Empcount  are called class variables.
    Empcount=0
    def __init__(self,first,last,pay,dept):#Constructor
        self.first=first
        self.last=last
        self.pay=pay
        self.dept=dept
        self.email=first + '.' + last + '@mycompany.com'

        Employee.Empcount+=1

    def displayName(self): #method/function
        return '{} {}'.format(self.first,self.last)
    def apply_tax(self):
        self.pay=int(self.TAX*self.pay)

print(Employee.Empcount)
e1=Employee('sri','ram',50000,'production')
e2=Employee('Steve','rick',88800,'R&D')

print(Employee.Empcount)

#print(e1,e2)----prints addresses of objects e1 and e2
print(e1.displayName()) 

# the above print command can also be replaced with the following code:
print(Employee.displayName(e2))
e1.TAX=1.15
e1.apply_tax()
print(e1.pay)

#the following __dict__ method will list all the attributes of object e1
print(e1.__dict__)
#the following __dict__ method will list all the attributes of class Employee
print(Employee.__dict__)
