import mysql.connector


def studentadd():
    while (True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="student")

            cur = con.cursor()
            sno = int(input("enter the studentid to add in to mysql db"))
            sname = input("enter the student name to add in to mysql db")
            smarks = float(input("enter the marks of the student to add into mysql db"))
            clgname = input("enter the name of the clg to add into mysql db")

            iq = "insert into studentdata values(%d, '%s', %f, '%s')" % (sno, sname, smarks, clgname)
            cur.execute(iq)
            con.commit()

            print("{} records inserted successfully".format(cur.rowcount))
            ch = input("do u want to insert another record(yes/no)")
            if ch.lower() == "no":
                print("thanks for using the program")
                break

        except ValueError:
            print("dont enter str values, special sybols and othr invalid inputs")

        except mysql.connector.DatabaseError as db:
            print("problem with the connection", db)
