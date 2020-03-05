import os
import platform

# Display the board at the terminal based on board_list
def display_board(board_list):

    clear()
    
    print(f"       |       |       ")
    print(f"   {board_list[7]}   |   {board_list[8]}   |   {board_list[9]}   ")
    print(f"       |       |       ")

    print("-----------------------")

    print(f"       |       |       ")
    print(f"   {board_list[4]}   |   {board_list[5]}   |   {board_list[6]}   ")
    print(f"       |       |       ")

    print("-----------------------")

    print(f"       |       |       ")
    print(f"   {board_list[1]}   |   {board_list[2]}   |   {board_list[3]}   ")
    print(f"       |       |       ")
    
    print("\n")
    return

# Takes the input number and return the new board state (as a list)
def get_input(isPlayerOne):

    location_taken = True
    play_location = 0

    while (location_taken):
        play_location = int(input("Mark an available location: "))

        if (board_list[play_location] == ' ') and isPlayerOne:
            location_taken = False
            board_list[play_location] = 'X'
        elif (board_list[play_location] == ' ') and not isPlayerOne:
            location_taken = False
            board_list[play_location] = 'O'


    return board_list


# Check if the game is tied, ongoing or won by either players
'''
Return True if the game if ongoing and False if the game ended
'''
def check_game_status(isPlayerOne):

    status_dict = {'gaming': True,'winner': ""}

    # Checking horizontals
    if (board_list[1] == board_list[2] == board_list[3] != ' '):
        if (isPlayerOne):
            status_dict['winner'] = "Player 1"
        else:
            status_dict['winner'] = "Player 2"

    elif (board_list[4] == board_list[5] == board_list[6] != ' '):
        if (isPlayerOne):
            status_dict['winner'] = "Player 1"
        else:
            status_dict['winner'] = "Player 2"
    
    elif (board_list[7] == board_list[8] == board_list[9] != ' '):
        if (isPlayerOne):
            status_dict['winner'] = "Player 1"
        else:
            status_dict['winner'] = "Player 2"
    
    # Checking verticals
    elif (board_list[1] == board_list[4] == board_list[7] != ' '):
        if (isPlayerOne):
            status_dict['winner'] = "Player 1"
        else:
            status_dict['winner'] = "Player 2"
    elif (board_list[2] == board_list[5] == board_list[8] != ' '):
        if (isPlayerOne):
            status_dict['winner'] = "Player 1"
        else:
            status_dict['winner'] = "Player 2"
    elif (board_list[3] == board_list[6] == board_list[9] != ' '):
        if (isPlayerOne):
            status_dict['winner'] = "Player 1"
        else:
            status_dict['winner'] = "Player 2"

    # Checking diagonals
    elif (board_list[1] == board_list[5] == board_list[9] != ' '):
        if (isPlayerOne):
            status_dict['winner'] = "Player 1"
        else:
            status_dict['winner'] = "Player 2"
    elif (board_list[7] == board_list[5] == board_list[3] != ' '):
        if (isPlayerOne):
            status_dict['winner'] = "Player 1"
        else:
            status_dict['winner'] = "Player 2"
    
    if not(' ' in board_list):
        status_dict['winner'] = None

    if ((status_dict['winner'] == "Player 1") or (status_dict['winner'] == "Player 2") or (status_dict['winner'] == None)):
        status_dict['gaming'] = False

    else:
        status_dict['gaming'] = True
    
    return status_dict



if platform.system() == 'Windows':
    clear = lambda: os.system('cls')
elif platform.system() == 'Linux' or platform.system() == 'Darwin':
    clear = lambda: os.system('clear')

play_again = 'y'

while (play_again == 'y'):
    board_list = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_status = {}
    gaming = True
    isPlayerOne = True

    while (gaming):
        display_board(get_input(isPlayerOne))
        game_status = check_game_status(isPlayerOne)
        gaming = game_status['gaming']
        isPlayerOne = not (isPlayerOne)

    if (game_status['winner'] == None):
        print("The game tied!")
    else: 
        print(f"{game_status['winner']} WINS!")

    play_again = input("Play again? y/n: ")

    
