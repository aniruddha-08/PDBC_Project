# MySQLRecordDeleteEx1.py
import mysql.connector as mnc
def deleterecord():
    while True:
        try:
            dbname=input("Enter Database Name To Delete Record:-")
            tbname=input("Enter Table Name:-")
            con=mnc.connect(host="localhost",user="root",passwd="tiger",database=dbname)
            curobj=con.cursor()
            sid = int(input("Enter Student Id Number:-"))
            ud=f"delete from {tbname} where sid={sid}"
            curobj.execute(ud)
            con.commit()
            print("-"*40)
            if curobj.rowcount>0 :
                print("{} Record Delete Successfully Verify".format(curobj.rowcount))
            else:
                print("Record Doe Not Exist")
            print("-"*40)
            ch=input("Do You want Delete any Record(YES/NO):-")
            if ch.lower()=='no':
                break
            print("_---_" * 20)
        except mnc.DatabaseError as bd:
            print("Problem in MySQL",bd)
            break
        except ValueError:
            print("\tDon't Enter alnums,strs and symbols for 'sid' -try again")

