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


def getAns(blinks):
    with open("input.txt", "r") as file:
        stones = [int(i) for i in file.readline().split(" ")]
    logging.info(stones)
    for p in range(blinks):
        for i in range(len(stones)):
            if stones[i] == 0:
                stones[i] = 1
            elif len(str(stones[i])) % 2 == 0:
                midpoint = len(str(stones[i])) // 2
                tempList = str(stones[i])
                t1, t2 = int(tempList[:midpoint]), int(tempList[midpoint:])
                stones[i] = t1
                stones.append(t2)
            else:
                stones[i] = stones[i]*2024
        logging.info(stones)
    return len(stones)


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns(25)}")
