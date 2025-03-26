import mysql.connector

def studentdelete():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="student")

            cur = con.cursor()
            sno = int(input("enter the id of the student to delete from student database"))
            dq = "delete from studentdata where sno=%d" % (sno)
            cur.execute(dq)
            con.commit()

            if cur.rowcount == 0:
                print("no record exist with that id to delete ")
            else:
                print("{} record deleted successfully".format(cur.rowcount))
                ch = input("do u want to delete another record(yes/no)")
                if ch.lower() == "no":
                    print("thanks for using the program")
                    break

        except mysql.connector.DatabaseError as db:
            print("problem with mysql connection", db)
