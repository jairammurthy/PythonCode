import cx_Oracle
con=cx_Oracle.connect("sriram","mymouse#1","localhost")
cur=con.cursor()
p=cur.execute("select * from products")
for i in p:
    print(i)
    

