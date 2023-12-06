import os
import sys
import time

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

seeds = []
p2_seeds = []

def range_overlap(range1, range2):
    x1, x2 = range1.start, range1[-1]
    y1, y2 = range2.start, range2[-1]
    return x1 <= y2 and y1 <= x2


start = time.time()
with open("05.input") as f:
    for line in f.readlines():
        if "seeds" in line:
            seeds = line.replace("\n", "").split(": ")[1]
            seeds = seeds.split(" ")
            for i in range(len(seeds)):
                seeds[i] = int(seeds[i])

            new_seeds = []

            for i in range(0, len(seeds), 2):
                # Extract all part 2 seed ranges
                p2_seeds.append(range(seeds[i], seeds[i] + seeds[i + 1]))

            continue

        line = line.replace("\n", "").split(" ")

        if len(line) == 1:
            if len(new_seeds) >= 1:
                # Add the new seed ranges and remove the deleted ones
                p2_seeds.extend(new_seeds)
                p2_seeds = list(filter(lambda item: item is not None, p2_seeds))
                new_seeds = []
            continue
        if len(line) <= 2:
            #Skip the text lines (seed-to-xxx)
            continue

        start_map = int(line[0])
        range_start = int(line[1])
        range_length = int(line[2])

        #print("iteration")
        for p2_seed in p2_seeds:
            if not p2_seed:
                continue
            if range_overlap(p2_seed, range(range_start, range_start + range_length)):
                if (
                    p2_seed[0] >= range_start
                    and p2_seed[-1] <= range_start + range_length
                ):
                    new_seeds.append(
                        range(
                            p2_seed[0] - (range_start - start_map),
                            p2_seed[-1] - (range_start - start_map) + 1,
                        )
                    )
                elif (
                    range_start > p2_seed[0]
                    and range_start + range_length >= p2_seed[-1]
                ):
                    p2_seeds.append(range(p2_seed[0], range_start))
                    new_seeds.append(
                        range(
                            range_start - (range_start - start_map),
                            p2_seed[-1] - (range_start - start_map) + 1,
                        )
                    )
                elif (
                    range_start > p2_seed[0]
                    and range_start + range_length < p2_seed[-1]
                ):
                    p2_seeds.append(range(p2_seed[0], range_start))
                    new_seeds.append(
                        range(
                            range_start - (range_start - start_map),
                            (range_start + range_length) - (range_start - start_map),
                        )
                    )
                    p2_seeds.append(
                        range((range_start + range_length), p2_seed[-1] + 1)
                    )
                elif (
                    range_start <= p2_seed[0]
                    and range_start + range_length >= p2_seed[0]
                    and range_start + range_length <= p2_seed[-1]
                ):
                    new_seeds.append(
                        range(
                            p2_seed[0] - (range_start - start_map),
                            range_start + range_length - (range_start - start_map),
                        )
                    )
                    p2_seeds.append(range(range_start + range_length, p2_seed[-1] + 1))

                p2_seeds[p2_seeds.index(p2_seed)] = None

p2_seeds.extend(new_seeds)
p2_seeds = list(filter(lambda item: item is not None, p2_seeds))
print(p2_seeds)
lowest = None
for seed in p2_seeds:
    if not lowest:
        lowest = seed[0]

    if lowest > seed[0]:
        lowest = seed[0]

print(f"Answer: {lowest}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")
