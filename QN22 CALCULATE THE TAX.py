def calculate_tax(age, gender, income):
    if age >= 18 and age < 60:
        if gender == 'M':
            if income > 1000000: return income * 0.30
            elif income >= 500000: return income * 0.20
            else: return income * 0.10
        elif gender == 'F':
            if income > 1000000: return income * 0.25
            elif income >= 500000: return income * 0.15
            else: return income * 0.05
    elif age >= 60:
        return income * 0.20 if income > 1000000 else income * 0.10
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
income = float(input("Enter income: "))
print(f"Tax: {calculate_tax(age, gender, income)}")
