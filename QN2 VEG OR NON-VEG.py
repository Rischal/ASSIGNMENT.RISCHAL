choice = input("Do you want vegetarian or non-vegetarian? ").lower()
if choice == "vegetarian":
    dish = input("Do you want Salad or Pasta? ").lower()
    if dish == "salad":
        print("You chose Salad!")
    elif dish == "pasta":
        print("You chose Pasta!")
    else:
        print("Invalid choice.")
elif choice == "non-vegetarian":
    dish = input("Do you want Chicken or Fish? ").lower()
    if dish == "chicken":
        print("You chose Chicken!")
    elif dish == "fish":
        print("You chose Fish!")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")