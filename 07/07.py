import os
import sys
import time

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

card_value_map = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def get_type_strength(hand: str) -> int:
    hand_list = list(hand)

    # Part 2 - START
    if hand_list.count("J") > 0 and hand_list.count("J") < 5:
        most_occuring_character = ""

        for card in hand_list:
            if card == "J":
                continue
            if most_occuring_character == "":
                most_occuring_character = card
                continue

            if hand_list.count(card) > hand_list.count(most_occuring_character):
                most_occuring_character = card

        hand = hand.replace("J", most_occuring_character)
    # Part 2 - END

    if len(set(hand)) == 1:
        return 7

    card_list = {}
    for i in range(0, len(hand)):
        if not card_list.get(hand[i]):
            card_list[hand[i]] = 0

        card_list[hand[i]] += 1

    if len(card_list) == 2:
        for card in card_list.values():
            if card == 4:
                return 6
            if card == 3:
                return 5

    if len(card_list) == 3:
        for card in card_list.values():
            if card == 3:
                return 4

    if len(card_list) == 3:
        return 3

    if len(card_list) == 4:
        return 2

    return 1


def is_hand_stronger(hand1, hand2) -> bool:
    for i in range(len(hand1)):
        if card_value_map[hand1[i]] > card_value_map[hand2[i]]:
            return True

        if card_value_map[hand1[i]] < card_value_map[hand2[i]]:
            return False

    return False


start = time.time()
hands = {}
sorted_hands = {}
with open("07.input") as f:
    for line in f.readlines():
        hand, bid = line.split(" ")
        hands[hand] = int(bid)

    while len(hands) > 0:
        lowest_hand = None
        for key in hands.keys():
            if not lowest_hand:
                lowest_hand = key
                continue

            if get_type_strength(lowest_hand) > get_type_strength(key):
                lowest_hand = key
            if get_type_strength(lowest_hand) == get_type_strength(key):
                if is_hand_stronger(lowest_hand, key):
                    lowest_hand = key

        sorted_hands[lowest_hand] = hands[lowest_hand]
        del hands[lowest_hand]

score = 0
iterator = 1
for hand in sorted_hands.values():
    score += hand * iterator
    iterator += 1

part_one = "NOT AVAILABLE"
print(f"Part 1: {part_one}")

part_two = score
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")
