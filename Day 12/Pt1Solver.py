import sys
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


def calculate_min_cost(targetX, targetY, aX, aY, bX, bY):
    minCost = sys.maxsize
    bestCombination = None

    for a in range(1, 101):
        for b in range(1, 101):
            x = a * aX + b * bX
            y = a * aY + b * bY
            cost = a * 3 + b

            if x == targetX and y == targetY and cost < minCost:
                minCost = cost
                bestCombination = (a, b)

    return bestCombination, minCost


def chunkify(lst, n):
    return [lst[i::n] for i in range(n)]


def getAns():
    with open("input.txt", "r") as file:
        aData, bData, target, discard = chunkify(file.read().splitlines(), 4)

    totalCost = 0
    for i in range(len(aData)):

        aX, aY = [int(x.split("+")[1])
                  for x in aData[i].split(":")[1].split(", ")]
        bX, bY = [int(x.split("+")[1])
                  for x in bData[i].split(":")[1].split(", ")]
        bX, bY = [int(x.split("+")[1])
                  for x in bData[i].split(":")[1].split(", ")]

        targetX, targetY = [int(x.split("=")[1])
                            for x in target[i].split(":")[1].split(", ")]

        # logging.info(f"{targetX}, {targetY}")
        bestCombination, minCost = calculate_min_cost(
            targetX, targetY, aX, aY, bX, bY)
        if minCost != sys.maxsize:

            # logging.info(f"Best combination: {bestCombination} with cost: {minCost}")
            totalCost += minCost
        else:
            # logging.info(f"No combination found")
            pass
    return totalCost


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
