def start_game():
    print("Welcome to the Adventure Game!")
    print("You are in a dark forest. There are paths to the left and right.")
    choice1 = input("Which path do you take? (left/right): ").lower()
    if choice1 == "left":
        bear_path()
    elif choice1 == "right":
        river_path()
    else:
        print("Invalid choice. Game over.")

def bear_path():
    print("You encounter a bear!")
    choice = input("Do you run or fight? (run/fight): ").lower()
    if choice == "run":
        print("You safely escape. You win!")
    elif choice == "fight":
        print("The bear defeats you. Game over.")
    else:
        print("Invalid choice. Game over.")

def river_path():
    print("You find a river.")
    choice = input("Do you swim across or build a raft? (swim/raft): ").lower()
    if choice == "swim":
        print("You are carried away by the current. Game over.")
    elif choice == "raft":
        print("You cross safely and find treasure. You win!")
    else:
        print("Invalid choice. Game over.")

start_game()
