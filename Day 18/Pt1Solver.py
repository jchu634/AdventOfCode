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


def getAns(noOfBytes, gridSize):
    with open("input.txt", "r") as file:
        drops = [[int(j) for j in i.split(",")] for i in file.read().splitlines()]
    grid = [["." for i in range(gridSize+1)] for j in range(gridSize+1)]
    # logging.info(grid)
    count = 0
    for i in range(noOfBytes):
        grid[drops[i][1]][drops[i][0]] = "#"
        count += 1

    aStarGrid = [[0 if j == "#" else 1 for j in list(i)] for i in grid]
    start = [0, 0]
    dest = [gridSize, gridSize]
    # printGrid(aStarGrid)

    return a_star_search(aStarGrid, start, dest)


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns(3014, 70)}")
