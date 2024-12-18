import sys
import numpy as np
from tqdm import tqdm
import logging
from aStar import a_star_search
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


def chunkify(lst, n):
    return [lst[i::n] for i in range(n)]


def printGrid(grid):
    for g in grid:
        logging.info("".join(g))


def generator():
    while True:
        yield


def print_progress(iteration):
    sys.stdout.write(f"\rCurrent iteration: {iteration}")
    sys.stdout.flush()


def getAns(gridSize):
    with open("input.txt", "r") as file:
        drops = [[int(j) for j in i.split(",")] for i in file.read().splitlines()]
    grid = [["." for i in range(gridSize+1)] for j in range(gridSize+1)]
    # logging.info(grid)

    for i in range(1024):
        grid[drops[i][1]][drops[i][0]] = "#"

    print(len(drops))
    i = 2500
    aStarGrid = [[0 if j == "#" else 1 for j in list(i)] for i in grid]
    while True:
        print_progress(i)  # Print the current iteration
        start = [0, 0]
        dest = [gridSize, gridSize]
        res = a_star_search(aStarGrid, start, dest)
        if res == -1:
            aStarGrid[drops[i][1]][drops[i][0]] = 1
            a_star_search(aStarGrid, start, dest, print=True)

            return drops[i]
        else:
            i += 1
            aStarGrid[drops[i][1]][drops[i][0]] = 0


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns(70)}")
