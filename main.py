import pygame
import sys
import random
import math

BLACK = (0, 0, 0) # background
WHITE = (210, 140, 247) #foreground
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
grid = [] # 2d array that holds the current state of the board
BLOCK_SIZE = 2 #Set the size of the grid block

CONVOLUTION_MATRIX = [[-0.335, -0.588, -0.624],[0.548, -0.125, 0.965],[0.395,-0.786, 0.987]]


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    initGrid()
    drawGrid()
    while True:
        updateGrid(grid)
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def updateGrid(grid):
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid)-1):
            a = grid[i-1][j-1]
            b = grid[i-1][j]
            c = grid[i-1][j+1]
            d = grid[i][j-1]
            me = grid[i][j]
            e = grid[i][j+1]
            f = grid[i+1][j-1]
            g = grid[i+1][j]
            h = grid[i+1][j+1]

            hood = [[a, b, c],[d, me, e],[f, g, h]]
            result = math.sin(round(dotProduct(hood), 3)) #sine function used as activation

            #clipping output from 0 to 1
            if (result > 1):
                result = 0
            else:
                result = max(0, result) # return 0 if result negative, else return result

            grid[i][j] = result



def fillSquare(x, y):
    rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE) 
    pygame.draw.rect(SCREEN, WHITE, rect)


def dotProduct(a):
    result = 0
    for i in range(3):
        for j in range(3):
            result += CONVOLUTION_MATRIX[i][j] * a[i][j]
    return result

def initGrid(): #creates a state of the board as a 2d array
    loopcount = int(WINDOW_HEIGHT/10)
    for x in range(loopcount):
        new = []
        for y in range(loopcount):
            choice = random.randrange(0, 100)/100
            new.append(choice)
        grid.append(new) 

def drawGrid(): #draws grid as stored in the grid 2d array
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            choice = grid[int(x/10)][int(y/10)]
            newColor = tuple(elem_1 * choice for elem_1 in WHITE)
            pygame.draw.rect(SCREEN, newColor, rect)

if __name__ == "__main__":
    main()