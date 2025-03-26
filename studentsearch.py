import mysql.connector
def studentsearch():
    try:
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="root",
                                      database="student")

        cur = con.cursor()
        sno = int(input("enter the id of the student to view from student database"))
        vq = "select * from studentdata where sno=%d"%(sno)
        cur.execute(vq)
        matadata = cur.description

        for values in matadata:
            print(values[0], end="\t\t")

        print()
        print("-" * 50)

        records = cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val), end="\t\t")
            print()

    except mysql.connector.DatabaseError as db:
        print("problem with oracle connection", db)



