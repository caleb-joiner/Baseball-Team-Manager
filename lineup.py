def main_menu():
    print("=============================================================")
    print("Baseball Team Manager")
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print()
    print("POSITIONS")
    print("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    print("=============================================================")
    print()

def display(lineup):
    if len(lineup) == 0:
        print("The lineup is empty. Add players to it.")
        print()
        add(lineup)
    else:
        for i, player in enumerate(lineup, start = 1):
            print(f"{i}. {player[0]}")
    print()

def add(lineup):
    positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

    name = str(input("Enter players last name: "))
    position = str(input("Enter players position: ")).upper()

# UnboundLocalError for (average) if position is messed up
    if position in positions:
        at_bats = int(input("Enter number of at bats: "))
        while at_bats < 0:
            print("At bats must be greater than 0. Try again.")
            at_bats = int(input("Enter number of at bats: "))
        hits = int(input("Enter number of hits: "))
        while hits < 0:
            print("Hits must be greater than 0. Try again.")
            hits = int(input("Enter number of hits: "))
        while hits > at_bats:
            print("Hits cannot be greater than at bats. Try again.")
            hits = int(input("Enter number of hits: "))
    else:
        print("Not a valid position. Try again.")
        add(lineup)
    print()

    average = round(hits / at_bats, 3)
    player = [name.title(), position.upper(), at_bats, hits, average]
    lineup.append(player)
    print(f"{player[0]} was added to the lineup.")

def remove(lineup):
    display(lineup)
    number = int(input("Enter the lineup number you'd like to remove: "))

    if number < 1 or number > len(lineup):
        print("Enter a valid lineup number. Try again.")
        remove(lineup)
    else:
        player = lineup.pop(number - 1)
        print(f"{player[0]} was removed from the lineup.")
    print()

def move(lineup):
    oldindex = int(input("Enter the lineup position you want to move: "))
    newindex = int(input("Enter the new lineup position: "))

    lineup.insert(newindex - 1, lineup.pop(oldindex - 1))
    display(lineup)

def main():
    lineup = []

    while True:
        main_menu()
        user_choice = int(input("Enter a menu option: "))
        if user_choice == 1:
            display(lineup)
        elif user_choice == 2:
            add(lineup)
        elif user_choice == 3:
            remove(lineup)
        elif user_choice == 4:
            move(lineup)
        elif user_choice == 7:
            break
        else:
            print("Not a valid menu option. Try again.")
    print("Goodbye.")

if __name__ == "__main__":
    main()