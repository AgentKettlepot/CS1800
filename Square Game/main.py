import random

board = []
global player_move 
player_move = True
def num_to_binary(num):
    return bin(num).replace("0b","")

def xor (bin1, bin2):
    xor = bin1 ^ bin2
    return xor

def playerMove(board):
    row = int(input("What row number do you want to remove from? "))
    num = int(input("How many squares do you want to remove? "))
    while num<=0:
        num = int(input("Please input a number greater than 0. How many squares do you want to remove? "))
    while (row > len(board)) or (row <=0):
        row = int(input("Please enter a valid row: "))
        num = int(input("How many squares do you want to remove? "))
    while (num > board[row-1][0]):
        print("ERROR: EXCEEDING NUMBER OF SQUARES")
        row = int(input("What row number do you want to remove from? "))
        num = int(input("How many squares do you want to remove? "))
    board[row-1][0] = board[row-1][0] - num
    global player_move
    player_move = False
    print(board)
    return board

def compMove(board):
    global player_move 
    player_move = True
    nim = board[0][0]
    for i in range(1, len(board)):
        nim = nim ^ board[i][0]
    #print("current nim sum " + str(nim))
    #print("current board: " + str(board))
    if nim==0: # if nim is already 0, just remove the largest row
        ind=0
        max_square=0
        for index in range(len(board)):
            if board[index][0] > max_square:
                max_square = board[index][0]
                ind=index
        print("Computer takes all from row: " + str(ind+1))
        temp_board=[]
        for ind1 in range(len(board)):
            if ind1 == ind:
                temp_board.append([0])
            else:
                temp_board.append([board[ind1][0]])
        #print("New board: " + str(temp_board))
        return temp_board           
        
    else:
        for i in range (len(board)):
            if (board[i][0]^nim) < board[i][0]: 
                print("Computer takes " + str(board[i][0] - board[i][0]^nim) + " from row: " + str(i+1))
                temp_board=[]
                for ind1 in range(len(board)):
                    if ind1 == i:
                        temp_board.append([board[i][0]^nim])
                    else:
                        temp_board.append([board[ind1][0]])
                print("New board: " + str(temp_board))
                return temp_board     

def generateBoard(rows, max_squares):
    for x in range(rows):
        board.append([random.randint(1, max_squares)])
    return board

def drawBoard(board):
    for x in range(len(board)):
        print(str(x+1) + ": ", end="")
        for i in range(board[x][0]):
            print("□", end="")
        print("")

def sumBoard(board):
    total=0
    for x in range(len(board)):
        for i in range(board[x][0]):
            total+=board[x][0]
    return total

def readBoard(file):
    f = open("Tests/"+file, "r")
    for line in (f.readlines() [:-1]):
        board.append([int(line)])

    return board

def test(board):
    drawBoard(board)
    print(board)
    while sumBoard(board) != 0:
        if player_move:
            board = playerMove(board)
            drawBoard(board)
        else:
            board = compMove(board)
            drawBoard(board)
    
    if (player_move):
        print("GAME OVER!! COMPUTER WINS")
    else:
        print("GAME OVER!!! PLAYER WINS")

def main():
    global player_move
    turn = int(input("Input 1 if you want to go first, 2 if you want the opponent to go first. "))
    while turn != 1 and turn != 2:
        turn = int(input("Please input 1 or 2: Input 1 if you want to go first, 2 if you want the opponent to go first. "))
    if (turn==1): 
        player_move = True
    else:
        player_move = False
    option = int(input("Input 1 for file boards and 2 for custom board: "))
    if option != 1 and option != 2:
        option = int(input("Please input 1 or 2: Input 1 for file boards and 2 for custom board: "))
    if option==1:
        file_num = int(input("Input a file number [1-8] to play"))
        print("----------TEST----------")
        board = readBoard("test"+str(file_num)+".txt")
        test(board)
    else:
        rows = int(input("How many rows?"))
        max_squares = int(input("What is the max number of squares per row?"))
        board = generateBoard (rows, max_squares)
        test(board)

main()