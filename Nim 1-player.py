import time

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

# the player make a move = {list:row number , n:amount}
# remove n number of 5s from list (from that row)
def remove(n,list):
    for i in range(n):
        for i in list:
            if i==5:
                list[list.index(5)]=0
                break

# convert n (n = amount of 5s in a row) to binary representation of that row
def conv(n):
    if n==0:
        return [0,0,0]
    if n==1:
        return [0,0,1]
    if n==2:
        return [0,1,0]
    if n==3:
        return [0,1,1]
    if n==4:
        return [1,0,0]
    if n==5:
        return [1,0,1]
    if n==6:
        return [1,1,0]
    if n==7:
        return [1,1,1]

# Computer's decision:
def ai_move():
    # l1 is the binary representation of row1 in the current game board.
    l1=conv(game[1].count(5))
    l2=conv(game[2].count(5))
    l3=conv(game[3].count(5))
    l4=conv(game[4].count(5))
    # l_list is the represenation of current game situation in binary.
    # "l_list" is a binary version of "game".
    l_list = [l1,l2,l3,l4]
    # nim_sum is used for evaluating strategy of computer's move to always win.
    nim_sum = [int((l1[0]+l2[0]+l3[0]+l4[0])%2),
               int((l1[1]+l2[1]+l3[1]+l4[1])%2),
               int((l1[2]+l2[2]+l3[2]+l4[2])%2)]
# possible list of nim_sum are: {[0,0,0],[0,0,1],[0,1,0],[1,0,0],
#                                [0,1,1],[1,0,1],[1,1,0],[1,1,1]}
# based on the result of nim_sum calculated above,
#   the row number and amount of 5s to be removed by computer is generated.
# ai = {'row':row number in the game board, 'amount':amount of 5s to be removed from that row}
# This strategy is derived from youtube and other website.
# I understand the strategy clearly, then turn it into codes.
    if nim_sum == [0,0,0]:
        lk=0
        for row in game:
            if 5 in row:
                ai['amount'] = 1
                ai['row'] = lk
                return
            lk+=1
                
    if nim_sum == [0,0,1]:
        lk=1
        for l in l_list:
            if l[2] == 1:
                ai['amount'] = 1
                ai['row'] = lk
                return
            lk+=1

    if nim_sum == [0,1,0]:
        lk=1
        for l in l_list:
            if l[1] == 1:
                ai['amount'] = 2
                ai['row'] = lk
                return 
            lk+=1

    if nim_sum == [1,0,0]:
        lk=1
        for l in l_list:
            if l[0] == 1:
                ai['amount'] = 4
                ai['row'] = lk
                return
            lk+=1

    if nim_sum == [0,1,1]:
        lk=1
        for l in l_list:
            if l[1] == 1:
                if l[2] == 1:
                    ai['amount'] = 3
                    ai['row'] = lk
                    return
                else:
                    ai['amount'] = 1
                    ai['row'] = lk
                    return
            lk+=1

    if nim_sum == [1,0,1]:
        lk=1
        for l in l_list:
            if l[0] == 1:
                if l[2] == 1:
                    ai['amount'] = 5
                    ai['row'] = lk
                    return
                else:
                    ai['amount'] = 3
                    ai['row'] = lk
                    return 
            lk+=1

    if nim_sum == [1,1,0]:
        lk=1
        for l in l_list:
            if l[0] == 1:
                if l[1] == 1:
                    ai['amount'] = 6
                    ai['row'] = lk
                    return
                else:
                    ai['amount'] = 2
                    ai['row'] = lk
                    return
            lk+=1

    if nim_sum == [1,1,1]:
        lk=1
        for l in l_list:
            if l[0] == 1:
                if l[1] == 1:
                    if l[2] == 1:
                        ai['amount'] = 7
                        ai['row'] = lk
                        return
                    else:
                        ai['amount'] = 5
                        ai['row'] = lk
                        return
                else:
                    if l[2] == 1:
                        ai['amount'] = 3
                        ai['row'] = lk
                        return
                    else:
                        ai['amount'] = 1
                        ai['row'] = lk
                        return
            lk+=1

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
    # put every items in every rows into one list.
    items_in_game = []
    for i in range(len(game)):
        items_in_game.extend(game[i])
    if 5 not in items_in_game:
        return True





