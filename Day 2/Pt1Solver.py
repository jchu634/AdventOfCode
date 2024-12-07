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
    totalSafe = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            flag = False
            elements = [int(i) for i in line.strip().split()]
            if sorted(elements) == elements or sorted(elements, reverse=True) == elements:
                for i in range(len(elements)-1):
                    if not (0 < abs(elements[i]-elements[i+1]) < 4):
                        flag = True
                        break
                if not flag:
                    totalSafe += 1

    return totalSafe


if __name__ == "__main__":

    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
