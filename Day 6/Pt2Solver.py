from tqdm import tqdm
import time
import numpy as np
import re
import logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


def printGrid(arr):
    for i in range(len(arr)):
        logging.info(arr[i])


def rotateArr(arr, rotations):
    splitArr = np.array([list(row) for row in arr])
    splitArr = np.rot90(splitArr, k=rotations)
    return np.array([''.join(row) for row in splitArr])


def countX(arr):
    total = 0
    for row in arr:
        total += row.count("X")
    return total


def isStuckinLoop(npArr):
    iterations = 1
    while True:
        npArr = rotateArr(npArr, 3)
        for i, row in enumerate(npArr):
            if '^' in list(row):
                newRowSplit = row.split("^")
                newRow = newRowSplit[0] + "X"  # + newRow[1].replace(".", "X")
                try:
                    index = newRowSplit[1].index("#")
                    newRowSplitSplit = newRowSplit[1].split('#', 1)
                    newRow += "".join(list(newRowSplitSplit[0].replace(".", "X"))[
                        :-1]) + "^#" + newRowSplitSplit[1]
                    npArr[i] = newRow
                except ValueError:
                    # There is no #: i.e. guard exits
                    return False

                break
        while True:
            iterations += 1
            if iterations % 1000 == 0:
                logging.error(f"High iterations:{iterations}")
            npArr = rotateArr(npArr, 1)

            for i, row in enumerate(npArr):
                if '^' in list(row):
                    newRowSplit = row.split("^")
                    newRow = newRowSplit[0] + "X"
                    try:
                        index = newRowSplit[1].index("#")
                        newRowSplitSplit = newRowSplit[1].split('#', 1)
                        # logging.info(newRowSplitSplit[0])
                        if '' == newRowSplitSplit[0]:
                            return False
                        elif '.' not in newRowSplitSplit[0]:
                            return True
                        newRow += "".join(list(newRowSplitSplit[0].replace(".", "X"))[
                            :-1]) + "^#" + newRowSplitSplit[1]
                        npArr[i] = newRow
                    except ValueError:
                        # There is no #: i.e. guard exits
                        return False

                    break
        printGrid(npArr)


def getAns():
    with open("input.txt", "r") as file:
        npArr = np.array(file.read().splitlines())

    total = 0
    for i in tqdm(range(len(npArr))):
        for j in range(len(npArr[i])):
            copiedArr = npArr.copy()
            if list(copiedArr[i])[j] == ".":
                copiedString = copiedArr[i]
                copiedArr[i] = copiedString[:j] + "#" + copiedString[j+1:]
                isStuck = isStuckinLoop(copiedArr)
                if isStuck:
                    total += 1
                    copiedArr = npArr.copy()
                    copiedString = copiedArr[i]
                    copiedArr[i] = copiedString[:j] + "O" + copiedString[j+1:]

                    # printGrid(copiedArr)
                    # logging.info("")
    return total


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
