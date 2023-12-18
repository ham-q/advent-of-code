def parse(filename):
    with open(filename, "r") as file:
        for line in file:
            return line.strip().split(",")

def hash(str):
    result = 0
    for char in str:
        result += ord(char)
        result = result * 17
        result = result % 256
    return result

def part_a(parsed_data):
    result = 0
    for string in parsed_data:
        result += hash(string)
    return result

def part_b(parsed_data):
    boxes = {}
    for i in range(256):
        boxes[i] = {}
    
    for string in parsed_data:
        if string[-1] == "-":
            label = string[:-1]
            box = hash(label)
            if label in boxes[box]:
                boxes[box].pop(label)
        else:
            (label, focal) = string.split("=")
            box = hash(label)
            boxes[box][label] = focal

    result = 0
    box_num = 1
    for box in boxes.values():
        slot_num = 1
        for lens in box.values():
            result += box_num * slot_num * int(lens)
            slot_num += 1
        box_num += 1
    
    return result


def main(filename):
    parsed_data = parse(filename)
    a_sol = part_a(parsed_data)
    print(a_sol)
    b_sol = part_b(parsed_data)
    print(b_sol)

if __name__ == '__main__':
    main('2023/Day15/main_input.txt')