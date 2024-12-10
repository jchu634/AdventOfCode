from itertools import product
import numpy as np
import copy
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


def checkSequence(sequence, check):
    permutations = product(["+", "*"], repeat=len(sequence)-1)

    for perm in permutations:
        sum = sequence[0]
        for i, op in enumerate(perm):
            match op:
                case "+":
                    sum += sequence[i+1]
                case "*":
                    sum *= sequence[i+1]
        if sum == check:
            return check
    return 0


def getAns():
    results = []
    operations = []
    total = 0

    with open("input.txt", "r") as file:
        for line in file.read().splitlines():
            split = line.split(": ")
            results.append(int(split[0]))
            operations.append([int(i) for i in split[1].split(" ")])

    for i, result in enumerate(results):
        total += checkSequence(operations[i], result)

    return total


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
