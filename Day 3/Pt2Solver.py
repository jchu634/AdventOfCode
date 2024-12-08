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


def getAns():
    total = 0
    enabled = True
    with open("input.txt", "r") as file:
        for line in file.readlines():
            matches = re.findall(
                r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line.strip())
            # logging.info(matches)
            for match in matches:
                if match == "do()":
                    enabled = True
                elif match == "don't()":
                    enabled = False
                else:
                    if enabled:
                        x, y = map(int, re.findall(r'\d+', match))
                        total += x*y

    return total


if __name__ == "__main__":

    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
