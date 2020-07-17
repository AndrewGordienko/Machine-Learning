board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Helps us find empty coordinates on the board in the form of 0
def empty_coords(board):
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            if board[i][j] == 0:
                return (i, j)
    return None

# Function to check if our number works
def validation(board, position, number):
    var1, var2 = position #row, col
    
    # Checking the row
    for i in range(len(board[0])):
        if board[var1][i] == number:
            return False
        
    # Checking the column
    for i in range(len(board)):
        if board[i][var2] == number:
            return False
        
    # Checking the square
    box_x_coord = var2 // 3
    box_y_coord = var1 // 3
    for i in range(box_x_coord*3, box_x_coord*3 + 3):
        for j in range(box_y_coord*3, box_y_coord*3 + 3):
            if board[j][i] == number:
                return False
            
    return True

def solve(board):
    if not empty_coords(board): # Everything is filled up and we are good to go
        return True
    else:
        row, col = empty_coords(board) # Let the battle begin!
    
    for i in range(1, 10): # Check every possible number
        if validation(board, (row, col), i) == True: # If the number works :)
            board[row][col] = i # Set the number as the one we just found
            if solve(board): # Go on to complete this loop again
                return True
            else:
                board[row][col] = 0 # Reset it

    return False

def print_board(board): # Formatting to make it look pretty 
    for i in range(len(board)):
        if i % 3 == 0 and i != 0: # By row
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])): # By column
            if j % 3 == 0 and j != 0: #using modulo to find exact division 
                print(" | ", end="") #the "end" makes sure we move to a new line

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

solve(board)
print_board(board)
