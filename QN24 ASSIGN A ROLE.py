def assign_role(age, gender, experience):
    if 21 <= age <= 35:
        if gender == 'M':
            if experience >= 5: return "Senior Developer"
            else: return "Junior Developer"
        elif gender == 'F':
            if experience >= 5: return "Senior Analyst"
            else: return "Junior Analyst"
    elif age > 35:
        return "Manager Role"
    return "Not Eligible"
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
experience = int(input("Enter experience (years): "))
print(assign_role(age, gender, experience))
