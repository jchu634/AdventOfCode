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


def getAns():
    with open("input.txt", "r") as file:
        inputFile = file.readline().strip()
    files = []
    fileLengths = []
    all = ""
    index = 0

    for i, num in enumerate(list(inputFile)):
        if i % 2 == 0:
            # files += [str(index) for i in range(int(num))]
            files += str(index)
            fileLengths.append((int(num), i))
            all += "N"
            index += 1
        else:
            all += num

    total = 0
    minSize = 0
    index = -1
    debugString = []
    all = list(all)
    for char in all:
        if len(files) == 0 or len(fileLengths) == 0:
            break
        else:
            if char == "N":
                # total += i * int(files.pop(0))
                a, c = fileLengths.pop(0)
                b = files.pop(0)
                total += ((4*i)+((a-1)*a)/2)*int(b)
                i += a

                debugString += [b] * a
                # debugString += str(b) * a

            else:
                blockSize = int(char)
                while True:
                    if blockSize > minSize:
                        flag = True
                        for i in reversed(range(0, len(fileLengths))):
                            if fileLengths[i][0] <= blockSize:
                                a, c = fileLengths.pop(i)
                                b = files.pop(i)
                                total += ((4*i)+((a-1)*a)/2)*int(b)
                                all[c] = str(a)

                                i += a
                                flag = False
                                # debugString += str(b) * a
                                debugString += [b] * a
                                break
                        if flag:
                            minSize = blockSize
                            debugString += "." * blockSize
                            debugString += ["."] * a
                            break
                        else:
                            blockSize -= a
                            if blockSize == 0:
                                break

                        # total += i * (int(files.pop(0)) if char !=
                        #       "." else int(files.pop()))
                    else:
                        debugString += ["."] * blockSize

                        break

    logging.info(debugString)
    total = 0
    for i, j in enumerate(list(debugString)):
        if j != ".":
            total += i*int(j)
    return total


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
