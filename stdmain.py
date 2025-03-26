from studentmenu import studentdata
from studentadd import studentadd
from studentviews import studentviews
from studentdelete import studentdelete
from studentupdate import studentupdate
from studentsearch import studentsearch
from exit import exit

while(True):
    studentdata()
    try:
        ch = int(input("enter ur choice"))
        match(ch):
            case 1:
                studentadd()
            case 2:
                studentviews()
            case 3:
                studentdelete()
            case 4:
                studentupdate()
            case 5:
                studentsearch()
            case 6:
                print("thanks for using the program")
                break
            case _:
                print("invalid input try again")
    except ValueError:
        print("dont enter any special characters or special symbols except 1 or 2 or 3 or 4 or 5 or 6 ")
