import numpy as np
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


def findTrailHeads(grid):
    trailHeads = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                trailHeads.append((x, y))
    return trailHeads


def get9locations(value, location, grid, maxX, maxY, path: list):
    if value == 9:
        temp = path.copy()
        temp.append(location)
        temp_str = ' -> '.join(map(str, temp))
        return {temp_str}
    locations = set()
    x, y = location

    def check_and_update(dx, dy):
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x <= maxX and 0 <= new_y <= maxY and grid[new_y][new_x] == value + 1:
            temp = path.copy()
            temp.append((new_x, new_y))
            locations.update(get9locations(
                value + 1, (new_x, new_y), grid, maxX, maxY, temp))

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    list(map(lambda d: check_and_update(d[0], d[1]), directions))

    return locations


def getAns():
    grid = []
    total = 0
    with open("input.txt", "r") as file:
        grid = [[int(j) for j in list(i)] for i in file.read().splitlines()]

    # for g in grid:
    #     logging.info(g)
    trailHeads = findTrailHeads(grid)

    maxY = len(grid)-1
    maxX = len(grid[0])-1
    for trailhead in trailHeads:
        temp = len(get9locations(0, trailhead, grid, maxX, maxY, [trailhead]))
        # logging.info(f"{trailhead}: {temp} {
        #              get9locations(0, trailhead, grid, maxX, maxY, [trailhead])}")
        total += temp

    return total


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
