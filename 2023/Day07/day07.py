from dataclasses import dataclass
from collections import Counter
from functools import cmp_to_key

@dataclass
class card:
    hand: list[str]
    bid: int

def parse_hands(filename) -> list[card]:
    cards = []
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split()
            cards += [card(list(data[0]), int(data[1]))]
    return cards

def card_value_ordering():
    return ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def alt_card_ordering():
    return ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

def get_card_value(c: card):
    frequency = sorted(Counter(c.hand).values(), reverse=True)
    if 5 in frequency:
        return 7
    if 4 in frequency:
        return 6
    if [3,2] == frequency:
        return 5
    if 3 in frequency:
        return 4
    if frequency.count(2) == 2:
        return 3
    if 2 in frequency:
        return 2
    else:
        return 1

def get_card_value_joker(c:card):
    card_counter = Counter(c.hand)
    if "J" in card_counter.keys():  # we know #Jokers > 0
        num_of_jokers = card_counter["J"]
        card_counter["J"] = 0
        frequency = sorted(card_counter.values(), reverse=True)
        if (5-num_of_jokers in frequency):
            return 7
        if 4-num_of_jokers in frequency:
            return 6
        if (num_of_jokers == 3 and (frequency.count(1) == 2 or 2 in frequency)) or (num_of_jokers == 2 and (3 in frequency or (2 in frequency and 1 in frequency))) or (num_of_jokers == 1 and (frequency.count(2) == 2 or (3 in frequency and 1 in frequency))):
            return 5
        if 3-num_of_jokers in frequency:
            return 4
        if (2 in frequency and 2-num_of_jokers in frequency) or (frequency.count(1) == 2 and num_of_jokers == 2):
            return 3
        if 2-num_of_jokers in frequency:
            return 2
        else:
            return 1
    else:
        return get_card_value(c)

def compare_cards(firstcard: card, secondcard: card) -> bool:
    firstvalue = get_card_value_joker(firstcard)
    secondvalue = get_card_value_joker(secondcard)
    if firstvalue > secondvalue:
        return 1
    if secondvalue > firstvalue:
        return -1
    else:
        card_order = alt_card_ordering()
        for i in range(5):
            if card_order.index(firstcard.hand[i]) > card_order.index(secondcard.hand[i]):
                return 1
            if card_order.index(firstcard.hand[i]) < card_order.index(secondcard.hand[i]):
                return -1
        return 0

def get_winnings(card_list: list[card]) -> list[int]:
    card_list.sort(key=cmp_to_key(compare_cards))
    result = []
    rank = 1
    for card in card_list:
        print("".join(card.hand))
        result += [rank*card.bid]
        rank += 1
    return result

def main(filename) -> None:
    card_list = parse_hands(filename)
    winnings = get_winnings(card_list)
    print(sum(winnings))

if __name__ == "__main__":
    main("2023/Day07/main_input.txt")