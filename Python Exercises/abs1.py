'''this is an exmaple of Abstraction class.
In this example, the __a variable is a class variable and cannot be
accessed outside class definition directly. It has to be acceseed via a module.
Same is applicable to methods as well.
    '''
class X:
    __a=11
    def m1(self):
        self.__a=22
        print(self.__a)
        self.m2()
    def m2(self):
        print("This is method 2")
        self.__m3()
    def __m3(self):
        print("This is method 3")
        
x1=X()
x1.m2()
x1.m1()
#x1.__m3()

