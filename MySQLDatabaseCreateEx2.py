import mysql.connector as mnc
def databasecreate():
    while True:
        try:
            databasename=input("Enter Database Name To Create:-")
            con=mnc.connect(host="localhost",user='root',passwd="tiger")
            curobj=con.cursor()
            dc=f"create database {databasename}"
            df=curobj.execute(dc)
            print("-_"*40)
            print("\tDatabase Created Successfully")
            print("-_"*40)
            ch=input("Do You Want Create Another Database Name(YES/NO):-")
            if ch.lower()=="no":
                print("_---_"*20)
                break
        except mnc.DatabaseError as dbe:
            print("Problem in mysql",dbe)
            break
