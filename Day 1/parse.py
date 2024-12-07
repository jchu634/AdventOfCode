import logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def replace_words_with_numbers(input_string):
    word_to_num = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                   "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
    output = ""
    i = 0
    while i < len(input_string):
        for word, number in word_to_num.items():
            if input_string[i:].startswith(word):
                output += number
                i += len(word)
                break
        else:
            output += input_string[i]
            i += 1
    return output

def calculateCalibrationValues():
    logging.info("Starting to calculate calibration values")
    calibrationValues = []
    for i in open("input.txt").read().split("\n"):
        i = replace_words_with_numbers(i)
        logging.debug(i)
        intList = [inputInt for inputInt in i if inputInt.isdigit()]
        logging.info(intList)
        calibrationValues.append(int(f"{intList[0]}{intList[-1]}"))
        
    return sum(calibrationValues)


if __name__ == "__main__":
    result = calculateCalibrationValues()
    print(result)
