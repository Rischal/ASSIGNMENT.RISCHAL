print("Welcome to the Forest Adventure")
path = input("Choose a path: left or right? ").lower()
if path == "left":
    action = input("Do you want to explore or rest? ").lower()
    if action == "explore":
        print("You found treasure!")
    elif action == "rest":
        print("You were attacked by wild animals. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif path == "right":
    print("You fell into a trap. Game Over.")
else:
    print("Invalid path. Game Over.")