def scoreanalize():

    grade = int(input("Give me a grade."))


    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    else:
        return "F"

def studentrecordbuilder(name,numbergrade, lettergrade):
    studentrecord = [name, numbergrade, lettergrade]
    return studentrecord




