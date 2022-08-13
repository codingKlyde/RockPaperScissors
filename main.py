import random





"""
    Main menu
"""
def main_menu():
    # Accepted input are 1, 2, 3
    # Numbers below 1 and above 3, Symbolic and character/s will be invalid input
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
                print("")
                print("\t-- INVALID INPUT! Choose from 1 - 3 only --")
                print("")
        except ValueError:
            print("")
            print("\t-- INVALID INPUT! Characters and symbols are not accepted --")
            print("")



"""
    Single player mode
"""
def single_player():
    print("\n")
    print("==============================")
    print("     SINGLE PLAYER MODE")
    print("==============================")
    print("")


    p1 = player1_input()                    # Call and assign the returned input to 'p1'
    p2 = player_bot()                       # Call and assign the returned input to 'p2'
    who_wins(p1, p2)                        # Call the function to determine the winner


    print("Play again? [y/n]")
    print("---------")
    optionChoice = (input("Choice: "))

    if optionChoice == 'y' or optionChoice == 'Y':
        single_player()
    elif optionChoice == 'n' or optionChoice == 'N':
        print("\n\n")
        main_menu()
    else:
        print("")
        print("\t--INVALID INPUT! y or n only --")
        print("")
    print("\n\n")



"""
    Passs and play mode
"""
def pass_play():
    print("\n")
    print("==============================")
    print("     PASS AND PLAY MODE")
    print("==============================")
    print("")


    p1 = player1_input()                    # Call and assign the returned input to 'p1'
    p2 = player2_input()                    # Call and assign the returned input to 'p2'
    who_wins(p1, p2)                        # Call the function to determine the winner


    print("Play again? [y/n]")
    print("---------")
    optionChoice = (input("Choice: "))

    if optionChoice == 'y' or optionChoice == 'Y':
        pass_play()
    elif optionChoice == 'n' or optionChoice == 'N':
        print("\n\n")
        main_menu()
    else:
        print("")
        print("\t-- INVALID INPUT! y or n only --")
        print("")
    print("\n\n")



"""
    Player 1
"""
def player1_input():
    # Accepted input are r, p, s, R, P, or S
    # Numbers, Symbolic and other character/s will be invalid input
    while True:
        print("Player 1's turn =")
        player1 = (input("\tR-P-S?:   "))

        player1 = player1.lower()                   # Convert uppercase char into lowercase char

        if player1 == 'r' or player1 == 'p' or player1 == 's':
            return player1
        else:
            print("")
            print("\t-- INVALID INPUT! R-P-S only --")
            print("")



"""
    Player 2
"""
def player2_input():
    # Accepted input are r, p, s, R, P, or S
    # Numbers, Symbolic and other character/s will be invalid input
    while True:
        print("\nPlayer 2's turn =")
        player2 = (input("\tR-P-S?:   "))

        player2 = player2.lower()                    # Convert uppercase char into lowercase char

        if player2 == 'r' or player2 == 'p' or player2 == 's':
            return player2
        else:
            print("")
            print("\t-- INVALID INPUT! R-P-S only --")
            print("")


"""
    Player bot
"""
def player_bot():
    randomRPS = ['r', 'p', 's', 'R', 'P', 'S']

    player2 = random.choice(randomRPS)          # Get random input from the array

    print("\n[BOT] Player 2's turn =")
    print("\tR-P-S?:   ", player2)

    player2 = player2.lower()                   # Convert uppercase char into lowercase char

    return player2



"""
    Rock-Paper-Scissors winner algorithm
"""
def who_wins(player1, player2):
    print("")


    if player1 == player2:
        print("\t-- DRAW!")
    elif player1 == 'r':
        if player2 == 'p':
            print("\t-- PLAYER 2 WINS!")
        elif player2 == 's':
            print("\t-- PLAYER 1 WINS!")
    elif player1 == 'p':
        if player2 == 's':
            print("\t-- PLAYER 2 WINS!")
        elif player2 == 'r':
            print("\t-- PLAYER 1 WINS!")
    elif player1 == 's':
        if player2 == 'r':
            print("\t-- PLAYER 2 WINS!")
        elif player2 == 'p':
            print("\t-- PLAYER 1 WINS!")
    print("")



"""
    Exit program
"""
def exit_program():
    print("Bye bye !!")
    exit()





""""" 
    PROGRAM WILL START HERE
"""""
print("*********************************************************")
print("*                                                       *")
print("*               ROCK PAPER SCISSORS                     *")
print("*                                                       *")
print("*********************************************************")
print("\n")

main_menu()
