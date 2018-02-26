import gc #garbage collector.

class emp:
    empCount=0
    def __init__(self,ename,eid,desig,salary):
        self.ename=ename
        self.eid=eid
        self.desig=desig
        self.salary=salary
        emp.empCount+=1
        
    def __del__(self):
        emp.empCount-=1

    @classmethod
    def showEmployees(emp):
        for obj in gc.get_objects():
            if isinstance(obj, emp):
                print(obj.eid,obj.ename,obj.desig,obj.salary)

e1=emp('Tom',1324,'Operator',35612)
e2=emp('Harry',1322,'Stores',25612)
e3=emp('Rick',1354,'legal',25612)
e4=emp('Steve',1334,'accounts',15612)


print(e1, emp.empCount)
emp.showEmployees()
print('----------------------')
del e2
emp.showEmployees()
