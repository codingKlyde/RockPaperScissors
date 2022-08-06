import random


# FUNCTION: MAIN MENU  
def main_menu():
    print("*********************************************************")
    print("*             ROCK-PAPER-SCISSORS GAME                  *")
    print("*********************************************************")
    print("")


    # Loop until correct input
    while True:
        try:
            print("1. SINGLE PLAYER")
            print("2. PASS AND PLAY")
            print("3. EXIT")
            print("---------")
            menuChoice = int(input("Choice: "))


            if menuChoice == 1:
                single_player()
            elif menuChoice == 2:
                pass_play()
            elif menuChoice == 3:
                exit_program()
            else:
                print("\n")
                print("m>> INVALID INPUT! Choose between 1 - 3 only!")
                print("\n")
        except ValueError:
            print("\n")
            print(">> INVALID INPUT! Characters and symbols are not accepted")
            print("\n")





# FUNCTION: SINGLE PLAYER MODE
def single_player():
    print("\n\n")
    print("==============================")
    print("     SINGLE PLAYER MODE")
    print("==============================")
    print("")


    p1 = player1_input()                    # Call the function and assign to 'p1'
    p2 = player_bot()                       # Call the function and assign to 'p2'
    who_wins(p1, p2)                        # Call the function to determine the winner


    print("Do you want to play again? [y/n]")
    print("---------")
    optionChoice = (input("Choice: "))

    if optionChoice == 'y' or optionChoice == 'Y':
        single_player()
    elif optionChoice == 'n' or optionChoice == 'N':
        print("\n\n")
        main_menu()
    else:
        print("\n")
        print("> INVALID INPUT! y or n only")
        print("\n")
    print("\n\n")





# FUNCTION: PASS AND PLAY MODE
def pass_play():
    print("\n\n")
    print("==============================")
    print("     PASS AND PLAY MODE")
    print("==============================")
    print("")


    p1 = player1_input()                    # Call the function and assign to 'p1'
    p2 = player2_input()                    # Call the function and assign to 'p2'
    who_wins(p1, p2)                        # Call the function to determine the winner


    print("Do you want to play again? [y/n]")
    print("---------")
    optionChoice = (input("Choice: "))

    if optionChoice == 'y' or optionChoice == 'Y':
        pass_play()
    elif optionChoice == 'n' or optionChoice == 'N':
        print("\n\n")
        main_menu()
    else:
        print("\n")
        print("> INVALID INPUT! y or n only")
        print("\n")
    print("\n\n")





# FUNCTION: PLAYER 01
def player1_input():
    # Loop until input is either r-p-s
    while True:
        # Input
        print("Player 1's turn =")
        player1 = (input("\tR-P-S?:   "))

        player1 = player1.lower()                   # Convert uppercase char into lowercase char

        if player1 == 'r' or player1 == 'p' or player1 == 's':
            return player1
        else:
            print("")
            print(">> INVALID INPUT! R-P-S only!")
            print("")





# FUNCTION: PLAYER 02
def player2_input():
    # Loop until input is either r-p-s
    while True:
        # Input
        print("\nPlayer 2's turn =")
        player2 = (input("\tR-P-S?:   "))

        player2 = player2.lower()                    # Convert uppercase char into lowercase char

        if player2 == 'r' or player2 == 'p' or player2 == 's':
            return player2
        else:
            print("")
            print(">> INVALID INPUT! R-P-S only!")
            print("")





# FUNCTION: PLAYER BOT
def player_bot():
    # Player 2 random input
    rpsRandomizer = ['r', 'p', 's']

    player2 = random.choice(rpsRandomizer)

    print("\n[BOT] Player 2's turn =")
    print("\tR-P-S?:   ", player2)

    return player2





# FUNCTION: R-P-S WINNER ALGORITHM
def who_wins(player1, player2):
    print("\n")


    # Determine who wins the match
    if player1 == player2:
        print(">> DRAW!")
    elif player1 == 'r':
        if player2 == 'p':
            print(">> PLAYER 2 WINS!")
        elif player2 == 's':
            print(">> PLAYER 1 WINS!")
    elif player1 == 'p':
        if player2 == 's':
            print(">> PLAYER 2 WINS!")
        elif player2 == 'r':
            print(">> PLAYER 1 WINS!")
    elif player1 == 's':
        if player2 == 'r':
            print(">> PLAYER 2 WINS!")
        elif player2 == 'p':
            print(">> PLAYER 1 WINS!")
    print("\n")





# FUNCTION: EXIT
def exit_program():
    print("THANK YOU!")
    exit()





""""" 
    MAIN CODE 
"""""
# Start program
main_menu()
