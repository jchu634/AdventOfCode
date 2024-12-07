from collections import Counter
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
    similarityScore = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            tempElement1, tempElement2 = line.strip().split("   ")
            list1.append(tempElement1)
            list2.append(tempElement2)
    list2Count = Counter(list2)
    for element in list1:
        similarityScore += int(element) * list2Count[element]
    return similarityScore


if __name__ == "__main__":

    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
