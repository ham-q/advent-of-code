from functools import reduce
from dataclasses import dataclass
from math import ceil, floor
from scipy.optimize import fsolve

@dataclass
class race_info:
    duration: int
    record: int

def parse_records(filename):
    with open(filename,"r") as file:
        data = file.readlines()
        # time = list(map(lambda x: int(x), data[0].strip().split()[1:]))
        time = [int("".join(data[0].strip().split()[1:]))]
        print("".join(data[0].strip().split()[1:]))
        print(time)
        # distance = list(map(lambda x: int(x), data[1].strip().split()[1:]))
        distance = [int("".join(data[1].strip().split()[1:]))]
        print(distance)
        races = [race_info(duration, record) for (duration, record) in zip(time, distance)]
    return races

def run_race(time_pressed: int, race_data: race_info):
    difference_from_record = time_pressed*(race_data.duration-time_pressed) - race_data.record - 0.01
    return difference_from_record

def get_ways_to_win(race_records):
    result = []
    for race in race_records:
        first_root = 0
        second_root = race.duration
        roots = fsolve(run_race, [first_root,second_root],args=race)
        print(roots)
        ways_to_win = floor(roots[1]) - ceil(roots[0]) + 1
        result += [int(ways_to_win)]
    return result


def main(filename):
    race_records = parse_records(filename)
    print(race_records)
    input()
    get_ways = get_ways_to_win(race_records)
    total_num_of_ways = reduce(lambda x, y: x*y, get_ways)
    print(get_ways)
    print(total_num_of_ways)

if __name__ == "__main__":
    main("2023/Day06/main_input.txt")