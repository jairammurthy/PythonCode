class X:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destructor called")
    def display(self):
        print('hi')

X()
print('An object created and destroyed at the same time \n')
X().display()

f=[X(),X(),X()]
print(id(f),id(f[0]),id(f[1]),id(f[2]))
print('hahahah')

#del f[2]
del f
