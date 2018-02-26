import datetime

class Emp:
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def onliner(self):
            return '{} {}'.format(self.name,self.age)
        @classmethod
        def anotherway(cls,name,age):
            return Emp(name,age)
        @staticmethod
        def is_itWorkDay(dt):
                if dt.weekday()==5 or dt.weekday()==6:
                        return False
                return True

e1=Emp('krishna',55)
e2=Emp.anotherway('shyam',44)
print(e2.onliner())

var_dt=datetime.date(2015,12,20)
print(Emp.is_itWorkDay(var_dt))

      
