import sys
import numpy as np
from tqdm import tqdm
import logging
import re
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


def getAns():
    with open("test.txt", "r") as file:
        fileIn = file.read().splitlines()
    regex = fileIn.pop(0).split(", ")
    fileIn.pop(0)
    pattern = f"^({'|'.join(map(re.escape, regex))})+$"
    counter = 0
    for combo in fileIn:
        if re.fullmatch(pattern, combo) is not None:
            counter += 1
            logging.info(combo)
    return counter


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
