from dataclasses import dataclass
from copy import deepcopy
from collections import Counter
from functools import cache

@dataclass
class picross_row:
    springs: list[int]
    location_data: list[str]

def parse(filename):
    result = []
    with open(filename, "r") as file:
        for line in file:
            temp = line.strip().split()
            result += [picross_row(list(map(int,temp[1].split(","))), list(temp[0]))]
        return result

@cache
def row_arrangements_redone(row_data):
    springs = row_data[0]
    locations = row_data[1]
    if len(locations) == 0:
        if len(springs) == 0:
            return 1
        else:
            return 0
    if len(springs) == 0:
        if  all(x != "#" for x in locations):
            return 1
        else:
            return 0
    if locations[0] == ".":
        return row_arrangements_redone((springs, locations[1:]))
    if locations[0] == "?":
        return row_arrangements_redone((springs, tuple(["."] + list(locations[1:])))) + row_arrangements_redone((springs, tuple(["#"] + list(locations[1:]))))
    if locations[0] == "#":
        looking_for = springs[0]
        if len(locations) < looking_for:
            return 0
        if all(x != "." for x in locations[:looking_for]):
            if len(locations) == looking_for:
                return row_arrangements_redone((springs[1:], locations[looking_for:]))
            elif locations[looking_for] == "#":
                return 0
            else:
                return row_arrangements_redone((springs[1:], locations[looking_for+1:]))
        else:
            return 0

def new_part_a(parsed_data):
    results = 0
    i=1
    for row in parsed_data:
        #print("------------------------------")
        #print("row:", row.location_data)
        #print(row.springs)
        ans = row_arrangements_redone((tuple(row.springs), tuple(row.location_data)))
        #print(i, "/", len(parsed_data))
        #print(ans)
        results += ans
        i += 1
    return results

def new_part_b(parsed_data):
    results = 0
    i=1
    for row in parsed_data:
        new_springs = row.springs*5
        new_locations = ((row.location_data + ["?"])*4) + row.location_data
        ans = row_arrangements_redone((tuple(new_springs), tuple(new_locations)))
        results += ans
        i += 1
    return results

def main(filename):
    parsed_data = parse(filename)
    a_sol = new_part_a(parsed_data)
    print("Sol for a:", a_sol)
    b_sol = new_part_b(parsed_data)
    print("Sol for b:", b_sol)

if __name__ == '__main__':
    main('2023/Day12/main_input.txt')