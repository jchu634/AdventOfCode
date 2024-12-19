import sys
import numpy as np
from tqdm import tqdm
import logging
import re
from itertools import permutations
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


def chunkify(lst, n):
    return [lst[i::n] for i in range(n)]


def count_ways(parts, target, memo=None):
    if memo is None:
        memo = {}

    # Base cases
    if target == "":
        return 1    # Answer Found
    if target in memo:
        return memo[target]

    # Initialize ways to form the current target
    ways = 0

    for part in parts:
        if target.startswith(part):
            # Recurse with the remaining target string
            ways += count_ways(parts, target[len(part):], memo)

    # Memoize the result
    memo[target] = ways
    return ways


def find_combination(pattern, substrings, input_string):
    # Escape substrings and join them into a regex pattern
    pattern = f"^({'|'.join(map(re.escape, substrings))})+$"

    # Create a regex object to extract matches
    regex = re.compile(f"({'|'.join(map(re.escape, substrings))})")

    # Check if the input matches the pattern
    if re.fullmatch(pattern, input_string):
        # Find all substrings that match sequentially
        matches = regex.findall(input_string)
        return True, matches
    else:
        return False, []


def find_combinations(pattern, substrings, input_string):
    # First, check if the input string can be formed
    if not re.fullmatch(pattern, input_string):
        return []

    results = []

    def backtrack(start, path):
        if start == len(input_string):
            results.append(path[:])  # Found a valid combination
            return

        for sub in substrings:
            if input_string.startswith(sub, start):
                path.append(sub)  # Add substring to the current path
                backtrack(start + len(sub), path)  # Recurse for the next part
                path.pop()  # Backtrack to explore other combinations

    backtrack(0, [])
    return results


def getAns():
    with open("input.txt", "r") as file:
        fileIn = file.read().splitlines()

    regex = sorted(fileIn.pop(0).split(", "), key=len, reverse=True)
    fileIn.pop(0)
    pattern = f"^({'|'.join(map(re.escape, regex))})+$"

    counter = 0
    for combo in tqdm(fileIn):
        tempBool, tempCombo = find_combination(pattern, regex, combo)
        if tempBool:
            counter += count_ways(regex, combo)

    return counter


if __name__ == "__main__":
    logging.info("Started Program")
    logging.info(f"Ans: {getAns()}")
