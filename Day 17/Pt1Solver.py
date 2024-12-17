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


def chunkify(lst, n):
    return [lst[i::n] for i in range(n)]


def getComboOperand(operand, regA, regB, regC):
    if operand <= 3:
        return operand
    elif operand == 4:
        return regA
    elif operand == 5:
        return regB
    elif operand == 6:
        return regC


def getAns():
    with open("input.txt", "r") as file:
        regA, regB, regC, _, Program = file.read().splitlines()

    regA = int(regA.split(": ")[1])
    regB = int(regB.split(": ")[1])
    regC = int(regC.split(": ")[1])
    Program = [int(i) for i in Program.split(": ")[1].split(",")]
    output = ""

    instructionPointer = 0
    try:
        while True:
            opCode = Program[instructionPointer]
            operand = Program[instructionPointer+1]
            match opCode:
                case 0:  # adv
                    regA = regA // (2**getComboOperand(operand, regA, regB, regC))
                case 1:  # bxl
                    regB = regB ^ operand
                case 2:  # bst
                    regB = getComboOperand(operand, regA, regB, regC) % 8
                case 3:  # jnz
                    if regA != 0:
                        instructionPointer = operand
                        continue
                case 4:  # bxc
                    regB = regB ^ regC
                case 5:  # out
                    if output:
                        output += f",{getComboOperand(operand, regA, regB, regC) % 8}"
                    else:
                        output = f"{getComboOperand(operand, regA, regB, regC) % 8}"
                case 6:  # bdv
                    regB = regA // (2**getComboOperand(operand, regA, regB, regC))
                case 7:  # cdv
                    regC = regA // (2**getComboOperand(operand, regA, regB, regC))

            instructionPointer += 2
    except IndexError:
        pass
    return output


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
