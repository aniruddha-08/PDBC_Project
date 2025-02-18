import mysql.connector as mnc
def updaterecord():
    while True:
        try:
            dbname=input("Enter Database Name To Update:-")
            tbname=input("Enter Table Name:-")
            con=mnc.connect(host="localhost",user="root",passwd="tiger",database=dbname)
            curobj=con.cursor()
            sid = int(input("Enter Student Id Number:-"))
            name = input("Enter Student Name:-")
            age = int(input("Enter Student Age Greater Than 18:-"))
            gender = input("Enter Student Gender(M/F/O) only write one char:-")
            phone_no = int(input("Enter Student Phone :-"))
            ud=f"update {tbname} set name='%s',age=%d,gender='%s',phone_no=%d where sid=%d" %(name,age,gender,phone_no,sid)
            curobj.execute(ud)
            con.commit()
            print("-"*40)
            if curobj.rowcount>0 :
                print("{} Record Update Successfully Verify".format(curobj.rowcount))
            else:
                print("Record Doe Not Exist")
            print("-"*40)
            ch=input("Do You want update any Record(YES/NO):-")
            if ch.lower()=='no':
                break
            print("_---_" * 20)
            print("Database update create successfully")
        except mnc.DatabaseError as bd:
            print("Problem in MySQL",bd)
            break
        except ValueError:
            print("\tDon't Enter alnums,strs and symbols for 'sid','age' and 'phone_no' -try again")
            break
