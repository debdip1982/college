science_marks = int(input("enter your science marks:"))
math_marks = int(input("enter your math marks:"))
if (science_marks>=34 and math_marks>=34):
    print("You have passed your exams")
elif(science_marks<34 and math_marks>=34):
    print("You passed math but failed in science")
elif(science_marks>=34 and math_marks<34):
    print("You passed math but failed in science")

else:
    print("You have failed in both subjects")
    