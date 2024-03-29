# left shift + click to set the starting spot - only 1!
# left shift + click on a starting spot already selected to remove it
# left control + click to set end spot - same double click feature
# regular click to set wall
# hit space bar to let it run
# need to tidy the code up still

import numpy as np
import pygame
import math
from itertools import product

DIMENSION = 50
WIDTH = 500
HEIGHT = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

COST = 1
START_NUMBER = 1
END_NUMBER = 2
WALL = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
board = np.zeros((DIMENSION, DIMENSION))

placeholder = 0
enter_toggle = 0

class Node():
    def __init__(self, parent_node):
        self.g_cost = None
        self.f_cost = None
        self.h_cost = None

        self.x_coordinate, self.y_coordinate = None, None
        self.parent_node = parent_node
        """
        def __eq__(self, other):
            return self.position == other.position
        def __lt__(self, other):
            return self.f < other.f
        """


def finding_position(arr, number):
    for i in range(len(arr[0])):
        for j in range(len(arr[0])):
            if arr[i][j] == number:
                return j, i
    
    return None, None

def a_star():
    step_counter = 0
    starting_node = Node(None)
    starting_node.g_cost = starting_node.f_cost = starting_node.h_cost = 0
    starting_node.x_coordinate, starting_node.y_coordinate = STARTING_COORDINATE_X, STARTING_COORDINATE_Y
    nodes_not_visited = []
    nodes_visited = []

    nodes_not_visited.append(starting_node)

    while True:
        step_counter += 1
        value = float("inf")
        for i in range(len(nodes_not_visited)):
            if nodes_not_visited[i].f_cost <= value:
                value = nodes_not_visited[i].f_cost
                current = nodes_not_visited[i]
                temp = i
        
        nodes_not_visited.pop(temp)
        nodes_visited.append(current)
        
        temp_list = []
        for a_node in nodes_visited:
            value = 0
            for i in range(len(temp_list)):
                if temp_list[i].x_coordinate == a_node.x_coordinate and temp_list[i].y_coordinate == a_node.y_coordinate:
                    value = 1
            if value == 0:
                temp_list.append(a_node)
        
        nodes_visited = temp_list

        print(current.x_coordinate, current.y_coordinate)

        if (current.x_coordinate, current.y_coordinate) == (ENDING_COORDINATE_X, ENDING_COORDINATE_Y):
            print("end")
            break
            
        children = []
        for vec in product([-1, 0, 1], repeat=2):
            if not any(vec):
                continue

            search_x, search_y = current.x_coordinate + vec[1], current.y_coordinate + vec[0]
            if search_x >= WIDTH/DIMENSION or search_x < 0 or search_y >= HEIGHT/DIMENSION or search_y < 0: 
                continue
            # 1 is wall, 2 is start
            if board[search_y][search_x] != 1:
                new_node = Node(current)
                new_node.x_coordinate, new_node.y_coordinate = search_x, search_y
                children.append(new_node)
        
        for child in (children):
            for closed_child in range(len(nodes_visited)):
                if child == nodes_visited[closed_child]:
                    break
            else:
                child.g_cost = current.g_cost + COST
                child.h_cost = abs(child.y_coordinate - ENDING_COORDINATE_Y) + abs(child.x_coordinate - ENDING_COORDINATE_X)
                child.f_cost = child.g_cost + child.h_cost

                for open_node in range(len(nodes_not_visited)):
                    if child == nodes_not_visited[open_node] and child.g_cost >= nodes_not_visited[open_node].g_cost:
                        break
                else:
                    nodes_not_visited.append(child)

                    temp_list = []
                    for a_node in nodes_not_visited:
                        value = 0
                        for i in range(len(temp_list)):
                            if temp_list[i].x_coordinate == a_node.x_coordinate and temp_list[i].y_coordinate == a_node.y_coordinate:
                                value = 1
                        if value == 0:
                            temp_list.append(a_node)
                    
                    nodes_not_visited = temp_list

    path = []
    while current.parent_node != None:
        path.append((current.x_coordinate, current.y_coordinate))
        current = current.parent_node

    path.pop(0)
    print(path)


    for i in range(len(path)):
        board[path[i][1]][path[i][0]] = 4
        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if enter_toggle != 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    placeholder = 1
                
                if event.key == pygame.K_LCTRL:
                    placeholder = 2

                if event.key == pygame.K_SPACE:
                    enter_toggle = 1
                    
                    for row in range(DIMENSION):
                        for column in range(DIMENSION):
                            if board[row][column] == 2:
                                # this is all the set up code
                            
                                x_start, y_start = column, row
                            
                            if board[row][column] == 3:
                                # this is the end spot
                                x_end, y_end = column, row
                    
                    # set up code should be here
                    STARTING_COORDINATE_X, STARTING_COORDINATE_Y = finding_position(board, 2)
                    ENDING_COORDINATE_X, ENDING_COORDINATE_Y = finding_position(board, 3)

                    board[STARTING_COORDINATE_Y][STARTING_COORDINATE_X] = 0
                    board[ENDING_COORDINATE_Y][ENDING_COORDINATE_X] = 0

                    a_star()

                    board[STARTING_COORDINATE_Y][STARTING_COORDINATE_X] = 2
                    board[ENDING_COORDINATE_Y][ENDING_COORDINATE_X] = 3
                
            if event.type == pygame.KEYUP:
                placeholder = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x, y = math.floor(x/DIMENSION), math.floor(y/DIMENSION)

                if placeholder == 1:
                    # start
                    if board[x][y] == 0:
                        board[x][y] = 2
                    else:
                        board[x][y] = 0
                
                if placeholder == 2:
                    # end
                    if board[x][y] != 3:
                        board[x][y] = 3
                    else:
                        board[x][y] = 0
                
                if placeholder == 0:
                    # wall
                    if board[x][y] == 0:
                        board[x][y] = 1
                    else:
                        board[x][y] = 0

    screen.fill(WHITE)

    for row in range(DIMENSION):
        for column in range(DIMENSION):
            if board[row][column] == 0:
                # empty spot
                pygame.draw.rect(screen, BLACK, (DIMENSION * row, DIMENSION * column, 50, 50), 1)

            if board[row][column] == 1:
                # wall
                pygame.draw.rect(screen, BLACK, (DIMENSION * row, DIMENSION * column, 50, 50))

            if board[row][column] == 2:
                # start
                pygame.draw.rect(screen, GREEN, (DIMENSION * row, DIMENSION * column, 50, 50))
                pygame.draw.rect(screen, BLACK, (DIMENSION * row, DIMENSION * column, 50, 50), 1)

            if board[row][column] == 3:
                # end
                pygame.draw.rect(screen, RED, (DIMENSION * row, DIMENSION * column, 50, 50))
                pygame.draw.rect(screen, BLACK, (DIMENSION * row, DIMENSION * column, 50, 50), 1)
            
            if board[row][column] == 4:
                # path solved
                pygame.draw.rect(screen, BLUE, (DIMENSION * row, DIMENSION * column, 50, 50))
                pygame.draw.rect(screen, BLACK, (DIMENSION * row, DIMENSION * column, 50, 50), 1)

    pygame.display.flip()
