# Rock Paper Scissors Game
# https://github.com/BambooKoi/rps

import os
import pickle
import random
import sys
import time

g_round = 0     # Current Game Round
p_wins = 0      # Player's Wins
c_wins = 0      # Computer's Wins
ties = 0        # Ties

choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}


def scores():
    os.system('cls')
    print(f'ROUND: {(g_round + 1):02}')
    print(f'\nCURRENT SCORES\n{player}: {p_wins:02}\tComputer: {c_wins:02}\tTies: {ties:02}\n')


def player_win():
    global p_wins
    global g_round
    p_wins += 1
    g_round += 1
    time.sleep(1)
    print(f'> {player} wins round with {p_throw}.')


def computer_win():
    global c_wins
    global g_round
    c_wins += 1
    g_round += 1
    print(f'> COMPUTER wins round with {computer}.')


def winner():
    # Tie Scenario
    if p_throw == computer:
        global ties
        global g_round
        ties += 1
        g_round +=1
        print('> It\'s a tie!')
    
    # p_throw Wins Scenario:
    elif (p_throw == choices[1] and computer == choices[3]):
        player_win()
    elif p_throw == choices[2] and computer == choices[1]:
        player_win()
    elif p_throw == choices[3] and computer == choices[2]:
        player_win()
    
    # Computer Wins Scenario:
    elif p_throw == choices[3] and computer == choices[1]:
        computer_win()
    elif p_throw == choices[2] and computer == choices[3]:
        computer_win()
    elif p_throw == choices[1] and computer == choices[2]:
        computer_win()

    time.sleep(3)


def no_understand():
    print(f'\nSorry, "{p_throw}" isn\'t one of the available options.')
    print('Enter "help" at any time for help.')


def help():
    print('\n## HELP/INSTRUCTIONS ##')
    print('Rock, Paper, Scissors is a game about 3 objects.')
    print('Can you guess what the objects are?')
    
    print('\nThe rules are simple:')
    print('- Rock beats Scissors')
    print('- Scissors beats Paper')
    print('- Paper beats Scissors')
    print('Choose your warrior per round.')
    
    print('\nThe controls should be easy to figure out, you got to the Help screen somehow.')
    print('All you need is the ability to type and hit ENTER KEY.\n')
    print('The main choices are listed in brackets. Such as (y)es or (n)o.')
    print('You only need to enter the letter in brackets. Such as "y" to say (y)es.')
    print('Of course there are exceptions to this rule like "quit" and "help".')
    print('Save your progress at any point with "save".')
    print('When quitting, the option to save with also be available.')

    input('Press any key to continue.\n> ')


def save():
    try:
        with open('rps_scores.pydata', 'wb') as f:
            pickle.dump(player, f)
            pickle.dump(g_round, f)
            pickle.dump(p_wins, f)
            pickle.dump(c_wins, f)
            pickle.dump(ties, f)
        print('Game progress saved.\n')
    except Exception as e:
        print(e)
        print('\nSorry, I couldn\'t figure out how to save your scores.')
        input('Press (Enter Key) to continue. ')


def close():
    while True:
        print('\nWould you like to save your progress?')
        saving = input('Enter (y)es, (n)o or (help).\n> ')
        saving = saving.lower()
        if saving == 'y':
            save()
            input('Press Enter Key to quit.')
            break
        elif (saving == 'n') or (saving == 'quit'):
            break
        elif saving == 'help':
            help()
        else:
            print(f'Sorry, "{saving}" isn\'t one of the available options.')
    sys.exit()


# Main Code
print("## Rock, Paper, Scissors ##\n")

# New Game or Continue?
while True:
    print('Hello! What would you like to do?')
    p_throw = input(f'Start a (n)ew game or (c)ontinue a previous session?\n> ')
    p_throw = p_throw.lower()
    # Try to load 'rps_score.pydata'. If it doesn't exist, start a new game.
    if p_throw == 'n':
        player = input('\nPlayer, what is your name? ')
        print(f'\nHi {player}, let\'s play Rock, Paper, Scissors!')
        time.sleep(3)
        break
    elif p_throw == 'c':
        try:
            with open('rps_scores.pydata', 'rb') as f:
                player = pickle.load(f)
                g_round = pickle.load(f)
                p_wins = pickle.load(f)
                c_wins = pickle.load(f)
                ties = pickle.load(f)
                print(f'Welcome back {player}!')
                time.sleep(3)
        except:
            for i in range(3, 0, -1):
                os.system('cls')
                print(f'\nCould not find a previous save session. Starting a new game in {i}.')
                time.sleep(2)
            player = input('\nPlayer, what is your name? ')
            print(f'\nHi {player}, let\'s play Rock, Paper, Scissors!')
            time.sleep(3)
        break
    elif p_throw == 'help':
        help()
    elif p_throw == 'quit':
        sys.exit()
    else:
        no_understand()

# The Game
while True:
    scores()

    while True:  # p_throw's input loop
        p_throw = input('Enter your move: (r)ock (p)aper (s)scissors or (quit)\n> ')
        p_throw = p_throw.lower()
        if p_throw == 'quit':
            close()
        elif p_throw == 'save':
            save()
        elif (p_throw == 'r') or (p_throw == 'p') or (p_throw == 's'):
            break
        elif p_throw == 'help':
            help()
        else:
            no_understand()

    # Player's choices:
    if p_throw =="r":
        p_throw = choices[1]
    elif p_throw =="p":
        p_throw = choices[2]
    elif p_throw == "s":
        p_throw = choices[3]

    # Display what the player & computer chose:
    computer = choices[random.randint(1,3)]
    print(f'\n{player} chose {p_throw}. Computer chose {computer}')
    time.sleep(1)
    print(f'{p_throw} versus {computer}!')

    winner()
    