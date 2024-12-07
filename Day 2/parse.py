import logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def getValidLinesSum():
    logging.info("Starting to calculate valid lines")
    validLines = set()
    red = 12
    green = 13
    blue = 14
    try:
        for i,lines in enumerate(open("input.txt").read().split("\n")):
            game = lines.split("Game ")[1].split(": ")[1].split(";")
            flag = False
            for rounds in game:
                redCount = 0
                greenCount = 0
                blueCount = 0

                actions = rounds.split(", ")
                for action in actions:
                    contents = [i for i in action.split(" ") if i]
                    if contents[-1] == "red":
                        redCount += int(contents[0])
                    elif contents[-1] == "green":
                        greenCount += int(contents[0])
                    elif contents[-1] == "blue":
                        blueCount += int(contents[0])
                logging.debug("red: " + str(redCount) + " green: " + str(greenCount) + " blue: " + str(blueCount))
                if redCount > red or greenCount > green or blueCount > blue:
                    flag = True
                    logging.info(f"Invalid line: {i+1}")
                    break
                    

            if not flag:                    
                validLines.add(i+1)
                        
            # validLines.append(i+1
    except IndexError:
        pass
    logging.info(validLines)
        
    return sum(validLines)

def getMinCubes():
    logging.info("Starting to calculate minimum cubes")
    powerSum = 0
    try:
        for lines in open("input.txt").read().split("\n"):
            game = lines.split("Game ")[1].split(": ")[1].split(";")
            
            red = 0
            green = 0
            blue = 0


            for rounds in game:
                actions = rounds.split(", ")
                for action in actions:
                    contents = [i for i in action.split(" ") if i]
                    if contents[-1] == "red":
                        if int(contents[0]) > red:
                            red = int(contents[0])
                    elif contents[-1] == "green":
                        if int(contents[0]) > green:
                            green = int(contents[0])
                    elif contents[-1] == "blue":
                        if int(contents[0]) > blue:
                            blue = int(contents[0])
                logging.debug("red: " + str(red) + " green: " + str(green) + " blue: " + str(blue))           

            logging.debug(red)
            logging.debug(green)
            logging.debug(blue)
            powerSum += red*green*blue
                
                     
            # validLines.append(i+1
    except IndexError:
        pass
        
    return powerSum



if __name__ == "__main__":
    # #Pt 1.
    # result = getValidLinesSum()
    # print(result)
    
    #Pt 2.
    result = getMinCubes()
    print(result)
