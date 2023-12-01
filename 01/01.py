import os
import sys
import time
import re

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

part_one = 0
part_two = 0

start = time.time()
with open("01.input") as f:
    for line in f.readlines():
        numbers = re.sub("[^0-9]", "", line)
        number = numbers[0] + numbers[len(numbers) - 1]
        part_one += int(number)

nummap = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}
with open("01.input") as f:
    for line in f.readlines():
        first_number = None
        for i in range(0, len(line)):
            if line[i].isnumeric():
                first_number = line[i]
                break
            else:
                for k, v in nummap.items():
                    if line[i : i + len(k)] == k:
                        first_number = v
                        break
            if first_number:
                break

        second_number = None
        for i in range(len(line) - 1, -1, -1):
            if line[i].isnumeric():
                second_number = line[i]
                break
            else:
                for k, v in nummap.items():
                    if line[i : i + len(k)] == k:
                        second_number = v
                        break
            if second_number:
                break

        part_two += int(first_number + second_number)


print(f"Part 1: {part_one}")

print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")
