#the grade calculator
def grade_for(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "F"


for m in [95, 82, 72, 55, 30]:
    print(m, "->", grade_for(m))