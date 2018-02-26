#dbstored procedure execution
#finding a square of a number

'''import cx_Oracle
con=cx_Oracle.connect("sriram/mymouse#1@localhost/orcl")
cur=con.cursor()
myvar=cur.var(cx_Oracle.NUMBER)
cur.callproc("mult",(12,myvar))
print(myvar)
cur.close()
con.close()'''



#dbstored procedure execution
# adding a record
import cx_Oracle
con=cx_Oracle.connect("sriram/mymouse#1@localhost/orcl")
cur=con.cursor()
myvar=cur.var(cx_Oracle.NUMBER)
pid=int(input("Provide PID"))
pname=input("Product name")
cur.callproc("addrec",(pid,pname,myvar))
print(myvar)
cur.close()
con.close()
