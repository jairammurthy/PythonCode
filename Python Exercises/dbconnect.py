'''
The following code does the following:
Connecting to database
inserting 5 records with cursor

finally closing cursor and connection

'''

import cx_Oracle
cn=cx_Oracle.connect("sriram/mymouse#1@localhost/orcl")
cur=cn.cursor()
cur.execute("select * from products")
data=cur.fetchall()
print(len(data)," rows")

'''
for i in range(2):
    var_pid=int(input("Product Id="))
    var_Pname=input("Product Name=")
    cur.execute("insert into products values(" + str(var_pid) + ",'" + var_Pname + "')")
    
if cur.rowcount==1:
    print('Record(s)s appended')
    cn.commit()
else:
    print('no rows affected')
    cn.rollback()
        

cr=cn.cursor()
cr.execute("select * from products")
print(cr.rowcount)
            
for k in cr:
    print(k)

cr.close()'''
cur.close()
cn.close()
