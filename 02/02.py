import os
import sys
import time
import math

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

i = 1
sum = 0
sum_power = 0
max_counts = {"red": 12, "green": 13, "blue": 14}
start = time.time()
with open("02.input") as f:
    for line in f.readlines():
        count_game = True

        line = line.replace("\n", "")
        line = line.split(": ")[1]
        rounds = line.split("; ")
        min_needed = {"red": 0, "green": 0, "blue": 0}
        for round in rounds:
            picks = round.split(", ")
            for pick in picks:
                count, color = pick.split(" ")
                if min_needed[color] < int(count):
                    min_needed[color] = int(count)

                if int(count) > max_counts[color]:
                    count_game = False

        sum_power += math.prod(min_needed.values())
        if count_game:
            sum += i
        i += 1

part_one = sum
print(f"Part 1: {part_one}")

part_two = sum_power
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")
