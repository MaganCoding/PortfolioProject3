#Import statements
import sys

# Create game board
one = ['|___|']
two = ['|___|']
three = ['|___|']
four = ['|___|']
five = ['|___|']
six = ['|___|']
seven = ['|___|']
eight = ['|___|']
nine = ['|___|']
gb = [one, two, three, four, five, six, seven, eight, nine]

#Create just the graph with the numbers so they know where to choose.
the_graph_w_nums = """['|_1_|']['|_2_|']['|_3_|']
['|_4_|']['|_5_|']['|_6_|']
['|_7_|']['|_8_|']['|_9_|']"""

# Explain how the game works
print(f"Welcome to TIC-TAC-TOE. Player 1 will always be X and Player 2 will always be O.\nIn order to play type the number of the square you want. Look below to know the numbers.")
print(f'{the_graph_w_nums}\nBefore we start, let me get your names.\n')

# get player 1 and player 2 names
p1_name = input("Player 1 What is your name?: ")
p2_name = input("Player 2 What is your name?: ")
game_on = True

#create a function to check if the player has won.
def is_winner(lst):
    for _ in lst:
        if 0 in lst and 3 in lst and 6 in lst:
            return True
        elif 1 in lst and 4 in lst and 7 in lst:
            return True
        elif 2 in lst and 5 in lst and 8 in lst:
            return True
        elif 0 in lst and 1 in lst and 2 in lst:
            return True
        elif 3 in lst and 4 in lst and 5 in lst:
            return True
        elif 6 in lst and 7 in lst and 8 in lst:
            return True
        elif 0 in lst and 4 in lst and 8 in lst:
            return True
        elif 2 in lst and 4 in lst and 6 in lst:
            return True
        else:
            return False

#create a function to see whether the game is over. either by draw or by 3 in a row.
def is_game_over():
    if is_winner(p1_choices):
        print(f'Game is Over {p1_name} has won')
        sys.exit()
    elif is_winner(p2_choices):
        print(f'Game is over {p2_name} has won')
        sys.exit()

    if ['|___|'] not in gb:
        game_on = False
        print("Game is over Its a draw.")
        # print(f"p1's choices: {p1_choices}. p2's choices: {p2_choices}")
        sys.exit()

#Create empty lists of the players choices
p2_choices = []
p1_choices = []

#create a function for the first player to play (X)
def p1s_turn():
    global p1_chosen_spot
    p1_chosen_spot = int(input(f"{p1_name}, Choose a spot: ")) - 1
    #append to the empty list
    p1_choices.append(p1_chosen_spot)
    gb[p1_chosen_spot] = ['| X |']

#create a function for the second player to play (O)
def p2s_turn():
    global p2_chosen_spot
    p2_chosen_spot = int(input(f"{p2_name}, Choose a spot: ")) - 1
    #append to the empty list.
    p2_choices.append(p2_chosen_spot)
    gb[p2_chosen_spot] = ["| O |"]

#Have the game start.
while game_on:
    print(f"{gb[0]}{gb[1]}{gb[2]}\n{gb[3]}{gb[4]}{gb[5]}\n{gb[6]}{gb[7]}{gb[8]}\n")

    is_game_over()
    p1s_turn()

    print(f"{gb[0]}{gb[1]}{gb[2]}\n{gb[3]}{gb[4]}{gb[5]}\n{gb[6]}{gb[7]}{gb[8]}\n")

    is_game_over()

    p2s_turn()