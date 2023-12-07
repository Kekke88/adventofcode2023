import os
import sys
import time
import math

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

start = time.time()
times = []
distances = []


def is_better_than_record(loading_time, time, record_distance):
    return loading_time * (time - loading_time) > record_distance


p2_time = 0
p2_dist = 0
p2_wins_start = 0
p2_wins_stop = 0
wins = []
with open("06.input") as f:
    for line in f.readlines():
        if "Time:" in line:
            times = line.replace("\n", "").split(" ")[1:]
            times = list(filter(None, times))
            p2_time = int("".join(times))
            for i in range(0, len(times)):
                times[i] = int(times[i])

        if "Distance:" in line:
            distances = line.replace("\n", "").split(" ")[1:]
            distances = list(filter(None, distances))
            p2_dist = int("".join(distances))
            for i in range(0, len(distances)):
                distances[i] = int(distances[i])

    for i in range(0, len(times)):
        tmp_wins = 0
        for j in range(1, times[i]):
            if is_better_than_record(j, times[i], distances[i]):
                tmp_wins += 1

        wins.append(tmp_wins)

    # Part 2
    for j in range(1, p2_time):
        if is_better_than_record(j, p2_time, p2_dist):
            p2_wins_start = j
            break

    for j in range(p2_time, 0, -1):
        if is_better_than_record(j, p2_time, p2_dist):
            p2_wins_stop = j
            break

part_one = math.prod(wins)
print(f"Part 1: {part_one}")

part_two = p2_wins_stop - p2_wins_start + 1
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")
