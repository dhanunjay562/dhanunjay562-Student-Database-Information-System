import mysql.connector
def studentupdate():
    while (True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="student")
            cur = con.cursor()
            sno = int(input("enter the student id to update the data"))
            sname = input("enter the name of the student to update in the mysql db")
            smarks = int(input("enter the marks of the student to update in the mysql database"))
            clgname = input("enter the name of the clg to update in the database")

            uq = "update studentdata set sname='%s', smarks=%d, clgname='%s' where sno=%d" % (sname, smarks, clgname, sno)
            cur.execute(uq)
            con.commit()

            if cur.rowcount > 0:
                print("{} student record updated successfully".format(cur.rowcount))
            else:
                print("no record exist to delete")
        except ValueError:
            print("dont enter strs, special sybols and othr invalid inputs")
