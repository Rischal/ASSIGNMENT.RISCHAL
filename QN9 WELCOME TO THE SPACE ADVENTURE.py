print("Welcome to the Space Adventure")
choice = input("Do you want to land on Mars or fly to Jupiter? ").lower()
if choice == "land on mars":
    action = input("Do you want to explore or build a base? ").lower()
    if action == "explore":
        print("You found alien artifacts. You Win!")
    elif action == "build a base":
        print("You ran out of resources. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif choice == "fly to jupiter":
    print("Your spaceship crashed. Game Over.")
else:
    print("Invalid choice. Game Over.")