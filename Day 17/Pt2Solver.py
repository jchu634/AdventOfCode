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


def programLoop(a):
    output = []
    while True:
        b = a % 8
        b = b ^ 4
        c = a // (2**b)
        b = b ^ c
        b = b ^ 4
        output.append(b % 8)
        a = a // 8
        if a == 0:
            return output


def getAns():
    with open("input.txt", "r") as file:
        regA, regB, regC, _, Program = file.read().splitlines()

    # regA = int(regA.split(": ")[1])
    # regB = int(regB.split(": ")[1])
    # regC = int(regC.split(": ")[1])
    Program = [int(i) for i in Program.split(": ")[1].split(",")]

    possibleCombinations = [0]  # Inti
    for i in range(1, len(Program)+1):
        newCombinations = []
        for com in possibleCombinations:
            for offset in range(8):
                a = 8 * com + offset
                if programLoop(a) == Program[-i:]:
                    newCombinations.append(a)
        possibleCombinations = newCombinations

    return min(possibleCombinations)


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
