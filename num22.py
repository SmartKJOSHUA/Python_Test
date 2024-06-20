def grade_students(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


print(grade_students(85))  
print(grade_students(60)) 
print(grade_students(45)) 
