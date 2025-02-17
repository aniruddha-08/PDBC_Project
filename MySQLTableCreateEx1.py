import mysql.connector as mnc
def tablecreate():
    while True:
        try:
            dbname=input("Enter Database Name:-")
            tbname=input("Enter table Name:")
            con=mnc.connect(host='127.0.0.1',user="root",passwd='tiger',database=dbname)
            curobj=con.cursor()
            ct=f"create table {tbname}(sid int primary key,name varchar(20) not null,age int not null,gender char(1),phone_no varchar(10))"
            curobj.execute(ct)
            print("-_"*30)
            print("\tTable Create Successfully")
            print("-_"*30)
            ch=input("Do you want Create Another Table(Yes/No):")
            if ch.lower()=="no":
                break
        except mnc.DatabaseError as db:
            print("Problem in MySql",db)
            break


