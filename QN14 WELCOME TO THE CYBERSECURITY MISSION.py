print("Welcome to the Cybersecurity Mission")
choice = input("Trace the hacker or secure the system? ").lower()
if choice == "trace the hacker":
    action = input("Track their IP or decode their message? ").lower()
    if action == "track their ip":
        print("You caught the hacker. You Win!")
    else:
        print("The message was a trap. Game Over.")
elif choice == "secure the system":
    action = input("Shut down the server or upgrade the firewall? ").lower()
    if action == "shut down the server":
        print("The attack was stopped. You Win!")
    else:
        print("The hacker bypassed it. Game Over.")
else:
    print("Invalid choice. Game Over.")