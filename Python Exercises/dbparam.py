#dbparam
#applying paramaeterised queries.

import cx_Oracle
con=cx_Oracle.connect("sriram/mymouse#1@localhost/orcl")
cur=con.cursor()
cur.prepare("select * from products where pid=:1")
a=True
while a:
    if a:
        pid=int(input("Enter a product Id"))
        cur.execute(None,{'1':pid})
        data=cur.fetchall()
        print(len(data)," Rows")
        for k in data:
            print(k)

    b=input("Continue")
    print(b,a)
    if b !=a:
       cur.close()
       con.close()
       break
    else:
        continue
