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


def checkOrderNp(update, rules):
    update_arr = np.array(update)
    for x, y in rules:
        if x in update and y in update:
            x_indices = np.where(update_arr == x)[0]
            y_indices = np.where(update_arr == y)[0]
            if np.any(x_indices > y_indices):
                return False
    return True


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
        if checkOrder(update, pageRules):
            total += int(findMiddle(update))

    return total


def getAnsNP():
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
        if checkOrderNp(update, pageRules):
            total += int(findMiddle(update))

    return total


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")

    # Misc: Curious if NP implementation of checking order was faster
    total = 0
    for i in range(5):
        startTime = time.time()
        getAns()

        total += time.time() - startTime
    logging.info("--- AVG %s seconds ---" % (total/5))

    total = 0
    for i in range(5):
        startTime = time.time()
        getAnsNP()
        # logging.info(f"Ans: {getAnsNP()}")
        total += time.time() - startTime
    logging.info("--- AVG %s seconds ---" % (total/5))
