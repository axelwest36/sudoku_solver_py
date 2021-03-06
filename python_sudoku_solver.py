import numpy as np

grid = [[5, 9, 0, 0, 3, 0, 0, 6, 0],
        [0, 3, 1, 8, 0, 2, 0, 0, 0],
        [8, 6, 0, 5, 9, 0, 0, 3, 1],
        [9, 0, 0, 0, 1, 3, 6, 2, 8],
        [0, 1, 0, 6, 0, 0, 9, 0, 4],
        [0, 0, 0, 9, 0, 0, 7, 1, 0],
        [0, 0, 5, 0, 4, 9, 2, 8, 0],
        [0, 4, 9, 2, 8, 0, 3, 7, 0],
        [2, 8, 6, 3, 7, 0, 0, 0, 0]]

def possible(y, x, n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
   global grid
   for y,x in np.ndindex(9,9):
       if grid[y][x] == 0:
           for n in range(1,10):
               if possible(y,x,n) == True:
                   grid[y][x] = n
                   solve()
                   grid[y][x] = 0
           return                
   print(np.matrix(grid))

solve()
