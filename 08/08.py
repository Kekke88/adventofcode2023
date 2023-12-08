import os
import sys
import time
import re
import math

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

directions = []
instructions = {}

start = time.time()
with open("08.input") as f:
    for line in f.readlines():
        if not directions:
            directions = list(
                line.replace("\n", "").replace("L", "0").replace("R", "1")
            )

        if "=" in line:
            matches = re.findall("([A-Z]{3})", line)
            instructions[matches[0]] = matches[1:]

def part_one_steps():
    total_steps = 0
    current_location = "AAA"

    direction_iterator = 0
    while current_location != "ZZZ":
        current_location = instructions[current_location][
            int(directions[direction_iterator])
        ]
        direction_iterator += 1

        if direction_iterator == len(directions):
            direction_iterator = 0

        total_steps += 1
    return total_steps

def part_two_steps(start: str):
    total_steps = 0
    current_location = start

    direction_iterator = 0
    while current_location[2] != "Z":
        current_location = instructions[current_location][
            int(directions[direction_iterator])
        ]
        direction_iterator += 1

        if direction_iterator == len(directions):
            direction_iterator = 0

        total_steps += 1
    return total_steps

start_instructions = []
for instruction in instructions.keys():
    if instruction[2] == "A":
        start_instructions.append(instruction)

p2_steps = []

for start_instruction in start_instructions:
    p2_steps.append(part_two_steps(start_instruction))

part_one = part_one_steps()
print(f"Part 1: {part_one}")

part_two = math.lcm(*p2_steps)
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")
