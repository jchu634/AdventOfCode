import numpy as np
import logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


def removeAndRetry(splitElements):
    for i in range(len(splitElements)):
        spl = splitElements.copy()
        spl.pop(i)

        elements = np.array([int(spl[j]) - int(spl[j - 1])
                            for j in range(1, len(spl))])

        if np.sign(int(spl[1]) - int(spl[0])) == -1:  # Decr
            if not np.any(False == np.logical_and(elements <= -1, elements >= -3)):
                return True
        elif np.sign(int(spl[1]) - int(spl[0])) == 1:  # Incr
            if not np.any(False == np.logical_and(elements >= 1, elements <= 3)):
                return True

    return False


def getAns():
    totalSafe = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            splitElements = line.strip().split()

            elements = np.array([int(splitElements[i]) - int(splitElements[i - 1])
                                for i in range(1, len(splitElements))])

            if np.sign(int(splitElements[1]) - int(splitElements[0])) == -1:  # Decr
                if np.any(False == np.logical_and(elements < 0, elements > -4)):
                    totalSafe += removeAndRetry(splitElements)
                else:
                    totalSafe += 1
            elif np.sign(int(splitElements[1]) - int(splitElements[0])) == 1:  # Incr
                if np.any(False == np.logical_and(elements > 0, elements < 4)):
                    totalSafe += removeAndRetry(splitElements)
                else:
                    totalSafe += 1
            else:
                totalSafe += removeAndRetry(splitElements)
    return totalSafe


if __name__ == "__main__":

    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
