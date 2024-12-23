print("Welcome to the Wizarding World")
subject = input("Choose a subject: spells or potions? ").lower()
if subject == "spells":
    action = input("Practice magic or compete in duels? ").lower()
    if action == "practice magic":
        print("You mastered a powerful spell. You Win!")
    else:
        print("You lost to a rival wizard. Game Over.")
elif subject == "potions":
    action = input("Brew an elixir or create poison? ").lower()
    if action == "brew an elixir":
        print("You healed a village. You Win!")
    else:
        print("Your potion backfired. Game Over.")
else:
    print("Invalid choice. Game Over.")