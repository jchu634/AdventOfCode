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
    permutations = product(["+", "*", "|"], repeat=len(sequence)-1)

    for perm in permutations:
        sum = sequence[0]
        for i, op in enumerate(perm):
            match op:
                case "+":
                    sum += sequence[i+1]
                case "*":
                    sum *= sequence[i+1]
                case "|":
                    sum = int(str(sum) + str(sequence[i+1]))

        if sum == check:
            return True
    return False

# Function written based on entirely wrong reading of the question


def getAppendedPermutations(sequence, check):
    returnList = []
    permutations = product([".", "|"], repeat=len(sequence)-1)

    for perm in permutations:
        a = []
        buffer = ""
        bufferActive = False
        unsuitable = False
        for i, op in enumerate(perm):
            match op:
                case ".":
                    if bufferActive:
                        buffer += str(sequence[i])
                        if int(buffer) > check:
                            unsuitable = True
                            break

                        a.append(int(buffer))
                        bufferActive = False
                        buffer = ""

                    else:
                        a.append(sequence[i])
                case "|":
                    bufferActive = True
                    buffer += str(sequence[i])

        if bufferActive:
            buffer += str(sequence[-1])
            if int(buffer) > check:
                unsuitable = True
            a.append(int(buffer))
        else:
            a.append(int(sequence[-1]))

        if not unsuitable:
            returnList.append(a)

    return returnList


def getAns():
    results = []
    operations = []
    total = 0

    with open("input.txt", "r") as file:
        for line in file.read().splitlines():
            split = line.split(": ")
            results.append(int(split[0]))
            operations.append([int(i) for i in split[1].split(" ")])

    for i, result in tqdm(enumerate(results)):
        if checkSequence(operations[i], result):
            total += result

    return total


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
