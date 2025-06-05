student_score = int(input("Enter the student score:"))
if student_score >= 90 & student_score < 89:
    print("The student grade is 'B'.")
elif student_score >= 70 & student_score < 79:
    print("The student grade is 'C'.")
elif student_score >= 60 & student_score < 69:
    print("The student grade is 'D'.")
elif student_score < 60:
    print("The student grade is 'F'.")