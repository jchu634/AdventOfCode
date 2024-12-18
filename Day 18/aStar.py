import math
import heapq
import logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


class Cell:
    def __init__(self):
        self.f = float('inf')
        self.g = float('inf')
        self.h = float('inf')
        self.parent_i = -1
        self.parent_j = -1


def is_valid(row, col, ROW, COL):
    return 0 <= row < ROW and 0 <= col < COL


def is_unblocked(grid, row, col):
    return grid[row][col] == 1


def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]


def calculate_h_value(row, col, dest):
    return abs(row - dest[0]) + abs(col - dest[1])

# Trace the path from source to destination


def trace_path(grid, cell_details, dest):
    print("The Path is ")
    path = []
    row = dest[0]
    col = dest[1]

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    # Add the source cell to the path
    path.append((row, col))
    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    for i in path:
        print("->", i, end=" ")
    print()

    # Print the solution grid
    print_solution_grid(grid, path)


# Print the solution grid

def print_solution_grid(grid, path):
    solution_grid = [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                solution_grid[row][col] = '#'
            else:
                solution_grid[row][col] = '.'

    for (row, col) in path:
        solution_grid[row][col] = 'P'

    logging.info(list(set(path)))
    logging.info(path)
    logging.info(list(set(path)) == path)
    logging.info(len(set(path)) == len(path))
    solution_grid[path[0][0]][path[0][1]] = 'S'  # Start
    solution_grid[path[-1][0]][path[-1][1]] = 'D'  # Destination

    for row in solution_grid:
        logging.info(' '.join(row))

# Implement the A* search algorithm


def a_star_search(grid, src, dest, print=False):
    ROW = len(grid)
    COL = len(grid[0])

    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        logging.error("Source or the destination is blocked")
        return -1

    # Check if we are already at the destination
    if is_destination(src[0], src[1], dest):
        logging.info("We are already at the destination")
        return 0

    # Initialize the closed list (visited cells)
    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    # Initialize the details of each cell
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    # Initialize the start cell details
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j
    cell_details[i][j].direction = None  # No direction at the start

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        # For each direction, check the successors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]
            new_direction = dir

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_i, new_j, ROW, COL) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                # If the successor is the destination
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    cell_details[new_i][new_j].direction = new_direction
                    cell_details[new_i][new_j].g = cell_details[i][j].g + 1.0
                    # logging.info("The destination cell is found")
                    # Trace and print the path from source to destination
                    if print:
                        trace_path(grid, cell_details, dest)
                    found_dest = True
                    return cell_details[new_i][new_j].g
                else:
                    # Calculate the new f, g, and h values
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        # Update the cell details
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j

    # If the destination is not found after visiting all cells
    if not found_dest:
        logging.error("Failed to find the destination cell")
        return -1
