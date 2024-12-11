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


def getStones(i):
    if i == "0":
        return ["1"]
    elif len(i) % 2 == 0:
        midpoint = len(i) // 2        
        return i[:midpoint], str(int(i[midpoint:])) #Conversions necessary to remove leading zero
    else:
        return [str(int(i)*2024)]

def getAns(blinks):
    with open("input.txt", "r") as file:
        stones = file.readline().split(" ")

    quantityDict = {}     # Dict: {stoneNo}: no of stones with this number
    for stone in stones:  # Populate dict
        if stone in quantityDict:
            quantityDict[stone] += 1
        else:
            quantityDict[stone] = 1
        quantityDict[stone] = 1

    for p in tqdm(range(blinks)):
        newDict = {}
        for num in quantityDict:
            quantity = quantityDict[num]
            stones = getStones(num)

            for i in stones:
                if i in newDict:
                    newDict[i] += quantity
                else:
                    newDict[i] = quantity
        quantityDict = newDict.copy()
    # logging.info(quantityDict)
    return sum(quantityDict.values())

if __name__ == "__main__":
    blinks = 75
    logging.info("Started Program")
    logging.info(f"Ans: {getAns(blinks)}")
