class A:
    i=11
    def m1(self):
        print("I am method 1")
        print(self.i)
        print(A.i)
x1=A()
x1.m1()
x1.i=45
x1.m1()
