
from MySQLDatabaseCreateEx2 import databasecreate
from MySQLDatabaseDropEx2 import databasedrop
from MySQLTableCreateEx1 import tablecreate
from MySQLRecordInsertEx2 import  RecordInsert
from MySQLRecordUpdateEx1 import updaterecord
from MySQLRecordDeleteEx1 import deleterecord
from MySqlTableDropEx1 import talbedrop
from MySqlRecordShowEx1 import recordshow
def main():
    print("*"*50)
    print("\t\tStudent Information Data\n\t\tPython Project Connected With MySql")
    print("*"*50)
    print("\t1.Create Database\n\t2.Drop Database\n\t3.Create Table\n\t4.Drop Table\n\t5.Insert Record\n\t6.Update Record\n\t7.Delete Record\n\t8.Show Record\n\t9.Exit")
    import sys
    while True:
        ch=input("Enter Your Choice:-")
        match(ch):
            case '1':
                databasecreate()
            case '2':
                databasedrop()
            case '3':
                tablecreate()
            case '4':
                talbedrop()
            case '5':
                RecordInsert()
            case '6':
                updaterecord()
            case '7':
                deleterecord()
            case '8':
                recordshow()
            case '9':
                print("*-*"*30)
                print("\t\tThank You! For using This Project")
                print("*-*"*30)
                sys.exit()

            case _:
                print("Invalid Choice..Try Again")

main()