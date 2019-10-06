board=["  "for i in range(9)]
lastSymbol=""
number =1;

print("Welcome to Tic-Tac-Toe Game Created By Sanket Singh!!!!");
def print_board():
   # global lastSymbol
    row1 = "| {} | {} | {} |".format(board[0],board[1],board[2])
    row2 = "| {} | {} | {} |".format(board[3],board[4],board[5])
    row3 = "| {} | {} | {} |".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

print_board()

def  player_move(choice):
    global lastSymbol
    global number
    preserveSymbol = lastSymbol
    preserverNumber = number
   # print_board()
    if lastSymbol == "" or lastSymbol == "O" :
        lastSymbol="X"
        number = 2
    elif lastSymbol=="X":
        lastSymbol="O"
        number =1
    if board[choice-1]!= "  ":
        #print(lastSymbol)
        print("Space is taken")
        lastSymbol = preserveSymbol
        number=preserverNumber

    board[choice-1] = lastSymbol
    print_board()
    return victoryDecider(lastSymbol,preserverNumber)

def  victoryDecider(lastSymbol,preserverNumber):    
    if (lastSymbol in board [0] and lastSymbol in board[1] and lastSymbol in board [2]) or \
       (lastSymbol in board [3] and lastSymbol in board[4] and lastSymbol in board [5]) or \
       (lastSymbol in board [6] and lastSymbol in board[7] and lastSymbol in board [8]) or \
       (lastSymbol in board [0] and lastSymbol in board[3] and lastSymbol in board [6]) or \
       (lastSymbol in board [1] and lastSymbol in board[4] and lastSymbol in board [7]) or \
       (lastSymbol in board [2] and lastSymbol in board[5] and lastSymbol in board [8]) or \
       (lastSymbol in board [0] and lastSymbol in board[4] and lastSymbol in board [8]) or \
       (lastSymbol in board [2] and lastSymbol in board[4] and lastSymbol in board [6]) :
        print("Congratulation :")
        print("Player {} with Symbol {} wins the Game  ".format(preserverNumber,lastSymbol))
        return True;
    elif "  " in board:
        return False;
    else:
        print("Game is Draw!!!")
        return True;
       


while True:
    print("Your turn Player {}".format(number))
    try:
        choice = int(input("Entre Number between (1-9): ").strip())
        if not(choice>=0 and choice <=9):
            print("Not a valid input please enter number between 1-9")
            continue;
    except ValueError :
        print("That's not a Number!")
        print("Not a valid input please enter number between 1-9")
        continue;

    if (player_move(choice)):
        break
    else:
        continue

