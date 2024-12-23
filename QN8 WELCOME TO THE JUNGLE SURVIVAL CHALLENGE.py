print("Welcome to the Jungle Survival Challenge")
action = input("Do you want to search for food or build a shelter? ").lower()
if action == "search for food":
    choice = input("Do you want to hunt or gather? ").lower()
    if choice == "hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif choice == "gather":
        print("You found enough food. You Win!")
    else:
        print("Invalid choice. Game Over.")
elif action == "build a shelter":
    print("You built a shelter and survived the night. Game Over.")
else:
    print("Invalid action. Game Over.")