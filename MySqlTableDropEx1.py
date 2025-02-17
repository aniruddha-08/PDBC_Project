import mysql.connector as mnc
def talbedrop():
    while True:
        try:
            dbname=input("Enter Database Name:")
            tbname=input("Enter Table Name To Drop:")
            con=mnc.connect(host="localhost",user="root",passwd="tiger",database=dbname)
            curobj=con.cursor()
            td=f"drop table {tbname}"
            curobj.execute(td)
            con.commit()
            print("-_" * 40)
            print("\tTable Drop Successfully")
            print("-_" * 40)
            ch=input("Do you want drop another Table(Yes/No):")
            if ch.lower()=="no":
                break
        except mnc.DatabaseError as db:
            print("Problem in MySql",db)
            break
