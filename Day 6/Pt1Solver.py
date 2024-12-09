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


def getAns():
    with open("input.txt", "r") as file:
        npArr = np.array(file.read().splitlines())
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
                    newRowSplitSplit = newRowSplit[1].split('^', 1)
                    newRow += "".join(list(newRowSplitSplit[0].replace(
                        ".", "X"))) + "^" + newRowSplitSplit[1]
                    npArr[i] = newRow

                    return countX(npArr)

                break
        while True:
            npArr = rotateArr(npArr, 1)

            for i, row in enumerate(npArr):
                if '^' in list(row):
                    newRowSplit = row.split("^")
                    newRow = newRowSplit[0] + "X"
                    try:
                        index = newRowSplit[1].index("#")
                        newRowSplitSplit = newRowSplit[1].split('#', 1)
                        newRow += "".join(list(newRowSplitSplit[0].replace(".", "X"))[
                            :-1]) + "^#" + newRowSplitSplit[1]
                        npArr[i] = newRow
                    except ValueError:
                        # There is no #: i.e. guard exits
                        newRow += newRowSplit[1].replace(".", "X")
                        npArr[i] = newRow
                        return countX(npArr)

                    break
        printGrid(npArr)


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
