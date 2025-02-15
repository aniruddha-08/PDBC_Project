import mysql.connector as mnc
def databasedrop():
    while True:
        try:
            dbname=input("Enter Database Name To Drop:-")
            con=mnc.connect(host="localhost",user="root",passwd="tiger")
            curobj=con.cursor()
            dd=f"drop database {dbname}"
            curobj.execute(dd)
            con.commit()
            print("-_"*40)
            print("\tDatabase Drop Successfully")
            print("-_"*40)
            ch=input("Do You Want Drop Another Database(YES/No):-")
            if ch.lower()=="no":
                print("_---_"*20)
                break
        except mnc.DatabaseError as db:
            print("Problem in mysql",db)

