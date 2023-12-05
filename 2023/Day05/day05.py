def parse(filename, reverse):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    results = {}
    with open(filename, "r") as file:
        formatted_data = list(map(lambda x: x.strip(),file.readlines()))
        formatted_data += [""]
        results["seeds"] = list(map(lambda x: int(x), formatted_data[0].split(": ")[1].split()))
        current_key = ()
        key_data = []
        for i in range(2, len(formatted_data)):
            current_line = formatted_data[i]
            if current_line == "":
                results[current_key] = key_data
                current_key = []
                key_data = []
            elif current_line[0] in digits:
                key_data += [list(map(lambda x: int(x), current_line.split()))]
            else:
                conversion = current_line.split()[0].split("-")
                if not reverse:
                    current_key = conversion[0]
                    key_data = [conversion[2]]
                else:
                    current_key = conversion[2]
                    key_data = [conversion[0]]
    return results


def convert_almanac(current_data, conversion_list):
    converted_data = []
    for elem in current_data:
        new_elem = elem
        for item in conversion_list:
            if elem >= item[1] and elem < item[1]+item[2]:
                new_elem = elem+(item[0]-item[1])
        converted_data += [new_elem]
    return converted_data

def get_seed_locations(almanac_info):
    seeds = almanac_info["seeds"]
    current_type = "seed"
    while current_type != "location":
        # print("current type: " + current_type)
        temp = almanac_info[current_type]
        # print("converting to: " + temp[0])
        conversion_lists = temp[1:]
        seeds = convert_almanac(seeds, conversion_lists)
        current_type = temp[0]
    return seeds

def convert_single_location(seed, almanac_info):
    current = seed
    current_type = "location"
    while current_type != "seed":
        temp = almanac_info[current_type]
        conversion_list = temp[1:]
        for rule in conversion_list:
            if current >= rule[0] and current < rule[0]+rule[2]:
                current = current+(rule[1]-rule[0])
                break
        current_type = temp[0]
    return current

def get_seed_range(seeds):
    result = []
    for i in range(0, len(seeds), 2):
        result += [(seeds[i],seeds[i]+seeds[i+1])]
    return result

def in_range(seed, seed_ranges):
    return any(start <= seed < end for start, end in seed_ranges)

def new_get_seed_locations(almanac_info):
    seed_ranges = get_seed_range(almanac_info["seeds"])
    location = 0
    while True:
        seed = convert_single_location(location, almanac_info)
        if in_range(seed, seed_ranges):
            return location
        location += 1
        if location % 1_000_000 == 0:
            print(location)

def main(filename):
    almanac_info = parse(filename, True)
    # locations = get_seed_locations(almanac_info)
    min_local = new_get_seed_locations(almanac_info)
    print(min_local)

if __name__ == "__main__":
    main("2023/Day05/main_input.txt")