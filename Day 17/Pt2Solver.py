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


def getProgramOutput(regA, regB, regC, Program):
    output = []

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
                    output.append(getComboOperand(operand, regA, regB, regC) % 8)
                case 6:  # bdv
                    regB = regA // (2**getComboOperand(operand, regA, regB, regC))
                case 7:  # cdv
                    regC = regA // (2**getComboOperand(operand, regA, regB, regC))

            instructionPointer += 2
    except IndexError:
        pass
    return output


def generator():
    while True:
        yield


def getAns():
    with open("input.txt", "r") as file:
        regA, regB, regC, _, Program = file.read().splitlines()

    regA = 0
    regB = int(regB.split(": ")[1])
    regC = int(regC.split(": ")[1])
    Program = [int(i) for i in Program.split(": ")[1].split(",")]
    logging.info(Program)
    y = len(Program)
    x = len(Program)-3
    while True:

        output = getProgramOutput(regA, regB, regC, Program)
        matching_digits = sum(1 for a, b in zip(output, Program) if a == b)

        if output[x:y+1] == Program[x:y]:

            logging.info(f"{output} ({regA}): {matching_digits} matching digits")
            output_str = ' '.join(bin(x)[2:] if i % 2 == 0 else str(x) for i, x in enumerate(output))

            # logging.info(f"Output: {output_str}")

        if (output == Program):
            logging.info(getProgramOutput(regA, regB, regC, Program))
            logging.info(getProgramOutput(regA, regB, regC, Program) == Program)
            return regA

        regA += 1


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
