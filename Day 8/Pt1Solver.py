from itertools import product
import numpy as np
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


def drawGrid(grid, antiNodes):
    max_height = len(grid)

    grid_with_antinodes = copy.deepcopy(grid)

    for x, y in antiNodes:
        grid_with_antinodes[y][x] = '#'

    for i in range(max_height):
        original_row = ''.join(grid[i])
        modified_row = ''.join(grid_with_antinodes[i])
        logging.info(f"{original_row}    {modified_row}")


def getAns():
    grid = []
    tagged_locations = {}
    locations = set()
    antiNodes = set()
    with open("input.txt", "r") as file:
        grid = [list(i) for i in file.read().splitlines()]

    maxY, maxX = len(grid), len(grid[0])

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != ".":
                locations.add((x, y))
                if grid[y][x] in tagged_locations:
                    tagged_locations[grid[y][x]].append((x, y))
                else:
                    tagged_locations[grid[y][x]] = [(x, y)]

    for key, coords in tagged_locations.items():
        for coord in coords:
            for otherCoord in coords:
                if coord != otherCoord:
                    xDiff = coord[0]-otherCoord[0]
                    yDiff = coord[1]-otherCoord[1]
                    antiNode = (coord[0]+xDiff, coord[1]+yDiff)

                    if (maxX > antiNode[0] >= 0) and (maxY > antiNode[1] >= 0):
                        antiNodes.add(antiNode)

    drawGrid(grid, antiNodes)

    return len(antiNodes)


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
