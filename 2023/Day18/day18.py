from dataclasses import dataclass
import numpy as np
from skspatial.measurement import area_signed

@dataclass
class instruction:
    direction: str
    length: int
    colour: str

def parse1(filename):
    result = []
    with open(filename,"r") as file:
        for line in file:
            data = line.strip().split()
            result += [instruction(data[0], int(data[1]), data[2])]
    return result

def parse2(filename):
    result = []
    num_to_direction = {
        '0': "R",
        '1': "D",
        '2': "L",
        '3': "U"
    }
    with open(filename,"r") as file:
        for line in file:
            data = line.strip().split()[2][2:-1]
            direction = num_to_direction[data[-1]]
            length = int(data[0:-1], 16)
            result += [instruction(direction, length, "N/A")]
    return result

def add_tuples(t1,t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def scale_tuple(t1,s):
    return (t1[0]*s, t1[1]*s)

def update_dimensions(current, dimensions):
    return (min(current[1], dimensions[0]), max(current[1], dimensions[1]), min(current[0], dimensions[2]), max(current[0], dimensions[3]))

def shoelace(x,y):  # x = set of x points / y = set of y points s.t. (x[i],y[i]) describes a point on the polygon
    total = 0
    for i in range(len(x)):
        total += x[i-1]*y[i]-x[i]*y[i-1]
    return np.abs(total*0.5)

def build_polygon(instruction_set):
    x_set = []
    y_set = []
    polygon = []
    perimeter_points = 0
    current = (0,0)
    dimensions = (0,0,0,0)
    direction_to_step = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
    }
    for instruction in instruction_set:
        step = direction_to_step[instruction.direction]
        length = instruction.length
        current = add_tuples(current, scale_tuple(step, length))
        perimeter_points += length
        dimensions = update_dimensions(current, dimensions)
        polygon.insert(0, [current[0], current[1]])
    #    polygon += [ [current[0], current[1]] ]
        x_set += [current[0]]
        y_set += [current[1]]
    x_set = list(map(lambda x: x-dimensions[0], x_set))
    y_set = list(map(lambda x: x-dimensions[2], y_set))
    #print("perimeter is:", perimeter_points)
    return ((x_set, y_set), perimeter_points)
    #return (polygon, perimeter_points)

def part_a(parsed_data):
    poly = build_polygon(parsed_data)
    ans = int(shoelace(poly[0][0], poly[0][1])) + int(poly[1]/2) + 1
    #ans = int(area_signed(poly[0])) + int(poly[1]/2) + 1
    return ans

def main(filename):
    parsed_data = parse1(filename)
    a_sol = part_a(parsed_data)
    print(a_sol)
    new_parsed_data = parse2(filename)
    b_sol = part_a(new_parsed_data)
    print(b_sol)

if __name__ == '__main__':
    main('2023/Day18/main_input.txt')