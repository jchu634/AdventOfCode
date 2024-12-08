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
        arr = [list(i) for i in file.read().splitlines()]

    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            if arr[i][j] == "A":
                if (arr[i-1][j-1] == "S" and arr[i+1][j+1] == "M") or (arr[i-1][j-1] == "M" and arr[i+1][j+1] == "S"):
                    if (arr[i-1][j+1] == "S" and arr[i+1][j-1] == "M") or (arr[i-1][j+1] == "M" and arr[i+1][j-1] == "S"):
                        total += 1

    # [(i-1,j-1), (i,j) ,(i-1,j+1)]
    # [(i  ,j-1), (i,j) ,(i  ,j+1)]
    # [(i+1,j-1), (i,j) ,(i+1,j+1)]

    return total


if __name__ == "__main__":

    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
