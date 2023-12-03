import itertools
from functools import reduce

def colours_to_list(input, colour_list):
    game_colours = {}
    for item in input:
        temp = item.split()
        value = int(temp[0])
        colour = temp[1]
        game_colours[colour] = value
    result = []
    for colour in colour_list:
        if colour in game_colours:
            result += [game_colours[colour]]
        else:
            result += [0]
    return result

def parse_games(filename):
    # [[id, [r0,g0,b0], [r1,g1,b1]... [rn,gn,bn]]...]
    output = []
    with open(filename ,"r") as file:
        for line in file:
            game_information = []
            temp = list(map(lambda x: x.split("; "), line.strip().split(": ")))
            temp[0] = int(temp[0][0][5:])
            temp[1] = list(map(lambda x: x.split(', '), temp[1]))
            temp[1] = list(map(lambda x: colours_to_list(x, ['red','green','blue']), temp[1]))
            game_information = temp
            output += [game_information]
    return output

def check_if_set_is_valid(input_set, true_amount):
    assert len(input_set) == len(true_amount)
    result = True
    for i in range(len(input_set)):
        if input_set[i] > true_amount[i]:
            result = False
    return result

def game_validator(game_list,true_amount):
    result = []
    for game in game_list:
        validity_check = list(map(lambda x: check_if_set_is_valid(x,true_amount) ,game[1]))
        if all(validity_check):
            result += [game[0]]
    return result

def find_power(game_list):
    result = []
    for game in game_list:
        list_of_sets = game[1]
        max_elems = []
        for i in range(len(list_of_sets[0])):
            max_elems += [max([sublist[i] for sublist in list_of_sets])]
        power = reduce(lambda x, y: x*y, max_elems)
        result += [power]
    return result

def Main(filename):
    formatted_data = parse_games(filename)
    valid_game_IDs = game_validator(formatted_data, [12,13,14])
    power_list = find_power(formatted_data)
    print(sum(power_list))

if __name__ == "__main__":
    Main("2023/Day02/main_input.txt")