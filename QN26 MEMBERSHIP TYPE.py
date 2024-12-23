def calculate_membership_fee(age, gender, membership_type):
    if 18 <= age < 30:
        if gender == 'M':
            if membership_type == 'Monthly': return 50
            else: return 500
        elif gender == 'F':
            if membership_type == 'Monthly': return 45
            else: return 450
    elif 30 <= age <= 50:
        if membership_type == 'Monthly': return 60
        else: return 600
    elif age > 50:
        if membership_type == 'Monthly': return 40
        else: return 400
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
membership_type = input("Enter membership type (Monthly/Yearly): ")
print(f"Membership Fee: Rs{calculate_membership_fee(age, gender, membership_type)}")