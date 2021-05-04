
def calc_grade(name,homework,assessment,final_exam):
    mark=((homework + assessment + final_exam)/175)*100

    if mark>70:
        grade="A"
    elif mark>=60 and mark<70:
        grade="B"
    elif mark>=50 and mark<60:
        grade="C"
    elif mark>=40 and mark<50:
        grade="D"

    return f"{name}'s  grade is: {grade}"

name = str(input("Input name: "))
homework = int(input("Input homework mark(/25): "))
assessment = int(input("Input assessment mark(/50): "))
exam=int(input("Input exam mark(/100): "))

print(calc_grade(name, homework, assessment, exam))