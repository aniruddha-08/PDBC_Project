import mysql.connector as mnc
def recordshow():
    while True:
        try:
            dbname=input("Enter Database Name:")
            tbname=input("Enter Table Name:")
            con=mnc.connect(host="localhost",user='root',passwd='tiger',database=dbname)
            curobj=con.cursor()
            st=f"select * from {tbname}"
            curobj.execute(st)
            metadata = curobj.description
            print("-" * 50)
            for colinfo in metadata:
                print("\t" + colinfo[0], end="\t")
            print()
            print("-" * 50)
            records = curobj.fetchall()
            if (len(records) == 0):
                print("Table does not records")
            else:
                for record in records:
                    for val in record:
                        print("\t{}".format(val), end="\t")
                    print()
            print("-" * 50)
            print("Table Show Successfully")
            ch=input("Do you want Check another Table(Yes/No):")
            if ch.lower()=="no":
                break
        except mnc.DatabaseError as db:
            print("File Nit Found Error",db)
            break
