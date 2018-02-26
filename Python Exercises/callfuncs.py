# executing oracle function

import cx_Oracle
con=cx_Oracle.connect("sriram/mymouse#1@localhost/orcl")
cur=con.cursor()

myvar=cur.var(cx_Oracle.NUMBER)
myvar=cur.callfunc("cubes",cx_Oracle.NUMBER,(7,))
print(myvar)
cur.close()
con.close()

