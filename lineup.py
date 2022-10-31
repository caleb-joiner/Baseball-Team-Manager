print("=============================================================")
print("Baseball Team Manager")
print("MENU OPTIONS")
print("1 - Calculate batting average")
print("2 - Exit program")
print("=============================================================")
print()

user_choice = int(input("Enter a menu option: "))
if user_choice == 1:
    name = input("Enter player's name: ")
    at_bats = int(input("Enter player's at bats: "))
    hits = int(input("Enter player's hits: "))
    average = round(hits / at_bats, 3)

    print(f"{name}'s batting average is {average}")
elif user_choice == 2:
    print("Goodbye.")
    exit()
else:
    print("Not a valid option. Please try again.")