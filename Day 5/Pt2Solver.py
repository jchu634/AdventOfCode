import time
import numpy as np
import re
import logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


def checkOrder(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def fixOrder(update, rules):
    while True:
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    yIndex = update.index(y)
                    update.pop(update.index(x))
                    update = update[0:yIndex] + [x] + update[yIndex::]

        if checkOrder(update, rules):
            break
    return update


def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])


def getAns():
    total = 0
    with open("input.txt", "r") as file:
        arr = file.read().splitlines()

    pageRules = []
    for i in range(len(arr)):
        rule = arr.pop(0)
        if rule == "":
            break
        else:
            pageRules.append(rule.split('|'))

    for updates in arr:
        update = updates.split(',')
        if not checkOrder(update, pageRules):
            update = fixOrder(update, pageRules)
            total += int(findMiddle(update))

    return total


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
