import os
import sys
import time
import math

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

matrix = []

# This is a monstrosity please dont even look at this

def has_adjacent_symbol(y: int, x: int):
    try:
        # Down/Up/Right/Left
        if matrix[y][x + 1] != "." and not matrix[y][x + 1].isdigit():
            return True
    except IndexError:
        pass
    try:
        if matrix[y][x - 1] != "." and not matrix[y][x - 1].isdigit():
            return True
    except IndexError:
        pass
    try:
        if matrix[y - 1][x] != "." and not matrix[y - 1][x].isdigit():
            return True
    except IndexError:
        pass
    try:
        if matrix[y + 1][x] != "." and not matrix[y + 1][x].isdigit():
            return True
    except IndexError:
        pass
    try:
        # Diagonal
        if matrix[y - 1][x - 1] != "." and not matrix[y - 1][x - 1].isdigit():
            return True
    except IndexError:
        pass
    try:
        if matrix[y + 1][x - 1] != "." and not matrix[y + 1][x - 1].isdigit():
            return True
    except IndexError:
        pass
    try:
        if matrix[y - 1][x + 1] != "." and not matrix[y - 1][x + 1].isdigit():
            return True
    except IndexError:
        pass
    try:
        if matrix[y + 1][x + 1] != "." and not matrix[y + 1][x + 1].isdigit():
            return True
    except IndexError:
        pass

    return False


def get_number(y: int, x: int) -> tuple[int, int]:
    start = 0
    end = x
    for i in range(x, -1, -1):
        if matrix[y][i].isdigit():
            start = i
        else:
            break

    for i in range(x, len(matrix[y])):
        if matrix[y][i].isdigit():
            end = i
        else:
            break

    return (int("".join(matrix[y][start : end + 1])), end + 1)


numbers = []
skip_until = None
start = time.time()
with open("03.input") as f:
    for line in f.readlines():
        row = []
        for c in line:
            if c != "\n":
                row.append(c)
        matrix.append(row)

    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            if skip_until == x:
                skip_until = None

            if skip_until == None and matrix[y][x].isdigit():
                if has_adjacent_symbol(y, x):
                    number, skip_until = get_number(y, x)
                    numbers.append(number)

                    if skip_until == len(matrix[y]):
                        skip_until = None


def count_numbers(x, y, z):
    total_numbers = 0

    if x[1] == ".":
        if x[0].isdigit():
            total_numbers += 1
        if x[2].isdigit():
            total_numbers += 1
    else:
        total_numbers += 1

    if y[0].isdigit():
        total_numbers += 1
    if y[2].isdigit():
        total_numbers += 1

    if z[1] == ".":
        if z[0].isdigit():
            total_numbers += 1
        if z[2].isdigit():
            total_numbers += 1
    else:
        total_numbers += 1

    return total_numbers


def extract_numbers(x: int, data: list, row_length: int):
    nums = []

    start = 0
    end = 0
    if data[x - 1].isdigit():
        end = x - 1
        for i in range(x - 1, -1, -1):
            if data[i].isdigit():
                start = i
            else:
                break
        nums.append(int("".join(data[start : end + 1])))

    if data[x + 1].isdigit():
        start = x + 1
        for i in range(x + 1, len(data)):
            if data[i].isdigit():
                end = i
            else:
                break
        nums.append(int("".join(data[start : end + 1])))

    if data[x - row_length] == ".":
        if data[x - row_length - 1].isdigit():
            end = x - row_length - 1
            for i in range(x - row_length - 1, -1, -1):
                if data[i].isdigit():
                    start = i
                else:
                    break
            nums.append(int("".join(data[start : end + 1])))
        if data[x - row_length + 1].isdigit():
            start = x - row_length + 1
            for i in range(x - row_length + 1, len(data)):
                if data[i].isdigit():
                    end = i
                else:
                    break
            nums.append(int("".join(data[start : end + 1])))
    else:
        for i in range(x - row_length, -1, -1):
            if data[i].isdigit():
                start = i
            else:
                break
        for i in range(x - row_length, len(data)):
            if data[i].isdigit():
                end = i
            else:
                break
        nums.append(int("".join(data[start : end + 1])))

    if data[x + row_length] == ".":
        if data[x + row_length - 1].isdigit():
            end = x + row_length - 1
            for i in range(x + row_length - 1, -1, -1):
                if data[i].isdigit():
                    start = i
                else:
                    break
            nums.append(int("".join(data[start : end + 1])))
        if data[x + row_length + 1].isdigit():
            start = x + row_length + 1
            for i in range(x + row_length + 1, len(data)):
                if data[i].isdigit():
                    end = i
                else:
                    break
            nums.append(int("".join(data[start : end + 1])))
    else:
        for i in range(x + row_length, -1, -1):
            if data[i].isdigit():
                start = i
            else:
                break
        for i in range(x + row_length, len(data)):
            if data[i].isdigit():
                end = i
            else:
                break
        nums.append(int("".join(data[start : end + 1])))

    return nums


part2_numbers = []
with open("03.input") as f:
    data = []
    row_length = 0
    for line in f.readlines():
        row_length = len(line)
        for c in line:
            if c != "\n":
                data.append(c)

    for i in range(0, len(data)):
        if data[i] == "*":
            above = data[i - row_length - 1 : i - row_length + 2]
            middle = data[i - 1 : i + 2]
            below = data[i + row_length - 1 : i + row_length + 2]

            amount_of_numbers = count_numbers(above, middle, below)
            extracted_numbers = extract_numbers(i, data, row_length)

            if len(extracted_numbers) == 2:
                part2_numbers.append(math.prod(extracted_numbers))

part_one = sum(numbers)
print(f"Part 1: {part_one}")

part_two = sum(part2_numbers)
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")
