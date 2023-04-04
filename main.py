# Define a function to check if a player has won
def check_win(gameboard):
    # Check rows
    for i in range(0, 9, 3):
        if gameboard[i] == gameboard[i+1] == gameboard[i+2]:
            return True

    # Check columns
    for i in range(3):
        if gameboard[i] == gameboard[i+3] == gameboard[i+6]:
            return True

    # Check diagonals
    if gameboard[0] == gameboard[4] == gameboard[8]:
        return True
    if gameboard[2] == gameboard[4] == gameboard[6]:
        return True

    return False

# Define a function to place a marker on the game board
def place_on_board(player, gameboard):
    # Ask the user to choose a number from 1 to 9
    while True:
        chosen_number = input(f"{player}, choose a number from 1 to 9: ")
        if chosen_number.isdigit() and int(chosen_number) in range(1, 10):
            chosen_number = int(chosen_number)
            break
        print("Invalid input. Choose a number from 1 to 9.")

    # Check if the chosen number has already been marked
    if gameboard[chosen_number - 1] in markers:
        print("This spot has already been marked. Choose another number.")
        place_on_board(player, gameboard)
    else:
        # Change the chosen number to the player's marker in the gameboard list
        gameboard[chosen_number - 1] = markers[players.index(player)]

        # Print the game board in a 3x3 format
        print_game_board(gameboard)

        # Check if the player has won
        if check_win(gameboard):
            print(f"We have a winner! Congratulations {player}!")
            exit()

# Define a function to print the game board
def print_game_board(gameboard):
    print("-------------")
    print(f"| {gameboard[0]} | {gameboard[1]} | {gameboard[2]} |")
    print("-------------")
    print(f"| {gameboard[3]} | {gameboard[4]} | {gameboard[5]} |")
    print("-------------")
    print(f"| {gameboard[6]} | {gameboard[7]} | {gameboard[8]} |")
    print("-------------")
    
# Define a function to check if the game is a draw
def check_draw(gameboard):
    # Check if all spots on the gameboard have been marked
    if all(isinstance(i, str) for i in gameboard):
        print("We have a draw! Thank you for playing.")
        exit()

print("*** Welcome to TicTac Toe ***")

# Create an empty list to store the player names
players = []

# Ask the user to fill in the name of the first player and append it to the players list
player1 = input("Fill in the name of player 1: ")
players.append(player1)

# Ask the user to fill in the name of the second player and append it to the players list
player2 = input("Fill in the name of player 2: ")
players.append(player2)

# Create a list with the markers for each player
markers = ['X', 'O']

# Create a list with the game board
gameboard = [1, 2, 3, 4, 5, 6, 7, 8,9]

print(f"These are the players: {players}")
print(f"These are their markers: : {markers}")
print()
print(f"The game board looks like this:")
print_game_board(gameboard)

# Loop through the game until there is a winner or a draw
while True:
    place_on_board(player1, gameboard)
    check_draw(gameboard)
    place_on_board(player2, gameboard)
    check_draw(gameboard)
