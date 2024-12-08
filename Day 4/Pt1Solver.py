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


def getAns():
    total = 0
    logging.info("test")
    with open("input.txt", "r") as file:
        npArr = np.array(file.read().splitlines())
    total += np.sum(np.char.count(npArr, 'XMAS'))
    total += np.sum(np.char.count(npArr, 'SAMX'))

    splitArr = np.array([list(row) for row in npArr])
    splitArr = np.rot90(splitArr, k=1)
    revertedArr = np.array([''.join(row) for row in splitArr])
    total += np.sum(np.char.count(revertedArr, 'XMAS'))
    total += np.sum(np.char.count(revertedArr, 'SAMX'))

    diagonals = [splitArr.diagonal(
        i) for i in range(-splitArr.shape[0]+1, splitArr.shape[1])]
    diagonals += [np.fliplr(splitArr).diagonal(i)
                  for i in range(-splitArr.shape[0]+1, splitArr.shape[1])]
    diagonal_strings = [''.join(diag) for diag in diagonals]

    total += sum(s.count('XMAS') for s in diagonal_strings)
    total += sum(s.count('SAMX') for s in diagonal_strings)

    return total


if __name__ == "__main__":

    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
