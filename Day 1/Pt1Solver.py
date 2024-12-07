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
    list1 = []
    list2 = []
    totalDist = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            tempElement1, tempElement2 = line.strip().split("   ")
            list1.append(tempElement1)
            list2.append(tempElement2)
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        totalDist += abs(int(list1[i]) - int(list2[i]))
    return totalDist


if __name__ == "__main__":

    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
