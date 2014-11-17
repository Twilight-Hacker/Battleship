from random import randint

nrows = int(raw_input("Enter number of board rows: ")) #Board dimensions
ncols = int(raw_input("Enter number of board columns: ")) #Board dimensions
board = []

for x in range(nrows):
    board.append(["O"] * ncols)

def print_board(board):
    for row in board:
        print " ".join(row)

ships = int(raw_input("Enter number of ships:")) #total num of ships

if ships>ncols*nrows:
    ships = ncols*nrows/3
    print "Impossible number selected. Resetting to %d." %ships 

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

recommend = max((nrows*ncols)/(ships*3), ships)
print "We recommend %d turns" %recommend

tturns = int(raw_input("Enter number of turns:")) #total num of turns

if tturns >= ncols*nrows:
    print "Meaningless number of turns. Resetting to recommended"
    tturns = recommend

turns = tturns #number of turns remaining

easy = (ncols*nrows)/(tturns+ships)
if easy > 2:
    print "Difficulty level: Hard"
elif easy > 1:
    print "Difficulty level: Normal"
else:
    print "Difficulty level: Easy"

ship_coord = []
while ships>0:
    ship_row=random_row(board)
    ship_col=random_col(board)
    if not ([ship_row,ship_col]) in ship_coord:
        ship_coord.append([ship_row,ship_col])
        ships -= 1
print "Let's play Battleship!"
print_board(board)

# Everything from here on should go in your for loop!
while turns>0:
    print
    print "Turn: ", (tturns-turns+1), "/", tturns
# Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    guess_row -= 1 #input - index correction
    guess_col -= 1
    print
    
    if [guess_row, guess_col] in ship_coord: #Success
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "D"
        ship_coord.remove([guess_row,guess_col])
        turns -= 1
        if len(ship_coord)==0:
            print "Congratulations. You won."
            turns = -1
        else:
            pass
    else:
        if (guess_row < 0 or guess_row >= nrows) or (guess_col < 0 or guess_col >= ncols):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            turns -= 1
    if turns == 0:
        print "Game Over"
        print "Revealed Board:"
        for i in range(len(ship_coord)):
            if board[ship_coord[i][0]][ship_coord[i][1]]=="O":
                board[ship_coord[i][0]][ship_coord[i][1]]="S"
        # Print (turn + 1) here!
    print_board(board)
