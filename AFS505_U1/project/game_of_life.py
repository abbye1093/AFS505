from sys import argv

###############################################################################
#                       4. Apply Rules & Make Moves                           #
###############################################################################

def make_move(grid, n_columns, n_rows):
    """Apply the four rules of the game to the current game grid.

    Creates a new_grid to be manipulated by the rules.
    Nested for-loop runs through the rows and columns of a 2D list.
    Each neighbor of the cell of interest is identified and neighbor totals are calculated.
    If statements are used to implement the rules of the game.
    The rules are as follows:
        #1. Any ON cell with fewer than two ON neighbors turns OFF
        #2. Any ON cell with two or three ON neighbours stays ON
        #3. Any ON cell with more than three ON neighbors turns OFF
        #4. Any OFF cell with three ON neighbors turns ON
    new_grid is updated after the rules are applied.

    :param grid: initial grid generated by initialize_grid and translated to appropriate symbols via print_grid
    :type grid: 2D list
    :param n_columns: number of columns in list
    :type n_columns: integer
    :param n_rows: number of rows in list
    :type n_rows: integer
    :return new_grid: updated game grid after rules are implemented
    :type return: 2D list

    """
    # Generate the game grid to be manipulated
    new_grid = [[0] * (n_columns + 1) for i in range(n_rows + 1)]


    for i in range(n_rows):
        for j in range(n_columns):
            upper_left = grid[i-1][j-1] # neighbor to upper left of cell of interest
            upper = grid[i-1][j] # neighbor above cell of interest
            upper_right = grid[i-1][j+1] # neighbor to upper right of cell of interest
            left = grid[i][j-1] # neighbor to left of cell of interest
            right = grid[i][j+1] # neighbor to right of cell of interest
            bot_left = grid[i+1][j-1] # neighbor to bottom left cell of interest
            bot = grid[i+1][j] # neighbor below cell of interest
            bot_right = grid[i+1][j+1] # neighbor to bottom right of cell of interest

            # sum of the state of all neighbors
            on_neighbors = upper_left + upper + upper_right + left + right + bot_left + bot + bot_right

            # Any ON cell with fewer than two ON neighbors turns OFF
            if grid[i][j] == 1 and on_neighbors < 2:
                new_grid[i][j] = 0

            # Any ON cell with two or three ON neighbours stays ON
            elif grid[i][j] == 1 and (on_neighbors == 2 or on_neighbors == 3):
                new_grid[i][j] = 1

            # Any ON cell with more than three ON neighbors turns OFF
            elif grid[i][j] == 1 and on_neighbors > 3:
                new_grid[i][j] = 0

            # Any OFF cell with three ON neighbors turns ON
            elif grid[i][j] == 0 and on_neighbors == 3:
                new_grid[i][j] = 1

    return new_grid #manipulated game grid



###############################################################################
#                           3. Inital Game Settings                           #
###############################################################################

def initialize_grid(argv, grid):
    """Establishes inital grid with user specified coordinates set to "ON".

    Import argv coordinate list, split the coordinates by ':'.
    Convert the strings to integers.
    Apply to game grid.

    :param argv: user imports from command line
    :type argv: string
    :param grid: matrix of ones's and zero's
    :type grid: list
    :return: grid with coordinates

    """
    # Import starting_coor from argv list
    starting_coor = argv[2:]

    # Loop through argv list, split by colon
    # Assign row and col to integers
    # Adjust for expected input
    for i in range(len(starting_coor)):
        row, col = starting_coor[i].split(':')
        row = int(row)
        col = int(col)
        grid[row - 1][col - 1] = 1



###############################################################################
#                           2. Print Game Grid                                #
###############################################################################

def print_grid(n_rows, n_columns, grid):
    """Print the grid with dashes and x's.

    Translate the one's and zero's with dashes and x's. Print to std out.

    :param n_rows: number of rows in grid
    :type n_rows: integer
    :param n_columns: number of columns in grid
    :type n_columns: integer
    :param grid: 2D list of zeros and ones
    :type grid: list
    :return: print grid to std out

    """

    # loop through the grid, print zeros as - and ones as X
    for i in range(n_rows):
        for j in range(n_columns):
            if grid[i][j] == 0:
                print('-', end= '')
            else:
                print('X', end= '')
        print()
    print()



###############################################################################
#                               1. main                                       #
###############################################################################

def main():
    """Function used to control game.

    Create a 2D list of zero's with 30 rows and 80 columns.
    Call initialize_grid to apply the user specified starting "ON" cells.
    Call print_grid to display zero's as '-' and one as 'X'.
    Set the max_iterations of the game to user specified amount, as an integer.
    Loop through max iterations of the game and print each iteration.

    """

    n_rows = 30
    n_columns = 80
    grid = [[0] * (n_columns + 1) for i in range(n_rows + 1)]
    initialize_grid(argv, grid)
    print_grid(n_rows, n_columns, grid)

    max_iterations = int(argv[1]) #argv imports as string, must change to int for count
    loop_count = 0

    while loop_count < max_iterations:
        # print the first grid with user inputs, then print all of the new grids
        if loop_count == 0:
            new_grid = make_move(grid, n_columns, n_rows)
        else:
            new_grid = make_move(new_grid, n_columns, n_rows)
        print_grid(n_rows, n_columns, new_grid)
        loop_count += 1





if __name__ == "__main__":
    main()
