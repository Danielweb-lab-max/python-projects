def marks():
    getMarks=int(input("Enter marks: "))
    if getMarks > 90:
        print("Grade A")
    elif getMarks > 80:
        print("Grade B")
    else:
        print("Fail")

marks()