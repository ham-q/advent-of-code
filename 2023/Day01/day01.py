import re

def parse_calibration(filename):
    output = []
    with open(filename ,"r") as file:
        for line in file:
            output += [line]
    return output

def extract_digits_only(case):
    first_digit = "0"
    last_digit = "0"
    first_not_found = True
    for char in case:
        if char in ['0','1','2','3','4','5','6','7','8','9']:
            if first_not_found:
                first_digit, last_digit = char, char
                first_not_found = False
            else:
                last_digit = char
    calibration_value = int(first_digit + last_digit)
    return calibration_value

def extract_numbers(case):
    translation_table = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3':'3',
        '4':'4',
        '5':'5',
        '6':'6',
        '7':'7',
        '8':'8',
        '9':'9',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
        }
    first_index = 10000
    first_digit = "0"
    last_index = -1
    last_digit = ""
    for number in ['0','1','2','3','4','5','6','7','8','9','one','two','three','four','five','six','seven','eight','nine']:
        found_instances = [m.start() for m in re.finditer(number, case)]
        if found_instances:
            if found_instances[0] < first_index:
                first_index = found_instances[0]
                first_digit = translation_table[number]
            if found_instances[-1] > last_index:
                last_index = found_instances[-1]
                last_digit = translation_table[number]
    calibration_value = int(first_digit + last_digit)
    return calibration_value

def extract_calibration_values(calibration_list):
    results = []
    for case in calibration_list:
        results += [extract_numbers(case)]
    return results

def Main(filename):
    formatted_input = parse_calibration(filename)
    print(sum(extract_calibration_values(formatted_input)))

if __name__ == "__main__":
    Main("2023/Day01/main_input.txt")