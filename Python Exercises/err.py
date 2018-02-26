# ex: 1

import os
try:
    print(os.getcwd())
    f=open("test1.html")
except Exception as e: # in this line 'as e' is optional
    print("An error occurred. And the error is given below")
    print(e)
else:
    # this part gets executed only if the try section does not throw any error.
    print("No error occurred. File reading went fine")
finally:
    print("this line gets printed irrespective of an error")



#ex-2
import os
try:
    print(os.getcwd())
    f=open("test.html")
except FileNotFoundError : # here we are specifying the exact error
    print("An error occurred. File not found error exactly caught")
else:
    # this part gets executed only if the try section does not throw any error.
    print("No error occurred. File reading went fine")
    print(f.readline())
finally:
    print("this line gets printed irrespective of an error")
