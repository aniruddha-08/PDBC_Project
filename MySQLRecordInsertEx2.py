import mysql.connector as mnc
# from MainMySql import main
def RecordInsert():
    while True:
        try:
            dbname=input("Enter Database Name:-")
            tbname=input("Enter Tabel name:-")
            con=mnc.connect(host='localhost',user='root',passwd='tiger',database=dbname)
            curobj=con.cursor()
            print("-_"*40)
            sid = int(input("Enter Student Id Number:-"))
            name = input("Enter Student Name:-")
            age = int(input("Enter Student Age Greater Than 18:-"))
            gender = input("Enter Student Gender(M/F/O) only write one char:-")
            phone_no = int(input("Enter Student Phone :-"))
            print("-_"*40)
            di=f"insert into {tbname} values({sid},'{name}',{age},'{gender}',{phone_no})"
            curobj.execute(di)
            con.commit()
            print("-_"*40)
            print("Student Record Inserted Successfully")
            print("-_"*40)
            ch=input("Do you want add another Record(YES/NO):-")
            if ch.lower()=="no":
                break
            print("_---_" * 20)
        except mnc.DatabaseError as db:
            print("Problem In MySql", db)
            break
        except ValueError:
            print("\tDon't Enter alnums,strs and symbols for 'sid','age' and 'phone_no' -try again")
            break
