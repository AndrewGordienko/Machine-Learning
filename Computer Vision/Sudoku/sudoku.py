board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

def empty_coords(board):
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            if board[i][j] == 0:
                return (i, j)
    return None

def validation(board, position, number):
    var1, var2 = position #row, col

    #row
    for i in range(len(board[0])):
        if board[var1][i] == number:
            return False

    #col
    for i in range(len(board)):
        if board[i][var2] == number:
            return False

    #square
    box_x_coord = var2 // 3
    box_y_coord = var1 // 3

    for i in range(box_x_coord*3, box_x_coord*3 + 3):
        for j in range(box_y_coord*3, box_y_coord*3 + 3):
            if board[j][i] == number:
                return False

    
    return True

def solve(board):
    if not empty_coords(board):
        return True
    else:
        row, col = empty_coords(board)
    
    for i in range(1, 10):
        if validation(board, (row, col), i) == True:
            board[row][col] = i
            if solve(board):
                return True
            else:
                board[row][col] = 0

    return False

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0: #using modulo to find exact division 
                print(" | ", end="") #the "end" makes sure we move to a new line

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

solve(board)
print_board(board)