# START THE GAME!!!
# game = a list containing each row of the game board.
game=[
      ['       The nim game       '],
      ['          ',5,'         '],
      ['       ',5,5,5,'      '],
      ['    ',5,5,5,5,5,'   '],
      [' ',5,5,5,5,5,5,5,'']
      ]
# ai = artificial intelligence = computer
# ai dictionary = temporary ai's move.
ai={'amount':0, 'row':0}

# introduction
print('\n'*70)
print('Welcome to Nim Game!')
print('There are 4 rows of number 5s as shown below.')
print_game_board()
print('The first row has only one 5.')
print('The second row has three 5s.')
print('The third row has five 5s.')
print('The fourth row has seven 5s.')
print()
print('The goal of this game is to eliminate all 5s from this board.')
print('You and computer will take turn eliminating number 5 from the board.')
print('Each turn, a player can take as many 5s as they want, but only from one row.')
print('THE LAST PLAYER TO ELIMINATE NUMBER 5, WINS!')
print('')
print('First, you will be prompt to input the row number you want to eliminate 5s.')
print('Then, you will be prompt to input the amount of 5s you want to eliminate from that row.')
wait = input('Press Enter to start the game!')

print_game_board_clear()
go_first = input("Will you go first?(Y/N): ")

if go_first.lower() not in 'n, no, no!, not, nope, no thanks, no need, never':
    # player goes first.
    while True:
    #player's turn
        print_game_board_clear()
        print("Your turn")
        row_str  = input('Row number: ')
        try:
            row = int(row_str)
        except ValueError:
            print('Please input an integer.')
            wait = input('Press Enter to try again: ')
            continue
        if row<1 or row>4:
            print('Invalid input')
            wait = input('Press Enter to try again: ')
            continue
        amount_str = input('    Amount: ')
        try:
            amount = int(amount_str)
        except ValueError:
            print('Please input an integer.')
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
            print('You Win!!!')
            break

    #computer's turn
        print('Computer is thinking...')
        time.sleep(1.5)
        ai_move()
        print_game_board_clear()
        print('Computer will eliminate:\nRow number: {}\n    Amount: {}'.format(ai['row'],ai['amount']))
        wait = input('Press Enter to continue ')
        remove(ai['amount'],game[ai['row']])
        print_game_board_clear()
        if game_over():
            print('You Lose')
            break
else:
    #computer goes first
    #computer's turn
    print_game_board_clear()
    print('')
    print('Computer is thinking...')
    time.sleep(1.5)
    ai_move()
    print_game_board_clear()
    print('Computer will eliminate:\nRow number: {}\n    Amount: {}'.format(ai['row'],ai['amount']))
    wait = input('Press Enter to continue ')
    remove(ai['amount'],game[ai['row']])
    
    while True:
    #player's turn
        print_game_board_clear()
        print("Your turn")
        row_str  = input('Row number: ')
        try:
            row = int(row_str)
        except ValueError:
            print('Please input an integer.')
            wait = input('Press Enter to try again: ')
            continue
        if row<1 or row>4:
            print('Invalid input')
            wait = input('Press Enter to try again: ')
            continue
        amount_str = input('    Amount: ')
        try:
            amount = int(amount_str)
        except ValueError:
            print('Please input an integer.')
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
            print('You Win!!!')
            break

    #computer's turn
        print('Computer is thinking...')
        time.sleep(1.5)
        ai_move()
        print_game_board_clear()
        print('Computer will eliminate:\nRow number: {}\n    Amount: {}'.format(ai['row'],ai['amount']))
        wait = input('Press Enter to continue ')
        remove(ai['amount'],game[ai['row']])
        print_game_board_clear()
        if game_over():
            print('You Lose')
            break
        

print('Thank You For Playing')
