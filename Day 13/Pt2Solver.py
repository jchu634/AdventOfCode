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


def generator(bX, b, targetX, bY, targetY):
    while bX * b <= targetX and bY * b <= targetY:
        yield


def calculate(targetX, targetY, aX, aY, bX, bY):

    # targetX = i(aX) + j(bX)
    # targetY = i(aY) + j(bY)

    # targetX-j(bX) = i(aX)
    # targetY-j(bY) = i(aY)

    # targetX(aY)-j(bX)(aY) = i(aX)(aY)
    # targetY(aX)-j(bY)(aX) = i(aY)(aX)

    # targetY(aX)-j(bY)(aX) = targetX(aY)-j(bX)(aY)
    # targetY(aX) - targetX(aY) = j(bY)(aX)-j(bX)(aY)

    j = ((targetY * aX) - (targetX*aY)) / ((bY * aX) - (bX * aY))

    # targetX = i(aX) + j(bX)
    # targetX - j(bX)= i(aX)
    # (targetX - j(bX))/(aX)= i

    i = (targetX - (j*bX))/(aX)

    if (i*aX) + (j*bX) == targetX and (i*aY) + (j*bY) == targetY and (i % 1 == 0 and j % 1 == 0):
        return (i*3) + j
    else:
        return 0


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

        targetX, targetY = [int(x.split("=")[1]) + 10000000000000
                            for x in target[i].split(":")[1].split(", ")]

        # logging.info(f"{targetX}, {targetY}")
        cost = calculate(targetX, targetY, aX, aY, bX, bY)
        totalCost += cost

    return totalCost


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
