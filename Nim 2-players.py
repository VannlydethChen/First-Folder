# Clear the Idle screen and print the game board.
def print_game_board_clear():
    print('\n'*50)
    for row in game:
        print(row)
    print()

# Just print the game board.
def print_game_board():
    for row in game:
        print(row)
    print()

# the player make a move = {row number:list , amount:n}
# remove n number of 5s from list (from that row)
def remove(n,list):
    for i in range(n):
        list_order=0
        for i in list:
            if i==5:
                list[list_order]=0
                break
            list_order +=1

# check if user's input is invalid
def invalid_input(game, row, amount):
    if amount <=0:
        return True
    elif amount <= game[row].count(5):
        #no problem
        return False
    else:
        return True

# check if game is over
def game_over():
    items_in_game = []
    for i in range(len(game)):
        items_in_game.extend(game[i])
    if 5 not in items_in_game:
        return True





# START THE GAME!!!
# game = a list containing each row game board.
game=[
      ['       The nim game       '],
      ['          ',5,'         '],
      ['       ',5,5,5,'      '],
      ['    ',5,5,5,5,5,'   '],
      [' ',5,5,5,5,5,5,5,'']
      ]

# introduction
print('\n'*70)
print('Welcome to Nim Game!')
print('There are 4 rows of number 5s as shown below. \n')
print_game_board()
print('The first row has only one 5.')
print('The second row has three 5s.')
print('The third row has five 5s.')
print('The fourth row has seven 5s.')
print()
print('The goal of this game is to eliminate all 5s from this board.')
print('Player 1 and Player 2  will take turn eliminating number 5 from the board.')
print('Each turn, a player can take as many 5s as they want, but only from one row.')
print('THE LAST PLAYER TO ELIMINATE NUMBER 5, WINS!')
print('')
print('On each move, you will be prompt to input the row number you want to eliminate 5s.')
print('Then, you will be prompt to input the amount of 5s you want to eliminate from that row.')
wait = input('Press Enter to start the game!')
print('\n'*100)


# the game starts!!!
player = 1
while True:
    # player make a move
    print_game_board_clear()
    print("Player {}'s turn".format(player))
    row_str  = input('Row number: ')
    try:
        row = int(row_str)
    except ValueError:
        print("Please input integer only.")
        wait = input('Press Enter to try again: ')
        continue
    if row<1 or row>4:
        print('Invalid input')
        wait = input('Press Enter to try again: ')
        continue
    amount_str = input('Amount: ')
    try:
        amount = int(amount_str)
    except ValueError:
        print("Please input integer only.")
        wait = input('Press Enter to try again: ')
        continue
    if invalid_input(game, row, amount):
        print('You can\'t take away {} 5s from row {}.'.format(amount, row))
        wait = input('Press Enter to try again: ')
        continue
    remove(amount,game[row])
    print_game_board_clear()
    print('')
    if game_over():
        print('Player {} Wins!!!'.format(player))
        break
    
    # switch turn
    if player == 1:
        player = 2
    elif player == 2:
        player = 1

print('Thank You For Playing')

# Thank You for coming here to read the code.
# I love and enjoy writing games, that's why i can achieve this.
# This is the first game ever that i've written using programming language.
# I'm looking forward to writing more games like this, or even better than this.
# Finally, I would like to thank my 'Introduction to Programming' teacher, Lior Kadosh, for teaching me Python.

