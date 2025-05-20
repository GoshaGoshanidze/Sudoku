import random
import time

print("""
  .-')                _ .-') _               .-. .-')              
 ( OO ).             ( (  OO) )              \  ( OO )             
(_)---\_) ,--. ,--.   \     .'_  .-'),-----. ,--. ,--. ,--. ,--.   
/    _ |  |  | |  |   ,`'--..._)( OO'  .-.  '|  .'   / |  | |  |   
\  :` `.  |  | | .-') |  |  \  '/   |  | |  ||      /, |  | | .-') 
 '..`''.) |  |_|( OO )|  |   ' |\_) |  |\|  ||     ' _)|  |_|( OO )
.-._)   \ |  | | `-' /|  |   / :  \ |  | |  ||  .   \  |  | | `-' /
\       /('  '-'(_.-' |  '--'  /   `'  '-'  '|  |\   \('  '-'(_.-' 
 `-----'   `-----'    `-------'      `-----' `--' '--'  `-----'    
""")

def validation(num, row, column, grid):
    for i in range(9):
        if grid[row][i] == num or grid[i][column] == num:
            return False
    box_x, box_y = row // 3 * 3, column // 3 * 3

    for i in range(3):
        for j in range(3):
            if grid[box_x + i][box_y + j] == num:
                return False
    return True

def fill(grid, row = 0, column = 0):
    if row == 9:
        return True
    if column == 9: 
        return fill(grid, row + 1, 0)
    if grid[row][column] != 0:
        return fill(grid, row, column + 1)
    for num in random.sample(range(1, 10), 9):
        if validation(num, row, column, grid):
            grid[row][column] = num
            if fill(grid, row, column + 1):
                return True
            grid[row][column]
    return False

def generation():
    start_time = time.time()
    while True:
        grid = [[0] * 9 for _ in range(9)]
        if fill(grid):
            return grid
        if time.time() - start_time > 5:
            print("Прошло больше 5 сек.")
            start_time = time.time()

def print_sudoku(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

if __name__ == "__main__":
    board = generation()
    print_sudoku(board)
