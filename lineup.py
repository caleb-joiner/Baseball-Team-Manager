import csv

FILENAME = "lineup.csv"

def write_lineup(lineup):
    with open(FILENAME, "w") as file:
        writer = csv.writer(file)
        writer.writerows(lineup)

            
def read_lineup():
    lineup = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            lineup.append(row)
    return lineup

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

def add(lineup, positions):

    name = str(input("Enter players last name: "))
    position = str(input("Enter players position: ")).upper()

# UnboundLocalError for (average) if position is messed up
    if position in positions:
        try:
            at_bats = int(input("Enter number of at bats: "))
            while at_bats < 0:
                print("At bats must be greater than 0. Try again.")
                at_bats = int(input("Enter number of at bats: "))
        except ValueError:
            print("Enter a valid input for at bats.")
            at_bats = int(input("Enter number of at bats: "))
        try:
            hits = int(input("Enter number of hits: "))
            while hits < 0:
                print("Hits must be greater than 0. Try again.")
                hits = int(input("Enter number of hits: "))
        except ValueError:
            print("Enter a valid input for hits.")
            hits = int(input("Enter number of hits: "))
        while hits > at_bats:
            print("Hits cannot be greater than at bats. Try again.")
            hits = int(input("Enter number of hits: "))
    else:
        print("Not a valid position. Try again.")
        add(lineup, positions)

    average = round(hits / at_bats, 3)
    player = [name.title(), position.upper(), at_bats, hits, format(average, ".3f")]
    lineup.append(player)
    write_lineup(lineup)
    print(f"{player[0]} was added to the lineup.")

def remove(lineup):
    display(lineup)
    number = int(input("Enter the lineup number you'd like to remove: "))

    if number < 1 or number > len(lineup):
        print("Enter a valid lineup number. Try again.")
        remove(lineup)
    else:
        player = lineup.pop(number - 1)
        write_lineup(lineup)
        print(f"{player[0]} was removed from the lineup.")
    print()

def move(lineup):
    oldindex = int(input("Enter the lineup position you want to move: "))
    newindex = int(input("Enter the new lineup position: "))

    lineup.insert(newindex - 1, lineup.pop(oldindex - 1))
    display(lineup)

def edit_pos(lineup, positions):
    ind = int(input("Enter player index to edit: "))
    print("Player details", lineup[ind - 1])
    pos = input("Enter new position: ").upper()
    if pos in positions:
        lineup[ind - 1][1] = pos
        write_lineup(lineup)
    else:
        print("Enter valid position.")
        edit_pos()

def edit_stats(lineup):
    ind = int(input("Enter player index to edit: "))
    print("Player details", lineup[ind - 1])
    new_abs = int(input("Enter at bats: "))
    new_hits = int(input("Enter hits: "))
    new_avg = round(new_hits / new_abs, 3)
    
    lineup[ind - 1][2] = new_abs
    lineup[ind - 1][3] = new_hits
    lineup[ind - 1][4] = new_avg
    write_lineup(lineup)

def main():
    lineup = read_lineup()    
    positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

    while True:
        main_menu()
        user_choice = int(input("Enter a menu option: "))
        if user_choice == 1:
            display(lineup)
        elif user_choice == 2:
            add(lineup, positions)
        elif user_choice == 3:
            remove(lineup)
        elif user_choice == 4:
            move(lineup)
        elif user_choice == 5:
            edit_pos(lineup, positions)
        elif user_choice == 6:
            edit_stats(lineup)
        elif user_choice == 7:
            break
        else:
            print("Not a valid menu option. Try again.")
    print("Goodbye.")

if __name__ == "__main__":
    main()