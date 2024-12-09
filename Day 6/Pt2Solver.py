import copy
from tqdm import tqdm
import logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


def print_arrays_side_by_side(array1, array2):
    max_height = max(len(array1), len(array2))
    max_width1 = max(len(row) for row in array1)
    max_width2 = max(len(row) for row in array2)
    logging.info("")

    for i in range(max_height):
        row1 = array1[i] if i < len(array1) else [' '] * max_width1
        row2 = array2[i] if i < len(array2) else [' '] * max_width2

        combined_row = ''.join(row1) + '    ' + ''.join(row2)
        logging.info(combined_row)

    input()


def getGuardLocations(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '^':
                return j, i  # y,x


def isStuckinLoop(maze, guardX, guardY):
    direction = 'u'
    locations_visited_granular = set()
    maxY, maxX = len(maze)-1, len(maze[0])-1

    while True:
        # logging.info(f"{guardX}, {guardY}, {
        #              maze[guardY][guardX]}, {direction}"

        match direction:
            case "u":
                if guardY == 0:
                    return False

                if maze[guardY-1][guardX] == "#":
                    direction = 'r'
                else:
                    guardY -= 1
                    if (guardX, guardY, direction) in locations_visited_granular:
                        return True
                    else:
                        locations_visited_granular.add(
                            (guardX, guardY, direction))

            case "r":
                if guardX == maxX:
                    return False

                if maze[guardY][guardX+1] == "#":
                    direction = 'd'
                else:
                    guardX += 1
                    if (guardX, guardY, direction) in locations_visited_granular:
                        return True
                    else:
                        locations_visited_granular.add(
                            (guardX, guardY, direction))

            case "d":
                if guardY == maxY:
                    return False

                if maze[guardY+1][guardX] == "#":
                    direction = 'l'
                else:
                    guardY += 1
                    if (guardX, guardY, direction) in locations_visited_granular:
                        return True
                    else:
                        locations_visited_granular.add(
                            (guardX, guardY, direction))

            case "l":
                if guardX == 0:
                    return False

                if maze[guardY][guardX-1] == "#":
                    direction = 'u'
                else:
                    guardX -= 1
                    if (guardX, guardY, direction) in locations_visited_granular:
                        return True
                    else:
                        locations_visited_granular.add(
                            (guardX, guardY, direction))


def getSolvedGrid(maze, guardX, guardY, ignoreOrigin=False):

    direction = 'u'
    locations_visited = []
    logging.info(getGuardLocations(maze))
    maxY, maxX = len(maze)-1, len(maze[0])-1
    if not ignoreOrigin:
        locations_visited.append((guardX, guardY, direction))

    while True:
        # logging.info(f"{guardX}, {guardY}, {
        #              maze[guardY][guardX]}, {direction}")

        match direction:
            case "u":
                if guardY == 0:
                    return locations_visited

                if maze[guardY-1][guardX] == "#":
                    direction = 'r'
                else:
                    guardY -= 1
                    locations_visited.append((guardX, guardY))

            case "r":
                if guardX == maxX:
                    return locations_visited

                if maze[guardY][guardX+1] == "#":
                    direction = 'd'
                else:
                    guardX += 1
                    locations_visited.append((guardX, guardY))

            case "d":
                if guardY == maxY:
                    return locations_visited

                if maze[guardY+1][guardX] == "#":
                    direction = 'l'
                else:
                    guardY += 1
                    locations_visited.append((guardX, guardY))

            case "l":
                if guardX == 0:
                    return locations_visited

                if maze[guardY][guardX-1] == "#":
                    direction = 'u'
                else:
                    guardX -= 1
                    locations_visited.append((guardX, guardY))


def getAns():
    maze = []
    with open("input.txt", "r") as file:
        for line in file.read().splitlines():
            maze.append(list(line))

    guardX, guardY = getGuardLocations(maze)

    locations = getSolvedGrid(maze, guardX, guardY)
    locations = set(locations)
    logging.info(f"Pt1 Ans: {len(locations)}")

    total = 0

    for location in tqdm(locations):    # Only evaluate places the guard will patrol

        # Needs to be a deep copy and not a shallow copy
        copiedMaze = copy.deepcopy(maze)
        copiedMaze[location[1]][location[0]] = "#"

        isStuck = isStuckinLoop(copiedMaze, guardX, guardY)
        if isStuck:
            total += 1
    return total


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Pt2 Ans: {getAns()}")
