def show_ticket_price(age, gender, show_type):
    if age < 12:
        if show_type == 'Matinee': return 500
        else: return 700
    elif 12 <= age < 60:
        if gender == 'M':
            if show_type == 'Matinee': return 800
            else: return 1000
        elif gender == 'F':
            if show_type == 'Matinee': return 700
            else: return 900
    elif age >= 60:
        return 600
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
show_type = input("Enter show type (Matinee/Evening): ")
print(f"Ticket Price: Rs{show_ticket_price(age, gender, show_type)}")