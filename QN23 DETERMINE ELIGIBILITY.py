def determine_eligibility(age, gender, score):
    if 18 <= age <= 25:
        if gender == 'M':
            if score >= 85: return "Full Scholarship"
            elif score >= 70: return "Partial Scholarship"
            else: return "No Scholarship"
        elif gender == 'F':
            if score >= 80: return "Full Scholarship"
            elif score >= 65: return "Partial Scholarship"
            else: return "No Scholarship"
    return "Not Eligible"
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
score = float(input("Enter academic score (out of 100): "))
print(determine_eligibility(age, gender, score))