import os
import sys
import time
import re

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def inc_scratch_card(card_no: int):
    if not scratch_cards.get(card_no):
        scratch_cards[card_no] = 1
    else:
        scratch_cards[card_no] += 1


start = time.time()
points = 0
i = 0
scratch_cards = {}
with open("04.input") as f:
    for line in f.readlines():
        inc_scratch_card(i)
        winning_numbers = re.search("(?<=\:.)(.*)(?=.\|)", line).group(1).split(" ")
        winning_numbers = list(filter(("").__ne__, winning_numbers))

        drawn_numbers = re.search("(?<=\|)(.*)", line).group(1).split(" ")
        drawn_numbers = list(filter(("").__ne__, drawn_numbers))

        number_of_matches = len(set(winning_numbers) & set(drawn_numbers))

        num = scratch_cards[i]
        for j in range(1, number_of_matches + 1):
            for y in range(0, num):
                inc_scratch_card(i + j)

        if number_of_matches == 0:
            points += 0
        elif number_of_matches == 1:
            points += 1
        else:
            points += pow(2, number_of_matches - 1)

        #print(scratch_cards)

        i += 1

part_one = points
print(f"Part 1: {part_one}")

part_two = sum(scratch_cards.values())
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")
