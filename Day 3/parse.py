import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

import re

def replace_non_digit_or_period(input_string):
    return re.sub(r'[^0-9\.]', '-', input_string)

def calculatePartsInSchematics():
    logging.info("Starting to calculate parts values")
    sum = 0
    for i in open("input").read().split("\n"):
        # line = replace_non_digit_or_period(i)
        # split_line = 
        split_line = [re.split('(\W)',k) if k else "" for k in i.split(".")]
        logging.debug(split_line)
        # for j in range(len(split_line)):
        #     if split_line[j] and split_line[j].isdigit():
        #         try:
        #             if split_line[j+1] or split_line[j-1]:
        #                 # logging.info(lines[j])
        #                 sum += int(split_line[j])
        #         except IndexError:
        #             if split_line[j-1]:
        #                 # logging.info(lines[j])
        #                 sum += int(split_line[j])
                    
    return sum

        
        
    # return sum(calibrationValues)


if __name__ == "__main__":
    result = calculatePartsInSchematics()
    print(result)
