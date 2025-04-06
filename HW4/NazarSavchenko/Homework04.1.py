grade = (123)
def gradeCalculator(grade):
    if grade > 90 and grade < 100:
        print ("A")
    elif grade > 80 and grade < 90:
        print ("B")
    elif grade > 70 and grade < 80:
        print ("C")
    elif grade > 60 and grade < 70:
        print ("D")
    elif grade > 50 and grade < 60:
        print ("E")
    elif grade > 0 and grade < 50:
        print ("F")
    else: 
        print ("Wrong number")