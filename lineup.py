print("=============================================================")
print("Baseball Team Manager")
print("This program calculates the batting average for a player ")
print("based on the player's official number of at bats and hits.")
print("=============================================================")
print()

name = input("Enter player's name: ")
at_bats = int(input("Enter player's at bats: "))
hits = int(input("Enter player's hits: "))
average = round(hits / at_bats, 3)

print(f"{name}'s batting average is {average}")