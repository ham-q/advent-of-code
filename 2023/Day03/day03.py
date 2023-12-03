from functools import reduce

class numbers_information:
    value = 0
    locations = []

    def __init__(self, value, locations) -> None:
        self.value = value
        self.locations = locations
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self.value) + ": " + str(self.locations)

def parse_schematic(filename):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    symbol_locations = []
    numbers = []
    with open(filename,'r') as file:
        row_number = 0
        for line in file:
            line = line.strip()
            prev_was_int = False
            current_number = ""
            current_number_locations = []
            column_number = 0
            for char in line:
                if (char not in digits) and prev_was_int:
                    numbers += [numbers_information(int(current_number),current_number_locations)]
                    current_number = ""
                    current_number_locations = []
                    prev_was_int = False
                if char not in digits and char != ".":
                    symbol_locations += [numbers_information(char,[(row_number,column_number)])]
                if char in digits:
                    if not prev_was_int:
                        prev_was_int = True
                    current_number += char
                    current_number_locations += [(row_number,column_number)]
                column_number += 1
            if prev_was_int:
                numbers += [numbers_information(int(current_number),current_number_locations)]
            row_number += 1
    return (numbers, symbol_locations)


def validate_parts(numbers_info, symbol_info):
    valid_parts = []
    symbol_locations = [symbol.locations[0] for symbol in symbol_info]
    for number in numbers_info:
        locations = number.locations
        is_valid = False
        for location in locations:
            for i in range(-1,2):
                for j in range(-1,2):
                    if (location[0]+i,location[1]+j) in symbol_locations:
                        is_valid = True
        if is_valid:
            valid_parts += [number.value]
    return valid_parts

def find_gear_ratios(numbers_info, symbol_info):
    result = []
    gear_locations = [gear.locations[0] for gear in symbol_info if gear.value=="*"]
    for gear in gear_locations:
        adjacent_numbers = set(())
        for i in range(-1,2):
            for j in range(-1,2):
                for number in numbers_info:
                    if (gear[0]+i,gear[1]+j) in number.locations:
                        adjacent_numbers.add(number.value)
        if len(adjacent_numbers) == 2:
            gear_ratio = reduce(lambda x, y: x*y, adjacent_numbers)
            result += [gear_ratio]
    return result

def Main(filename):
    (number_info, symbol_info) = parse_schematic(filename)
    part_list = validate_parts(number_info, symbol_info)
    gear_ratios = find_gear_ratios(number_info, symbol_info)
    print(sum(gear_ratios))

if __name__ == "__main__":
    Main("2023/Day03/main_input.txt")