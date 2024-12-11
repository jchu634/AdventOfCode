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


def getAns():
    with open("input.txt", "r") as file:
        inputFile = file.readline().strip()
    files = []
    all = ""
    index = 0

    for i, num in enumerate(list(inputFile)):
        if i % 2 == 0:
            files += [str(index) for i in range(int(num))]
            all += "N" * int(num)
            index += 1
        else:
            all += "." * int(num)

    total = 0
    for i, char in enumerate(tqdm(all)):
        if len(files) == 0:
            break
        else:
            total += i * (int(files.pop(0)) if char !=
                          "." else int(files.pop()))

    return total


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
