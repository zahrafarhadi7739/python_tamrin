import sqlite3 as sq
import re
name =input("your name is")
family = input("your family is")
phone = (input("your phone is "))
email = input("enter your email")
def create_db():
    mydb = sq.connect('phonebooklet.db')
    curs = mydb.cursor()
    curs.execute("""create your table(
        name text ,
        family text, 
        email text,
        phone int           
     )""")
    mydb.commit()
    mydb.close()
def add_table_user(name,family,phone,email):
    connect_db =sq.connect('phonebooklet.db')
    curs = connect_db.cursor()
    curs.execute("insert",(name,family,email,phone))
    connect_db.commit()
    connect_db.close()
x=input("enter family search") 
r=re.findall(x)
print(r)

         


